from cryptography.fernet import Fernet

KEY = b'vE2QGrg4S8KuuPLDf3FQ5SHFPfPrUkSGiMYnqCsLl6Y='
cipher = Fernet(KEY)

def encrypt_message(msg):
    return cipher.encrypt(msg.encode()).decode()

def decrypt_message(token):
    return cipher.decrypt(token.encode()).decode()
