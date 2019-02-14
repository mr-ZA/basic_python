import sys

def decrypt(string, key):
    decrypted = ''
    for i in string:
        index = (ord(i) - key)
        decrypted = decrypted + chr(index)
    return decrypted

def encrypt(string, key):
    encrypted = ''
    for i in string:
        index = (ord(i) + key)            #Возвращает числовое представление для указанного символа.
        encrypted = encrypted + chr(index)
    return encrypted

def main():
    print('=' * 10 + "\n   MENU\n" + '=' * 10)
    print("1.Encrpyt")
    print("2.Decrypt")
    print("3.Quit")
    while True:
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3']:
            print ("Error, set the value from 1-3")
        elif choice == '1':
            strng = input("Please enter the string to encrypt: ")
            while True:
                key = int(input("Please enter an offset between 1-94: "))
                if key in range(1, 95):                                       #exclude 95, 1-94
                    print (encrypt(strng, key))
                    main()
        elif choice == '2':
            strng = input("Please enter the string to be decrypted: ")
            while True:
                key = int(input("Please enter off-set between 1-94: "))
                if key > 0 and key <= 94:
                    print(decrypt(strng, key))
                    main()
        elif choice == '3':
            print ("Goodbye.")
            sys.exit()

main()
