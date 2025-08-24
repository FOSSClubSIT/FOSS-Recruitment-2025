#CRYPTOGRAPHY
# from ciphers import caesar
# from ciphers import vigenere
# from ciphers import aes
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('cipher', help = 'Pick the cipher you wish to use', type=str)

args: Namespace = parser.parse_args()

print(args.echo)