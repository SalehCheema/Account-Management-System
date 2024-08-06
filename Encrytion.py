from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self,key=None):
        
        self.key = key
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        return self.cipher.decrypt(ciphertext.encode()).decode()

if __name__ == "__main__":
    EncryptionManager()    
