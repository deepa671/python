import base64
import hashlib

# Your custom string
custom_key = "deepa5547"

# Create a 32-byte key using SHA-256 and encode in base64
hashed_key = hashlib.sha256(custom_key.encode()).digest()
base64_key = base64.urlsafe_b64encode(hashed_key)

print("Custom base64-encoded Fernet key:", base64_key.decode())
