import time
from mini_blockchain.blockchain import Blockchain

def main():
    blockchain = Blockchain()

    #saample blocks
    blockchain.add_block(["Alice pays Bob 5 BTC"])
    time.sleep(1)
    
    blockchain.add_block(["Bob pays Charlie 2 BTC"])
    time.sleep(1)
    
    blockchain.add_block(["Charlie pays Dave 1 BTC"])

    

    blockchain.save_chain()

    

if __name__ == "__main__":
    main()
