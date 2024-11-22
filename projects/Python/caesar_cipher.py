#A Caesar Chipher is a simple encryption that moves each letter of the message a fixed number of positions down the alphabet

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha(): # Confirms if the  entry is alphabetic
            index = letters.find(letter.lower())
            new_index = (index + key) % num_letters  
            encrypted_letter = letters[new_index]
            
            ciphertext += encrypted_letter.upper() if letter.isupper() else encrypted_letter
        else:
            ciphertext += letter  
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():  # Confirms if the  entry is alphabetic
            index = letters.find(letter.lower())
            new_index = (index - key) % num_letters  
            decrypted_letter = letters[new_index]
            
            plaintext += decrypted_letter.upper() if letter.isupper() else decrypted_letter
        else:
            plaintext += letter  
    return plaintext

#Welcome

print()
print('*** Welcome to the CAESAR CIPHER PROGRAM! ***')
print()

user_input = input('Do you want to encrypt or decrypt? (e/d): ').lower()
print()

# Encryption option
# Depending on the number "key" chosen that is how far the letter will be shifted 

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    if 1 <= key <= 26:  # Validate key range
        text = input('Enter the text to encrypt: ')
        ciphertext = encrypt(text, key)
        print(f'CIPHERTEXT: {ciphertext}')
    else:
        print("Invalid entry! Please enter a key between 1 and 26.")

# Decrypt option
#To decrypt the message the same number "key" is used in the reverse

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    if 1 <= key <= 26:  # Validate key range
        text = input('Enter the text to decrypt: ')
        plaintext = decrypt(text, key)
        print(f'PLAINTEXT: {plaintext}')
    else:
        print("Invalid entry! Please enter a key between 1 and 26.")
else:
    print("Invalid input! Please enter 'e' to encrypt or 'd' to decrypt.")
