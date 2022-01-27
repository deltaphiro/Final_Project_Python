from Rsa_ende import *
from DES3 import *
while True:

    print("============================================================")
    print("            ~~~       C R Y P T H O        ~~~              ")
    print("============================================================")
    print("t o o l s k r i p t o g r a f i b e r b a s i s b a h a s a ")
    print("\n")

    tipe_key = input("Tool kriptografi yang ingin anda gunakan : \n 1.Vigenere \n 2.BlowFish \n 3.TripleDES \n 4.RSA \n 5.TwoFish \n 6.AES \nPilihan Anda : ")
    if tipe_key == "1":
        pass
    elif tipe_key == "2":
        plain_text = input("Untuk plaintext mohon dimasukkan tanpa spasi. \n Masukkan plaintext Anda : \n")
    elif tipe_key == "3":
        des = True
        while des ==True:
            mainDES3()
            if input("Apakah Anda masih  ingin lanjut? [Y/N] ").lower() == 'n':
                print("Terima kasih! \n")
                des = False
        else:
            pass
    elif tipe_key == "4":
        rsa = True
        while rsa ==True:
            mainRSA()
            if input("Apakah Anda masih  ingin lanjut? [Y/N] ").lower() == 'n':
                print("Terima kasih! \n")
                rsa = False
        else:
            pass
    elif tipe_key == "5":
        plain_text = input("Untuk plaintext mohon dimasukkan tanpa spasi. \n Masukkan plaintext Anda : \n")
    elif tipe_key == "6":
        plain_text = input("Untuk plaintext mohon dimasukkan tanpa spasi. \n Masukkan plaintext Anda : \n")
    else:
        print("Tolong input dengan benar.")