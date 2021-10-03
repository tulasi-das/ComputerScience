from cryptography.fernet import Fernet


'''def writeKey():
    key = Fernet.generate_key()
    with open("key.key","wb") as keyFile:
        keyFile.write(key) '''
def loadkeys():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
pwd = input("What is the master password ")
key = loadkeys() + pwd.encode()
fer = Fernet(key) 


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            words = line.rstrip()
            user, passw = words.split('|')
            print("User:",user,", Password:",passw)
            
    
def add():
    name = input("Enter your user name: ")
    password = input("Enter your password: ")
    with open('password.txt','a') as f:
        f.write(name+" | "+password+"\n")    

while True:
    mode = input("Would you like to add a new password or view the password(add/view) or press q to exit ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view() 
    elif mode == 'add':
        add()
    else:
        print("Invalid input")