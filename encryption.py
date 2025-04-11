from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Key must be 32 bytes for AES-256
SECRET_KEY = get_random_bytes(32)

def pad(data):
    return data + b" " * (16 - len(data) % 16)

def encrypt_data(data):
    data = pad(data.encode('utf-8'))
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_data(encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    return decrypted.decode('utf-8').rstrip()
