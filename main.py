from blockChainClasses.blockChain import Blockchain
from blockChainClasses.block import Block
import time

blockchain = Blockchain()
# Add blocks
blockchain.add_block(Block(1, time.time(), {"amount": 4}, blockchain.get_latest_block().hash))
blockchain.add_block(Block(2, time.time(), {"amount": 8}, blockchain.get_latest_block().hash))

# Check if the blockchain is valid
print("Is blockchain valid?", blockchain.is_chain_valid())

# Print the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 30)