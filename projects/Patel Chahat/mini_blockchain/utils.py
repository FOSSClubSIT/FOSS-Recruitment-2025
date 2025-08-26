import json
from block import Block

def print_chain_prettily(chain):                        #function to print the give chain in pretty redeable form.

    chain_data = [block.__dict__ for block in chain]
    print(json.dump(chain_data,indent=4))

def is_chain_valid(chain):                            #Function for checking wether the chain is valid or not 
    chain_data = [block.__dict__ for block in chain]
    for i in range(1,len(chain_data)):
        current = chain_data[i]
        prev = chain_data[i-1]

        if current.hash != Block.compute_hash(prev.hash):
            print("the chain is invalid")
            return False
        
        if current.previous_hash != prev.hash:
            return False
        
    return True

