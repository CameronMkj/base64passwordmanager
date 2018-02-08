# Based on ctrl + shift + numpad you will be returned a password and then pressed enter.
from Crypto import Random
from Crypto.Cipher import AES
import mkj_pkg.main as mkj
import sys, time, keyboard, hashlib, base64, os
from pynput.keyboard import Key, Controller

keyboardTwo = Controller()

def reader():
    reader = open("Encryptr.txt", "r")
    readed = reader.read()
    print(readed)
    finalOne = base64.b64decode(readed)
    mkj.ty(finalOne)
    mkj.pr(Key.enter)

mkj.cls()
mkj.shortimportant("MKJ Password Manager")
print("1. Change Password.")
print("2. Use program.")
inputOne = raw_input("...")
if inputOne == "1":
    mkj.cls()
    print("What password would you like to encrypt? ")
    key = raw_input("...")
    encryptedKey = base64.b64encode(key)
    file = open("Encryptr.txt", "w")
    file.write(encryptedKey)
    mkj.cls()
    print("(+)- Password Added!")
    print("Press any button to exit... ")
    raw_input("")
    os.system("python main.py")
    # sys.exit(1)

elif inputOne == "2":
    while True:
        if keyboard.is_pressed('ins'):
            reader()
            time.sleep(1)

    # print("What key would you like to use? ")
    # password = raw_input("...")
    # key = hashlib.sha256(password).digest()
    # print(key)
    # baseEncryptor = "pineapple"
    # IV = 16 * '\x03'
    # mode = AES.MODE_CBC
    # encryptor= AES.new(key, mode, IV=IV)
    # print("What text would you like to encrypt?")
    # text = raw_input("...")
    # finalText = text * 64 + baseEncryptor * 128
    # encryptedPass = encryptor.encrypt(finalText)
    # print(encryptedPass)
    # finalDecrypt = int(encryptedPass) / 64 - int(baseEncryptor) / 128
    # print(finalDecrypt)
    # file = open("Encryptr.txt", "w")
    # file.write(encryptedPass)


    # print("What is the password you would like to add to the database? ((16))")
    # passwordUnencrypted = raw_input("...")
    # print("What encryption key would you like to use? ((16, 24, 32))")
    # passwordKey = raw_input("...")
    # encryption_suite = AES.new(passwordKey, AES.MODE_CBC, 'This is an IV456')
    # passwordEncrypted = encryption_suite.encrypt(passwordUnencrypted)
    # print(passwordEncrypted)
# raw_input = "What is your encryption key? "
# encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# cipher_text = encryption_suite.encrypt("llllllllllllllll")
# encryptedPass = encrypt("password", 16)
# print(cipher_text)
# file = open("Encryptr.txt", "w")
# file.write()