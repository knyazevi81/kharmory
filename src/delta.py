import argparse
import sys
import logging
import os
from pathlib import Path, WindowsPath
from encrypt import *

from config import CONFIG


def validate_file_path(path: str) -> bool:
    file_path: WindowsPath = Path(path)
    return file_path.exists() and file_path.suffix == ".py"


def create_obfus(data: dict[str: bytes]) -> None:
    os.mkdir("dist")
    current_path = Path.cwd().joinpath("dist")
    print(current_path)

    main_text = f"""from kharmor.decrypter import Armor\nexec(Armor().decrypter__(b'{data['code']}'))"""

    decrypt_text = f"""from Crypto.Cipher import AES\nimport base64\nclass Armor():\n    def __init__(self):\n        self.key = {data['key']}\n    def decrypter__(self, encrypted_text: bytes):\n      cipher = AES.new(self.key, AES.MODE_ECB)\n      decoded_text = base64.b64decode(encrypted_text)\n      decrypted_text = cipher.decrypt(decoded_text)\n      return decrypted_text.decode('utf-8').replace(decrypted_text.decode('utf-8').split('\\n')[-1], "")"""
    
    test_decrypt_text = f"""from Crypto.Cipher import AES\nimport base64\nclass Armor():\n    def decrypter__(self, ec: bytes): return AES.new({data['key']}, AES.MODE_ECB).decrypt(base64.b64decode(ec)).decode('utf-8').replace(AES.new({data['key']}, AES.MODE_ECB).decrypt(base64.b64decode(ec)).decode('utf-8').split('\\n')[-1], "")"""
    
    Path(str(current_path) + "\main.py").write_text(main_text)
    os.mkdir(str(current_path) + "\kharmor")
    Path(str(current_path) + "\kharmor\decrypter.py").write_text(test_decrypt_text)


def main_entry() -> None:
    parser = argparse.ArgumentParser(
        description=""
    )

    parser.add_argument("-d", "--debug", type=bool, default=False)
    parser.add_argument("--file", type=str, help="Параметр для указания пути")
    args =  parser.parse_args(sys.argv[1:])

    CONFIG["target_file"] = args.file
    CONFIG["debug"] = args.debug

    if CONFIG["debug"]:
        # Включаем логгирование
        ...

    if not validate_file_path(CONFIG["target_file"]):
        print("Файл не найден...")
        exit()

    
def main() -> None:
    main_entry()
    code_data = CodeEncrypted(CONFIG["target_file"]).crypto_code()
    create_obfus(code_data)




if __name__ == "__main__":
    main()