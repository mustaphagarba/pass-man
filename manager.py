from cryptography.fernet import Fernet




def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyfile:
        keyfile.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

pwd = input("What is the master password? : ")

def view_password():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split('|')
            print('User: ', user, '\n Password: ', passw)
def add_password():
    name = input('What is the account name? : ')
    password = input('WHat is the account password? : ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + password + '\n')

while True:
    mode = input("Would you like to add a new password or view existing passwords (add, view)? :" )
    if mode == 'view' or mode == 'View':
        pass
    elif mode == 'add' or mode == 'Add':
        pass
    else:
        print('Invalid selection')
