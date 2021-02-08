from blockchain import Blockchain
from block import Block

blockchain = Blockchain()

block1 = Block(blockchain.getLastId(), blockchain.getLastHash(), "Test 2")
blockchain.addBlock(block1)

block2 = Block(blockchain.getLastId(), blockchain.getLastHash(), "Test 3")
blockchain.addBlock(block2)
