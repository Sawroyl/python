#Name=Bipin Tamang
#ID=2331195
def welcome():
    """This fucntion prints the welcome message"""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
def encrypt(message, shift):
    """ This function encrypts the message by shifting each letter by the shift value"""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code += shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_message += chr(char_code)#chr is use to change character from alpha
            else:
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_message += chr(char_code)
    return encrypted_message
 
def decrypt(message, shift):
    """ This function decrypts the message by shifting each letter by the negative shift value"""
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code -= shift
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_message += chr(char_code)
            else:  
                if char_code < ord('a'):
                    char_code += 26
                decrypted_message += chr(char_code)
    return decrypted_message
 
def test_mode(mode): 
    """This function returns True if mode is valid (i.e. "encrypt(e)" or "decrypt(d)"), False otherwise"""
    if mode.lower() == "e" or mode.lower() == "d":
        return True
    else:
        return False
 
def check_response(response):
    """ This function returns True if response is valid (i.e. "y" or "n"), False otherwise"""
    if response.lower() == "y" or response.lower() == "n":
        return True
    else:
        return False
 
def main():
   
    """This function acts as the main function of the program"""
    welcome()
    while True:
        mode = input("Would you like to encrypt(e) or decrypt(d) ")
        while not test_mode(mode):
            print("Invalid mode. Please enter either 'encrypt(e)' or 'decrypt(d)'.")
            mode = input("Enter mode (encrypt(e)/decrypt(d)): ")
        if mode=="e":
            message=input("Enter a message to encrypt: ")
        else:
            message=input("Enter a message to decrypt: ")
        shift = int(input("Enter the shift value : "))
        if mode == "e":
            print("The encrypted message: " + encrypt(message, shift))
        else:
            print("The decrypted message: " + decrypt(message, shift))
        response = input("Would you like to encrypt or decrypt another message(y/n): ")
        while not check_response(response):
            print("Invalid response. Please enter either 'y' for yes or 'n' for no.")
            response = input("Would you like to encrypt or decrypt another message (y/n): ")
        if response.lower() == "n":
            print("Thank you")
            break
 
if __name__ == "__main__":
    main()
