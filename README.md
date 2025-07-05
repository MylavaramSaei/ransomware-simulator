# 🛡️ Ransomware Simulator (Educational Project)

This project is a **safe, controlled ransomware simulation** built for educational purposes. It demonstrates how real-world ransomware works — by encrypting files and generating a ransom note — all within a test folder and without any malicious intent.

> ⚠️ **Disclaimer:** This tool is strictly for academic use. Do not run it on real or sensitive data. The author is not responsible for misuse.

---

## 📌 Features

- 🔐 Encrypts files in a specified folder using AES-256 (CBC)
- 📝 Generates a simulated ransom note
- 🔓 Decryptor restores files using the original key
- 🧪 Designed for Linux (tested on Kali Linux)
- 💻 Python-based with PyCryptodome library

---

## 🚀 How It Works

1. Drop test files into `test_folder/`
2. Run `encryptor.py` to:
   - Encrypt files with a randomly generated AES key
   - Rename them with `.locked` extension
   - Drop a `README.txt` ransom note
3. Use `decryptor.py` (with the saved `key.bin`) to restore files

---

## 🛠️ Technologies Used

- Python 3.x
- Kali Linux (Debian-based)
- [PyCryptodome](https://pypi.org/project/pycryptodome/)
- Git & GitHub
- FFmpeg (optional for demo GIF conversion)

---

## 🧪 Sample Output

```bash
$ ls test_folder/
README.txt  sample.txt.locked

$ python3 decryptor.py
Decryption complete.

$ ls test_folder/
sample.txt
