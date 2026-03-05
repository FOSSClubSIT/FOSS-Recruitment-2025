import time 
import json 
from mini_blockchain.blockchain import Blockchain
from mini_blockchain.utils import print_chain_prettily,is_chain_valid

def main():
    blockchain = Blockchain()
    try :
        blockchain.load_chain()
    except FileNotFoundError:
        print("no chain found creating a new one ...")
        blockchain.save_chain()
        print_chain_prettily(blockchain.chain)
        
    print("Mini Blockchain CLI")
    print("Type a command: add, show, validate, reset, exit/quit")
    while True:
        command = input("\n> ").strip().lower()
        if command.startswith("add"):
            parts = command.split(" ")
            if len(parts)<2:
                print("❌ please provide transactional data. Example: add Mr.Zoro payed 5 BTC")
                continue
            transaction = parts[1]
            blockchain.add_block([transaction])
            blockchain.save_chain()
            print(f"✅ Added block with transaction: {transaction}")

        elif command == "show":
            print_chain_prettily(blockchain.chain)
        
        elif command == "validate":
            if is_chain_valid(blockchain.chain):
                print(f"✅ Chain is valid!")
            else:
                print(f"❌ Chain is invalid!")
        elif command == "reset":
            blockchain = Blockchain()
            blockchain.save_chain()
            print("🔄 Blockchain has been reset with a new genesis block.")
            print("Your current chain is now: ")
            print_chain_prettily(blockchain.chain)
        
        elif command in ["exit","quit"]:
            print("👋 Exiting blockchain CLI...")
            print("Goodbye!")
            break
        else:
            print("❌ Unknown command. Valid commands: add, show, validate, reset, exit")
            

if __name__ == "__main__":
    main()