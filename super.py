from cgitb import text
from random import randint, random,choice
import random
import string
from time import sleep

alphabet = string.ascii_lowercase

def enkripsi_caesar(text,s):
    hasil = ""
 
    for i in range(len(text)):
        char = text[i]
 
        # enkripsi_caesar uppercase characters
        if (char.isupper()):
            #hasil += chr((ord(char) + s )) // MENYEBABKAN ERROR KETIKA CHAESAR CHIPER DI Z
            hasil += chr((ord(char) + s - 65) % 26 + 65)
 
        # enkripsi_caesar lowercase characters
        else:
            hasil += chr((ord(char) + s - 97) % 26 + 97)
 
    return hasil

def decrypt_caesar(kalimat, key):
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

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
    

def execution_super():
    print("Super Encrypted\n")
    plain_text = input("Masukan Text: ")
    plain_text = plain_text.upper()
    keyword = input("Masukan Kunci : ")
    keyword =keyword.upper()
    s = randint(1,26)
    caesar = enkripsi_caesar(plain_text,s)
    print(caesar)
    i = len(caesar) - 1
    translated = ''
    while i >= 0:
        translated = translated + caesar[i]
        i = i - 1
    print(translated)
    key = generateKey(translated, keyword)
    cek = len(key)
    cipher_text = cipherText(translated,key)
    print("encrypted message : ",cipher_text)
    a = ''.join(random.choice(alphabet) for i in range(2))
    b=str(s)
    c=len(b)
    sandi = a+key+a+b
    print("sandi = ",sandi)
    print("Super Decrypt")
    text = cipher_text.upper()
    kalimat = input("Masukan Sandi : ")
    if kalimat== sandi:
        sandi = sandi.upper()
        v=sandi[2:cek+2]
        tahap1=  originalText(text, v)
       
    translated = '' #chiper text
    i = len(tahap1) - 1
    while i >= 0:
        translated = translated + tahap1[i]
        i = i - 1
    tahap2=translated
    key=sandi[cek+4:len(sandi)]
    key=int(key)
    decrypt_caesar(tahap2,key)    

