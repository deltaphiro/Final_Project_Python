def vigenere_encrypt():

    plain_text=input('Untuk plaintext mohon dimasukkan tanpa spasi.\nMasukkan plaintext Anda : \n')
    print()
    key_text = input('Untuk KEY tolong dimasukkan tanpa spasi.\nMasukkan key Anda : \n')

    plain_text = plain_text.lower()
    key_text = key_text.lower()
    convert_p =[]
    convert_t =[]

    for letter in plain_text:
        number = ord(letter) - 97
        convert_p.append(number)
    # print(convert_p)

    for letter in key_text:
        number = ord(letter) - 97
        convert_t.append(number)
    # print(convert_t)

    if len(convert_p) != len(convert_t):
        if len(convert_p) < len(convert_t):
            add = len(convert_t)-len(convert_p)
            for i in range(add):
                convert_t.pop()
            # print(convert_t)
        elif len(convert_p) > len(convert_t):
            add = len(convert_p) - len(convert_t)
            for i in range(add):
                convert_t.append(convert_t[i])
            # print(convert_t)
        else:
            pass
    else:
        pass

    zipped_list = zip(convert_p, convert_t)
    total = [x + y for (x, y) in zipped_list]
    # print(total)

    new_list = []
    for i in range(len(total)):
        math = total[i]%26
        new_list.append(math)
    # print(new_list)

    print()
    print('ChipherText :')

    for i in range(len(new_list)):
        conv = chr(new_list[i] + 97)
        print(conv.upper(), end='')

    print()
 



def vigenere_decrypt():

    chipher_text=input('Untuk chiphertext mohon dimasukkan tanpa spasi.\nMasukkan chiphertext Anda : \n')
    print()
    key_text = input('Untuk KEY tolong dimasukkan tanpa spasi.\nMasukkan key Anda : \n')

    chipher_text = chipher_text.lower()
    key_text = key_text.lower()
    convert_c =[]
    convert_t =[]

    for letter in chipher_text:
        number = ord(letter) - 97
        convert_c.append(number)
    # print(convert_c)

    for letter in key_text:
        number = ord(letter) - 97
        convert_t.append(number)
    # print(convert_t)

    if len(convert_c) != len(convert_t):
        if len(convert_c) < len(convert_t):
            add = len(convert_t)-len(convert_c)
            for i in range(add):
                convert_t.pop()
            # print(convert_t)
        elif len(convert_c) > len(convert_t):
            add = len(convert_c) - len(convert_t)
            for i in range(add):
                convert_t.append(convert_t[i])
            # print(convert_t)
        else:
            pass
    else:
        pass

    zipped_list = zip(convert_c, convert_t)
    minus = [x - y for (x, y) in zipped_list]
    # print(minus)

    new_list = []
    for i in range(len(minus)):
        if i < 0:
            math = minus[i] + 26
        else:
            math = minus[i] % 26
        new_list.append(math)
    # print(new_list)

    print()
    print('PlainText :')

    for i in range(len(new_list)):
        conv = chr(new_list[i] + 97)
        print(conv.upper(), end='')
    print()



vigenere_encrypt()
vigenere_decrypt()