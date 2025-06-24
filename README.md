# 🔐 Securing File System using AES (GUI-Based)

A simple and intuitive desktop tool to **secure your files using AES-256 encryption**, built with Python and Tkinter. Easily encrypt or decrypt any file without needing technical skills — just point and click.

---

## 📦 Packages Needed

- `cryptography`  
  Install it via pip:
  ```bash
  pip install cryptography

🧠 How the System Works
🔐 Encryption Process:
User selects a file via the GUI.

AES key is auto-generated (or loaded from secret.key).

The file is read as binary, encrypted using Fernet (AES-256 under the hood).

An encrypted copy is saved with .enc extension.

A SHA256 hash of the original file is computed and logged for integrity.

Original file remains untouched unless configured otherwise.

🔓 Decryption Process:
User selects a .enc file.

The encryption key from secret.key is loaded.

The file is decrypted back into its original binary content.

The user chooses where to save the decrypted file (e.g., mydoc.pdf).

A new SHA256 hash is logged for verification.

🖼️ Interface Preview (Optional)
Add a screenshot of the GUI here if you'd like.

📁 Output Files
secret.key → Encryption key (keep this safe!)

file.enc → Encrypted file

decrypted_file → Decrypted output (you choose name/location)

file_log.txt → Log of actions with timestamps and SHA256 hashes

💡 Why Use This?
This tool is designed for:

Students learning cybersecurity

Non-tech users who want to protect sensitive files

Anyone needing quick, offline AES encryption without command-line hassle

🛠️ Built With
Python 3

cryptography

tkinter

hashlib


How to Run the Program
Open your terminal or VSCode terminal.

Navigate to the project folder:

```bash
cd path/to/your/project
python secure_storage.py
