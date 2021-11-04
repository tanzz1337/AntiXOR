print("Author : Syncr0ne From Baturaja 1337")

import fontstyle
import os

text = fontstyle.apply('<AntiXOR >', 'bold/Italic/red/GREEN_BG')
print(text)

print("AntiXOR V.1")
def cipher_encrypt():
    text = str(input("Masukan Pesan : "))
    key = input("Masukan Key : ")

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(text)):
        temp = ord(text[i]) ^ ord(key[key_itr])
        
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Encrypted Text: {}".format(encrypt_hex))


def cipher_decryption():
    msg = input("Masukan Pesan : ")
    key = input("Masukan Key : ")

    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i+2]).decode('utf-8')

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Decrypted Text: {}".format(decryp_text))

def main():
    choice = int(input("1. > Encryption Text\n2. > Decryption\nEnter Choice >>> "))
    if choice == 1:
        print("{ --- Encryption Text --- }")
        cipher_encrypt()
    elif choice == 2:
        print("{ --- Decryption Text --- }")
        cipher_decryption()
    elif choice == 3:
    	#os.system('cls')
    	print("> [ About Tools ] \nTools sederhana untuk melakukan encrypt/decrypt sebuah XOR\n>Next Update : From Path ( Windows & Linux) $ Decode Methode\n>Author : Syncr0ne/Sultan From Baturaja1337")
    	os.system('exit')
    else:
        print("Pilihan Tidak Ada !!")
        # os.system('cls')
        return main()
 
if __name__ == "__main__":
    main()
