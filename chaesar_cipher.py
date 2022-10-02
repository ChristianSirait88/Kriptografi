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
 

def main():
    text = "ZBELAJARKRIPTOGRAFIUNTUKINDONESIA"
    s = 4
    print ("Text  : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + enkripsi(text,s))
    
    
if __name__ == "__main__":
    main()