from Crypto.Cipher import Blowfish
from struct import pack


def BlowFish_Encrypt():

    plaintext=input('Masukkan plaintext Anda :\n')
    print()
    key = input('Masukkan key Anda [min length 4]:\n')

    bs = Blowfish.block_size
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_CBC)
    plen = bs - len(plaintext.encode()) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    cipher_msg = cipher.iv + cipher.encrypt(plaintext.encode() + padding)

    print()
    print(f"Chiphertext :\n{cipher_msg}")

# BlowFish_Encrypt()

def BlowFish_Decrypt():

    ciphertext=input('Masukkan chiphertext Anda :\n')
    print()
    key = input('Masukkan key Anda [min length 4]:\n')

    ciphertext_b = ciphertext.encode()
    bs = Blowfish.block_size
    iv = ciphertext_b[:bs]
    ciphertext_bs = ciphertext_b[bs:]

    key_b = key.encode()

    cipher = Blowfish.new(key_b, Blowfish.MODE_CBC, iv)
    plaintext_msg = cipher.decrypt(ciphertext_bs)

    last_byte = plaintext_msg[-1]
    plaintext = plaintext_msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]

    print()
    print(f"Plaintext :\n{repr(plaintext)}")

# BlowFish_Decrypt()

