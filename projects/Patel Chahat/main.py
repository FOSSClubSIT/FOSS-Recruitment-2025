import time
import argparse
from mini_blockchain.blockchain import Blockchain
from mini_blockchain.utils import print_chain_prettily,is_chain_valid

def main():
    parser = argparse.ArgumentParser(description="Mini Blockchain CLI")
    parser.add_argument("command",choices=["add","show","validate","reset"],help="command to run")
    parser.add_argument("data",nargs="*",help="Transaction data (for add command)")
    args = parser.parse_args()
    
    blockchain = Blockchain()

    try:
        
        blockchain.load_chain()
    except FileNotFoundError:
        print("No chain found, Creating a new one...")
        blockchain.save_chain()
    
    if args.command == "add":
        if not args.data:
            print("please provide transactional data")
            return
        transaction = " ".join(args.data)
        blockchain.save_chain()
        print(f"✅ Added block with transaction: {transaction}")

    elif args.command == "show":
        print_chain_prettily(blockchain.chain)

    elif args.command == "validate":
        print("✅ Chain is valid!" if is_chain_valid(blockchain.chain) else "❌ Chain is invalid!")

    elif args.command == "reset":
        blockchain = Blockchain()  # start fresh
        blockchain.save_chain()
        print("🔄 Blockchain reset with a new genesis block.")


if __name__ == "__main__":
    main()
