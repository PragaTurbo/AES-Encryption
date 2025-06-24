import os
import hashlib
import traceback
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from datetime import datetime

KEY_FILE = "secret.key"

# Generate AES key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

# Load key (or create if missing)
def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Calculate SHA256 hash
def calculate_hash(filepath):
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

# Log encryption/decryption actions
def log_metadata(original, modified, hash_val, action):
    with open("file_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} | {action} | {original} -> {modified} | SHA256: {hash_val}\n")

# Encrypt a file
def encrypt_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filepath, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)
        encrypted_filename = filepath + ".enc"

        with open(encrypted_filename, "wb") as enc_file:
            enc_file.write(encrypted)

        hash_val = calculate_hash(filepath)
        log_metadata(filepath, encrypted_filename, hash_val, "ENCRYPTED")

        messagebox.showinfo("Success", f"File encrypted:\n{encrypted_filename}")
    except Exception as e:
        traceback.print_exc()
        messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")

# Decrypt a file
def decrypt_file():
    filepath = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not filepath:
        return

    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filepath, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        output_filename = filedialog.asksaveasfilename(defaultextension="", title="Save Decrypted File As")
        if not output_filename:
            return

        with open(output_filename, "wb") as dec_file:
            dec_file.write(decrypted)

        hash_val = calculate_hash(output_filename)
        log_metadata(filepath, output_filename, hash_val, "DECRYPTED")

        messagebox.showinfo("Success", f"File decrypted:\n{output_filename}")
    except Exception as e:
        traceback.print_exc()
        messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

# Main GUI
def main():
    window = Tk()
    window.title("Secure File Storage")
    window.geometry("400x250")
    window.config(bg="#121212")

    Label(window, text="Secure File Storage", font=("Helvetica", 16, "bold"), fg="white", bg="#121212").pack(pady=20)

    Button(window, text="Encrypt File", font=("Helvetica", 12), command=encrypt_file, width=20, bg="#00adb5", fg="white").pack(pady=10)
    Button(window, text="Decrypt File", font=("Helvetica", 12), command=decrypt_file, width=20, bg="#393e46", fg="white").pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
