from Crypto.Cipher import AES
import os

FOLDER = "./test_folder/"
KEY_FILE = "key.bin"

def decrypt_file(path, key):
    with open(path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(data).rstrip(b" ")
    original_path = path.replace(".locked", "")
    with open(original_path, 'wb') as f:
        f.write(decrypted)
    os.remove(path)

def decrypt_all():
    with open(KEY_FILE, 'rb') as f:
        key = f.read()

    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            if file.endswith(".locked"):
                full_path = os.path.join(root, file)
                decrypt_file(full_path, key)

    print("✅ All files decrypted successfully.")

if __name__ == "__main__":
    decrypt_all()
