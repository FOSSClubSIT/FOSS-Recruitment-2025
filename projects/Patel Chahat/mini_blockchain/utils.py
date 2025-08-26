def print_chain_prettily(chain):
    for i, block in enumerate(chain):
        
        if isinstance(block, dict):
            index = block["index"]
            timestamp = block["timestamp"]
            transactions = block["transactions"]
            prev_hash = block["previous_hash"]
            hash_val = block["hash"]
        else:
            index = block.index
            timestamp = block.timestamp
            transactions = block.transactions
            prev_hash = block.previous_hash
            hash_val = block.hash

        print("+" + "-"*50 + "+")
        print(f"| Block {index:<43} |")
        print("+" + "-"*50 + "+")
        print(f"| Timestamp     : {timestamp:<25} |")
        print(f"| Transactions  : {transactions} |")
        print(f"| Previous Hash : {prev_hash[:15]}... |")
        print(f"| Hash          : {hash_val[:15]}... |")
        print("+" + "-"*50 + "+")

        if i < len(chain)-1:
            print("         |")
            print("         v")


def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        prev = chain[i-1]

        # Handle dict vs Block
        if isinstance(current, dict):
            current_hash = current["hash"]
            recomputed_hash = Block(
                current["index"],
                current["transactions"],
                current["timestamp"],
                current["previous_hash"],
                current.get("nonce", 0)
            ).compute_hash()
            prev_hash = prev["hash"]
            prev_hash_expected = current["previous_hash"]
        else:
            current_hash = current.hash
            recomputed_hash = current.compute_hash()
            prev_hash = prev.hash
            prev_hash_expected = current.previous_hash

        # recompute the hash of the current block
        if current_hash != recomputed_hash:
            print(f"❌ Invalid hash at block {i}")
            return False

        # check linkage
        if prev_hash_expected != prev_hash:
            print(f"❌ Invalid link between block {i-1} and {i}")
            return False

    print("✅ Blockchain is valid")
    return True
