import hashlib

def analyzer(input):


    commonPasswords = open('password.txt', 'r')

    for password in commonPasswords:

        encryption = password.encode('utf-8')
        hasher = hashlib.md5(encryption.strip()).hexdigest()

        if hasher == input:
            print('Password is not secure enough')
            break
        else:
            print('No Match was found')
            print('Password is strong')
            break


def converter(x):

    passwordHash = hashlib.md5(x.encode())
    md5er = passwordHash.hexdigest()

    return analyzer(md5er)

if __name__ == '__main__':
    converter(input('Create a Password: '))
