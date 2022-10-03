from inspect import trace


def encrypt_reverse():
   print("Encrypt Dengan Reverse Chiper")
   plaintxt = input("Masukan Plain Text : ")
   translated = '' #chiper text
   i = len(plaintxt) - 1

   while i >= 0:
      translated = translated + plaintxt[i]
      i = i - 1
   print("Cipher text adalah : ", translated)

   print("Decrypt Dengan Reverse Chiper")

def decrypt_reverse():
   ciphertxt = input("Masukan Cipher Text : ")
   translated = '' #chiper text
   i = len(ciphertxt) - 1

   while i >= 0:
      translated = translated + ciphertxt[i]
      i = i - 1
   print("Plain text adalah : ", translated)
