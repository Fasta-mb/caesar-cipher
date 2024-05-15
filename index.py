import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)


def encrypt(text, shift):
    encryptedMessage = ""
    for letter in text:
        position = alphabet.index(letter)
        shift_position = position + shift
        code = alphabet[shift_position]
        encryptedMessage += code
        
    print(encryptedMessage)
        


def decrypt(text, shift):
    decryptedMessage = ""
    for letter in text:
        position = alphabet.index(letter)
        shift_position = position - shift
        code = alphabet[shift_position]
        decryptedMessage += code
        
    print(decryptedMessage)



is_over = False
while not is_over:    
    direction = input("Type 'encode' to encrypt, 'decode' to decript:\n").lower() 
    
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
    else:
        print("oops wrong typing..")
      
    if direction == 'encode':
        encrypt(text, shift)
    if direction == 'decode':
        decrypt(text, shift)
        break
