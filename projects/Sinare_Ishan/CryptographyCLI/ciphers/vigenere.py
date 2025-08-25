def encrypt(text:str, key:str):
    if not key:
        raise ValueError("Key cannot be empty")
    # Convert key to uppercase and remove non-alphabetic characters
    key = ''.join(char.upper() for char in key if char.isalpha())
    if not key:
        raise ValueError("Key must contain at least one alphabetic character")
    encrypted = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            # Preserve original case
            is_upper = char.isupper()
            char = char.upper()
            # Get the shift value from the current key character
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # Encrypt by shifting forwards
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Restore original case
            if not is_upper:
                encrypted_char = encrypted_char.lower()
            encrypted += encrypted_char
            key_index += 1  # Only advance key for alphabetic characters
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    print(f'\nthe encrypted text is :\n{encrypted}')

def decrypt(text:str, key:str):
    if not key:
        raise ValueError("Key cannot be empty")
    # Convert key to uppercase and remove non-alphabetic characters
    key = ''.join(char.upper() for char in key if char.isalpha())
    if not key:
        raise ValueError("Key must contain at least one alphabetic character")
    decrypted = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            # Preserve original case
            is_upper = char.isupper()
            char = char.upper()
            # Get the shift value from the current key character
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # Decrypt by shifting backwards
            decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # Restore original case
            if not is_upper:
                decoded_char = decoded_char.lower()
            decrypted += decoded_char
            key_index += 1  # Only advance key for alphabetic characters
        else:
            # Keep non-alphabetic characters unchanged
            decrypted += char
    print(f"\nThe decrypted text is : \n{decrypted}")
