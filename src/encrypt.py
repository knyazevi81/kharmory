from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from math import ceil


class CodeEncrypted():

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.key = get_random_bytes(32)

    def __open_code_text(self) -> str:
        """
        Инкапсулированный метод для вывода кода в .py файле
        """
        with open(self.file_path, "r") as text:
            return text.read()
    
    def crypto_code(self):
        text = self.__open_code_text()

        cipher = AES.new(self.key, AES.MODE_ECB) # Инициализируйте шифровщик AES с ключом
        # Добавим дополнительное заполнение (pad), если длина текста не кратна 16 байтам (размер блока AES)
        pad_text = pad(text.encode('utf-8'), AES.block_size)
        

        encrypted_text = cipher.encrypt(pad_text)# Зашифруйте текст
        encoded_text = base64.b64encode(encrypted_text)

        return {
            "code": encoded_text.decode(),
            "key": self.key
        }