from PIL import Image
import numpy as np
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)

def encrypt_image(image_array, key):
    encrypted_image = np.copy(image_array)
    key_array = np.array(key)
    
    for i in range(encrypted_image.shape[0]):
        for j in range(encrypted_image.shape[1]):
            for k in range(encrypted_image.shape[2]):
                encrypted_image[i, j, k] ^= key_array[i % key_array.shape[0], j % key_array.shape[1], k]
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_image = np.copy(encrypted_image)
    key_array = np.array(key)
    
    for i in range(decrypted_image.shape[0]):
        for j in range(decrypted_image.shape[1]):
            for k in range(decrypted_image.shape[2]):
                decrypted_image[i, j, k] ^= key_array[i % key_array.shape[0], j % key_array.shape[1], k]
    
    return decrypted_image

def main():

    image_path = input("Enter the path to the input image: ")
    encrypted_path = input("Enter the path to save the encrypted image: ")
    decrypted_path = input("Enter the path to save the decrypted image: ")

    image_array = load_image(image_path)
    
    key = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)

    encrypted_image = encrypt_image(image_array, key)
    save_image(encrypted_image, encrypted_path)
    print(f"Image encrypted and saved to {encrypted_path}")

    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, decrypted_path)
    print(f"Image decrypted and saved to {decrypted_path}")

if __name__ == "__main__":
    main()
