import time
import json
from block import Block

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0,['GENESIS BLOCK'],time.time,"0")
        self.chain.append(genesis_block)
    
    def add_block(self,transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain),transactions,time.time(),previous_block.hash)
        self.chain.append(new_block)
    

    def save_chain(self,file_name = "chain.json"):
        chain_data = [block.__dict__ for block in self.chain]
        with open(file_name, "w") as f:
            json.dump(chain_data,f,indent=4)

    
