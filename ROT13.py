
rot13trans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
   
rot13table = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

rot13chiper = str.maketrans(rot13trans, rot13table)

#fungsi enkripsi
def rot13(text):
   return text.translate(rot13chiper)
def main():

   plaintxt = input("masukan plain text: ")
   chiper_text = rot13(plaintxt)
   print("Chiper text: ", chiper_text)
	
if __name__ == "__main__":
   main()