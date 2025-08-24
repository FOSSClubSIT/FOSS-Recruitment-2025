#CRYPTOGRAPHY
from ciphers import caesar
from ciphers import vigenere
from ciphers import aes
import argparse

def main():
    parser = argparse.ArgumentParser(
        description = "Text Encryption Toolkit CLI"
    )

    parser.add_argument("--cipher", choices=["C", "V", "A"], required=True,
                        help="Choose the cipher method (e.g., C for caesar, V for Vigenere, A for Advanced)")
    
    if args.cipher == "C":
        parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True,
                            help="Choose mode: encrypt or decrypt")
        parser.add_argument("--key", type=int, required=True,
                            help="Encryption/Decryption key (integer for Caesar)")
        parser.add_argument("--text", type=str, required=True,
                            help="Text to process")
        if args.mode == "encrypt":
            results = caesar.encrypt(args.text, args.key)
        if args.mode == "decrypt":
            results = caesar.decrypt(args.text, args.key)