import random

def gcd(bil1, bil2):
    if bil2 == 0:
        return bil1
    else:
        return gcd(bil2, bil1 % bil2)

def multiinv(e, totient):
    for i in range(totient):
        if ((e * i) - 1) % totient == 0:
            return i
        
def prima(bil):
    if bil > 1:
        for j in range(2, int(bil/2) + 1):
            if (bil % j) == 0:
                return False
        else:
            return True
    else:
        return False
            
def buat_keys(p, q):
    if p == q: 
        raise ValueError('nilai p dan q tidak boleh sama')
    elif not (prima(p) and prima(q)): 
        raise ValueError('kedua bilangan harus merupakan bilangan prima.')
    n = p * q
    λ = (p - 1) * (q - 1)
    e = random.randrange(1, λ)
    temp = gcd(e, λ)
    while temp != 1:
        e = random.randrange(1, λ)
        temp = gcd(e, λ)
    d = multiinv(e, λ)

    return (e, n), (d, n)

def encrypt(publicKey, plaintext):
    key, n = publicKey
    ciphertext = [(ord(char) ** key) % n for char in plaintext]
    return ciphertext

def decrypt(privateKey, ciphertext):
    key, n = privateKey
    plaintext = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plaintext)

def stringToArray(message):
    message_list = message[1:len(message) - 1].split(',')
    new_message_list = []
    for i in message_list:
        if i[0] == " ":
            new_message_list.append(int(i[1:]))
        else:
            new_message_list.append(int(i))
    return new_message_list

def mainRSA():
    public, private = 0, 0
    minta_keys = input("Perlu generate public key dan private key?[Y/N]").lower()
    if minta_keys == "y":
        p = int(input("Masukkan bilangan prima: "))
        q = int(input("Masukkan bilangan prima lainnya: "))
        public, private = buat_keys(p, q)
        print("Public key kamu adalah ", public, " dan private key kamu adalah ", private)

        print("""format kunci adalah (d, n), (d) adalah kunci utama dan (n) adalah totient
    ! Simpan dan ingat-ingat keys kamu. !""")
    task = input("Anda ingin Enskripsi atau Dekripsi? [E/ D]").lower()

    if task == "e":
        if public == 0:
            print("! Masukkan Public key kamu, kunci utama(d) dan totient(n) dari public key kamu !")
            key = input("Masukkan public key kamu: ")
            totient = input("Masukkan totient kamu: ")
            public = (int(key), int(totient))
        message = input("Masukkan pesan yang akan dienkripsi: ")
        encrypted_msg = encrypt(public, message)
        print("Pesan kamu yang telah dienkripsi: ")
        print(encrypted_msg)
    if task == "d":
        if private == 0:
            print("! Masukkan Private key kamu, kunci utama(d) dan totient(n) dari public key kamu !")
            key = input("Masukkan private key kamu: ")
            totient = input("Masukkan totient kamu: ")
            private = (int(key), int(totient))
        message = input("Masukkan pesan yang akan didekripsi: ")
        print("Pesan kamu yang telah didekripsi: ")
        print(decrypt(private, stringToArray(message)))

if __name__ == '__main__':
    mainRSA()