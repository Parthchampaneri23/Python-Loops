#Python program to check the validity of password input by users


import re

def password_check(password):
    val = True

    if len(password) < 8:
        print('length should be at least 8')
        val = False

    if not re.search("[a-z]", password):
        print('Password should have at least one lowercase letter')
        val = False

    if not re.search("[A-Z]", password):
        print('Password should have at least one uppercase letter')
        val = False

    if not re.search("[0-9]", password):
        print('Password should have at least one numeral')
        val = False

    if not re.search("[_@$]", password):
        print('Password should have at least one of the symbols _@$')
        val = False

    if val:
        return val

def main():
    passwd = input("Enter password: ")
    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Not a Valid Password")

if __name__ == '__main__':
    main()
