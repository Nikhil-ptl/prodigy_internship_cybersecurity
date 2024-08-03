def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_base = 65
            else:
                shift_base = 97
            
            original_position = ord(char) - shift_base
            new_position = (original_position + shift) % 26
            new_char = chr(new_position + shift_base)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_base = 65
            else:
                shift_base = 97
            
            original_position = ord(char) - shift_base
            new_position = (original_position - shift) % 26
            new_char = chr(new_position + shift_base)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to Encrypt-'E' or Decrypt-'D' a message? (E/D): ")
        choice = choice.upper()
        
        if choice != 'E' and choice != 'D':
            print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
            continue
        
        message = input("Enter your message: ")
        
        shift_input = input("Enter the shift value: ")
        try:
            shift = int(shift_input)
        except ValueError:
            print("Shift value must be an integer. Please try again.")
            continue
        
        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message: " + encrypted_message)
        else:
            decrypted_message = decrypt(message, shift)
            print("Decrypted message: " + decrypted_message)
        
        another = input("Do you want to process another message? (Y/N): ")
        another = another.upper()
        
        if another != 'Y':
            break

if __name__ == "__main__":
    main()

