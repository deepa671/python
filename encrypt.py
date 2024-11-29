
from cryptography.fernet import Fernet

# Load the encryption key from the file
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Initialize Fernet with the key
fernet = Fernet(key)

# Read and encrypt the data from the original file
with open("calculator.py", "rb") as file:
    data = file.read()

encrypted_data = fernet.encrypt(data)

# Write the encrypted data to a new file
with open("encrypted_calculator.py", "wb") as enc_file:
    enc_file.write(encrypted_data)

print("File successfully encrypted.")
