from pydoc import plain
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(msg.encode('cp1250'))
    return nonce, ciphertext

def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('cp1252')

def mainDES3():
    task = input("Anda ingin enkripsi atau dekripsi? [E/D]").lower()
    if task == 'e':
        nonce, ciphertext = encrypt(input('Masukkan Pesan yang ingin dienkripsi: '))
        print(f'nonce kamu: {nonce}')
        print(f'Pesan yang sudah dienkripsi: {ciphertext}')
    
    if task == 'd':
        nonce = bytes(input('Masukkan nonce kamu: ').encode())
        ciphertext = bytes(input('Masukkan pesan yang ingin didekripsi: ').encode())
        plaintext = decrypt(nonce, ciphertext)
        print(f'Pesan yang sudah didekripsi: {plaintext}')

if __name__ == '__main__':
    mainDES3()