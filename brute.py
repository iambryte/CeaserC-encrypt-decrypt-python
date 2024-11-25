def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            result += char
            
    return result

def main():
    print("Caesar Cipher Encoder/Decoder")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    if shift < 1 or shift > 25:
        print("Shift value must be between 1 and 25.")
        return
    
    if mode == 'encrypt':
        encrypted_text = caesar_cipher(text, shift, 'encrypt')
        print(f"Encrypted Text: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher(text, shift, 'decrypt')
        print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()