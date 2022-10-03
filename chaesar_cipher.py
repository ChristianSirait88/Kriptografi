from cgitb import text
from random import randint, random
import string
from time import sleep

alphabet = string.ascii_lowercase

def enkripsi(text,s):
    hasil = ""
 
    for i in range(len(text)):
        char = text[i]
 
        # enkripsi uppercase characters
        if (char.isupper()):
            #hasil += chr((ord(char) + s )) // MENYEBABKAN ERROR KETIKA CHAESAR CHIPER DI Z
            hasil += chr((ord(char) + s - 65) % 26 + 65)
 
        # enkripsi lowercase characters
        else:
            hasil += chr((ord(char) + s - 97) % 26 + 97)
 
    return hasil

def decrypt():
    print("Decrypt Caesar Chiper")
    kalimat = input("Masukan Encrypted Text : ")
    key = int(input("Masukan Kunci : "))
    encrypted_message = kalimat.lower()
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Pesan Anda : ")
    print(decrypted_message)

def main():
    text = input("Masukan plain text: ")
    s = 24
    print ("Text  : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + enkripsi(text,s))
    print("\n")
    decrypt()
    
if __name__ == "__main__":
    main()