
---

# Shipay Certificate Request Generator

This utility generates a Certificate Signing Request (CSR) and a private key for Shipay environments, facilitating secure communication. It's designed to be used by companies needing to automate the creation of these certificates as part of their integration with Shipay services.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or newer
- pip (Python package installer)
- Virtualenv (optional but recommended for environment isolation)

### Setting Up

1. **Clone the Repository**

   Begin by cloning the repository to your local machine:

   ```
   git clone https://github.com/agentkyo/generate_new_csr.git
   cd shipay-csr-generator
   ```

2. **Create a Virtual Environment (Optional)**

   It's recommended to create a virtual environment to keep dependencies required by the project separate from your global Python environment.

   ```
   python -m venv .venv
   ```

   To activate the virtual environment, run:

   - On Windows:
     ```
     .venv\Scripts\activate
     ```

   - On Unix or MacOS:
     ```
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   With the virtual environment activated, install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

### Generating Certificate Requests

1. **Configuration**

   Open the Python script or Notebook where you'll run the certificate request generation. Fill in the following details:

   - `YOUR_COMPANY_NAME_HERE`: Replace with your company's name.
   - `COUNTRY`: The 2-letter ISO code for your country, in uppercase (e.g., `BR` for Brazil).
   - `STATE_NAME`: The state or province name or code, in uppercase.
   - `ENVIROMENT`: Specify the environment for which you're generating the certificate (`staging` or `production`).
   - `YOUR_EMAIL_HERE`: Provide the contact email associated with the certificate.
   - `CITY_CODE`: The city code, if applicable, in uppercase.

2. **Run the Script**

   Execute the script with the following command, ensuring your configuration details are correctly entered:

   ```
   python generate_mtls_certificate_request.py
   ```

   This will generate the CSR and private key in the `./keys/YOUR_COMPANY_NAME/` directory.

    You also could use the JupyterNotebook to generate the certificate

   ```
   python generate_certificate_request.ipynb
   ```

### Troubleshooting

- Ensure all required fields are filled out correctly.
- Verify that your Python environment is correctly set up and activated.
- Check for any error messages in the console and address them as needed.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/agentkyo/shipay-csr-generator/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Caio Vinicius** - *Initial work* - [YourUsername](https://github.com/agentkyo)

See also the list of [contributors](https://github.com/agentkyo/shipay-csr-generator/contributors) who participated in this project.


## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

---
