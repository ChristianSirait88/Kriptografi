from inspect import trace


print("Encrypt Dengan Reverse Chiper")
plaintxt = input("Masukan Plain Text : ")
translated = '' #chiper text
i = len(plaintxt) - 1

while i >= 0:
   translated = translated + plaintxt[i]
   i = i - 1
print("Cipher text adalah : ", translated)

print("Decrypt Dengan Reverse Chiper")
dekrpsi = '' #chiper textbawah
kode = translated
j = len(kode) - 1
while j >= 0:
   dekrpsi = dekrpsi + kode[j]
   j = j - 1
print("Cipher text adalah : ", dekrpsi)