import subprocess
import chardet
import os


class CertificadoGenerator:
    def __init__(self):
        pass

    def run(
        self, company_name, country, state_name, shipay_enviroment, customer_email, uf
    ):
        self.company_name = company_name
        self.country = country
        self.state_name = state_name
        self.shipay_enviroment = shipay_enviroment
        self.customer_email = customer_email
        self.uf = uf
        directory_path = os.path.join("keys", self.company_name)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        self.generate_certificates(directory_path)

    def execute_command(self, cmd):
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        out, err = process.communicate()
        detected_encoding = chardet.detect(err)["encoding"] or "utf-8"

        if process.returncode != 0:
            print(f"Error while exec this command: {err.decode(detected_encoding)}")
            exit(1)
        return out.decode(detected_encoding)

    def generate_certificates(self, directory_path):
        print("Creating private key...")
        key_name = os.path.join(directory_path, f"{self.company_name}.key")
        cmd_generate_key = f"openssl genrsa -out {key_name} 2048"
        self.execute_command(cmd_generate_key)
        print("Creating CSR...")
        csr_name = os.path.join(directory_path, f"{self.company_name}.csr")
        cmd_generate_csr = f"openssl req -new -key {key_name} -out {csr_name} -nodes"
        fields = {
            "Country Name:": self.country.upper(),
            "State or Province Name:": self.uf.upper(),
            "Locality Name:": self.state_name,
            "Organization Name:": self.company_name,
            "Organizational Unit Name:": self.shipay_enviroment,
            "Common Name:": self.company_name,
            "Email Address:": self.customer_email,
            "A challenge password:": "",
            "An optional company name:": "",
        }
        input_data = (
            "\n".join(fields.values()) + "\n"
        ) 
        process = subprocess.Popen(
            cmd_generate_csr,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        out, err = process.communicate(input=input_data.encode("utf-8"))
        detected_encoding = chardet.detect(err)["encoding"] or "utf-8"
        if process.returncode != 0:
            print(f"Erro while try to create CSR: {err.decode(detected_encoding)}")
            exit(1)
        return out.decode(detected_encoding)
