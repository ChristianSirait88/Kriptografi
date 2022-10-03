from chaesar_cipher import *
from Vigenere_cipher import *
from reverse import *
from super import *

def menu_2():
    print("======================\n")
    print("     1. Encrypt \n")
    print("     2. Decrypt \n")
    y_inp = int(input("==> "))
    y = y_inp
    return y

def menu():
    x_inp= input("====> ")
    x = int(x_inp)
    
    match x:
        case 1:
            answer = menu_2()
            if answer == 1:
                execution_chaesar()
            else:
                execution_chaesar_decrypt()
        case 2:
            answer = menu_2();            
            if answer == 1:
                encrypt_reverse()
            else:
                decrypt_reverse()
        case 3:
                execution_vigenere()
        case 4:
                execution_super()
    
def main():
    print("================CRYPTOGRAPHY===================\n")
    print("              1. Chaesar  Chiper               \n")
    print("              2. Reverse  Chiper               \n")
    print("              3. Vigenere Chiper               \n")
    print("              4. Super    Chiper               \n")
    print("===============================================\n")
    menu()
    
if __name__ == "__main__":
    main()