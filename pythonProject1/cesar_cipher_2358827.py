def welcome():
    print("Welcome to the Caesar Cipher. \nThis program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    ed = input("Would you like to encrypt (e) or decrypt (d): ")
    ed = ed.lower()
    while ed != 'e' and ed != 'd':
        print("Invalid Mode")
        ed = input("Would you like to encrypt (e) or decrypt (d): ")
    if ed == 'e':
        msg = input("What message would  you like encrypt:")
        msg = msg.upper()
    else:
        msg = input("What message would  you like decrypt:")
        msg = msg.upper()

    try:
        shift = int(input("What is the shift number: "))
        if 1 <= shift <= 26:
            return ed, msg, shift
        else:
            print("Invalid Shift")
            shift = int(input("What is the shift number: "))
    except ValueError:
        print("Invalid Shift")
        shift = int(input("What is the shift number: "))



def encrypt(mesg, key):
    emsg = ""
    mesg = mesg.upper()
    for char in mesg:
        if char.isupper():
            emsg += chr((ord(char) + key - 65) % 26 + 65)
        else:
            emsg += chr((ord(char) + key - 97) % 26 + 97)
    return emsg


def get_cipherletter(new_key, letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alpha:
        return alpha[new_key]
    else:
        return letter


def decrypt(key, mesg):
    mesg= mesg.upper()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultant = ''
    for letter in mesg:
        new_key = (alph.find(letter) - key) % 26
        resultant = resultant + get_cipherletter(new_key, letter)
    return resultant


def main():
    welcome()
    result = enter_message()
    if result[0] == "e":
        encryptedmsg = encrypt(result[1], result[2])
        print(encryptedmsg)
    else:
        print(decrypt(result[2], result[1]))
    ano = input('Would you like to encrypt or decrypt another message? (y/n): ')
    while ano != 'n' and ano != 'y':
        ano = input('Would you like to encrypt or decrypt another message? (y/n): ')
        if ano == 'y':
            enter_message()
            continue
        elif ano == 'n':
            break
    print('Thanks for using the program, goodbye!')
main()


