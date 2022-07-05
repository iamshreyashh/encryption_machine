import os.path
import os
from cryptography.fernet import Fernet
numbers = []
def display_Menu_function():
    print("\t\t\t **HELLO PROGRAMMER** \t\t\t\n")
    print("(1)  Select/create data file")
    print("(2)  Encrypt the selected file")
    print("(3)  Dcrypt the selected file")
    print("(4) Exit the program")
def opt1():
    filename = input("Enter file name:")
    filename = filename
    if os.path.exists(filename):
        return filename
    else:
        print("File not found, create file ")
        print()            
def opt2(filename):
    key=Fernet.generate_key()
    with open("mykey.txt","wb") as mykey:
        mykey.write(key)
    x= Fernet(key)
    with open(filename,"rb") as original_file:
        original=original_file.read()
    encrypted=x.encrypt(original)
    with open("enc1_file.txt","wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(" FILE ENCRYPTED SUCCESSFULLY")
    print("ENCRYPTED FILE IS : ",encrypted)
    print("Your key is: ",key)
    print("The encrypted file is saved as enc1_file.txt")
        
def opt3():
    key=input("Enter the Key : ")
    x2=Fernet(key)
    x4=input("Enter the file_name you want to decrypt : ")
    with open(x4,"rb") as encrypted_file2:
        encrypted=encrypted_file2.read()
    decrypted=x2.decrypt(encrypted)
    with open("dec_file.txt","wb") as decrypted_file:
        decrypted_file.write(decrypted)
        print("FILE DECRYPTED SUCCESSFULLY")
    print(decrypted)    
if __name__ == "__main__":
    while(True):
        display_Menu_function()
        opt=input("menu choice: ")
        while opt<="1" or opt<="3":
            if opt=="1":
               x1=opt1()
            elif opt=="2":
                opt2(x1)
            elif opt=="3":
                opt3()
            else:
                break
            opt=input("menu choice: ")