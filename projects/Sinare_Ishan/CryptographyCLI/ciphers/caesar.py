#CAESAR CIPHER
def encrypt(text:str , key:int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert to lowercase for processing
            char = char.lower()
            # Shift the character by the key value
            shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            # Restore original case
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    print(f'\nThe encrypted text is : \n{encrypted_text}')
   
def decrypt(text:str, key:int):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Preserve original case
            is_upper = char.isupper()
            char = char.lower()
            # Shift backwards by key positions
            decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    print(f'\nThe decrypted text is : \n{decrypted_text}')
