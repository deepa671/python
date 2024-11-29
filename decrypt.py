
from cryptography.fernet import Fernet

# Prompt user to input the security key
security_key = input("Enter the security key: ")

try:
    # Load the encryption key from the user input (base64 encoded)
    key = security_key.encode()  # If the key is entered as a string

    # Initialize Fernet with the key
    fernet = Fernet(key)

    # Decrypt an encrypted file (e.g., encrypted_calculator.py)
    with open("encrypted_calculator.py", "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data to a new file (e.g., calculator.py)
    with open("decrypted_calculator.py", "wb") as dec_file:
        dec_file.write(decrypted_data)

    print("File successfully decrypted.")

except Exception as e:
    print(f"Error: {e}")
