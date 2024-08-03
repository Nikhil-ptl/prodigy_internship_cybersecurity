from PIL import Image
import numpy as np 

def encrypt(image_path, output_path, key):

    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)

    encrypted_pixels = (pixels + key) % 256

    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt(image_path, output_path, key):

    img = Image.open(image_path)
    img = img.convert('RGB')  
    pixels = np.array(img)

    decrypted_pixels = (pixels - key) % 256

    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        choice = input("Do you want to Encrypt-'E' or Decrypt-'D' an image? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
            continue
        
        image_path = input("Enter the path of the image file: ")
        output_path = input("Enter the path to save the output image file: ")
        try:
            key = int(input("Enter the encryption key (integer): "))
        except ValueError:
            print("Encryption key must be an integer. Please try again.")
            continue
        
        if choice == 'E':
            encrypt(image_path, output_path, key)
        else:
            decrypt(image_path, output_path, key)
        
        another = input("Do you want to process another image? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
