plaintxt = 'Informatika UPN Yogyakarta'
translated = '' #chiper text
i = len(plaintxt) - 1

while i >= 0:
   translated = translated + plaintxt[i]
   i = i - 1
print("Cipher text adalah : ", translated)