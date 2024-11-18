from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyfile:
        keyfile.write(key)'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

master_pwd = input('What is the master password? :')
key = load_key() + master_pwd.encode()
fer = Fernet(key)



pwd = input("What is the master password? : ")

def view_password():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split('|')
            print('User: ', user, '\n ', 'Password: ', str(fer.decrypt(passw.encode())))

def add_password():
    name = input('What is the account name? : ')
    password = input('WHat is the account password? : ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + str(fer.encrypt(password.encode())) + '\n')

while True:
    mode = input("Would you like to add a new password or view existing passwords (add, view)? :" )
    if mode == 'view' or mode == 'View':
        pass
    elif mode == 'add' or mode == 'Add':
        pass
    else:
        print('Invalid selection')
