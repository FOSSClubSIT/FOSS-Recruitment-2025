#CRYPTOGRAPHY
from argparse import ArgumentParser, Namespace
from ciphers import caesar, vigenere, aes
parser = ArgumentParser()
parser.add_argument('-v', '--verbose', help='Provides a verbose description', action='store_true')
parser.add_argument('cipher', help="Pick a cipher", type=str, choices=['Caesar', 'Vigenere', 'AES'],default='Caesar')
parser.add_argument('action', help="Encrypt/Decrypt", type=str, choices=['encrypt', 'decrypt'], default='encrypt')
args = parser.parse_args()

#if args.verbose:
if args.cipher == 'Caesar':
    key1 = int(input('ENTER INTEGER VALUE FOR KEY : '))

    if args.action == 'decrypt':
        text1 = input("\nEnter the text you want decrypted : \n")
        caesar.decrypt(text1,key1)
    elif args.action == 'encrypt':
        text1 = input("\nEnter the text you want encrypted : \n")
        caesar.encrypt(text1,key1)

if args.cipher == 'Vigenere':
    print("Initiating Viginere cipher")
    if args.action == 'decrypt':
        print("Initiating decryption sequence")
    elif args.action == 'encrypt':
        print("Initiating encryption sequence")

if args.cipher == 'AES':
    print("Initiating Advanced Encryption System cipher")
    if args.action == 'decrypt':
        print("Initiating decryption sequence")
    elif args.action == 'encrypt':
        print("Initiating encryption sequence")