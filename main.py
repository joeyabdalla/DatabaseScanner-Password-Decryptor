import hashlib
import sqlite3

def analyzer(input):

    conn = sqlite3.connect('passwords_examples.db')
    c = conn.cursor()

    c.execute("SELECT password FROM passwords")
    common_passwords = c.fetchall()

    if common_passwords:
        for password_tuple in common_passwords:
            password = password_tuple[0]

            encryption = password.encode('utf-8')
            hasher = hashlib.md5(encryption.strip()).hexdigest()

            if hasher == input:
                return False
        return True
    else:
        print("Table 'passwords' does not exist in the database.")
        return False

    conn.close()

def converter(x):

    passwordHash = hashlib.md5(x.encode())
    md5er = passwordHash.hexdigest()

    return analyzer(md5er)

if __name__ == '__main__':
    secure_password = False
    while not secure_password:
        password = input('Create a Password: ')
        secure_password = converter(password)
        if not secure_password:
            print('Password is not secure enough. Please try again.')
    print('Password is secure!')
