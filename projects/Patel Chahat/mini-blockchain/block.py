import time 
import json
import hashlib


class Block:
    def __init__(self,index,transactions,timestamp,previous_hash,nonce = 0):
        """
        single block in the blockchain.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        """
        Generate the SHA256 hash of teh block's contents.
        """
        #  Convert block data to a string (dict -> Json string)
        block_data = {
            'index':self.index,
            'transactions':self.transactions,
            'timestamp':self.timestamp,
            'previous_hash':self.previous_hash,
            'nonce':self.nonce,
        }
        #  Ensure consistent ordering
        block_string = json.dumps(block_data,sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

if __name__ == "__main__":
    block = Block(0,['Mr. Chahat just payed 5 bitcoins'],time.time(),"0")
    print(f"block hash: {block.hash}")
    