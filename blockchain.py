from block import Block
import json

class Blockchain:

    chain = []

    def __init__(self):
        self.createFirstBlock()

    def createFirstBlock(self):
        first_block = Block(0, 0, "Test 1")
        self.chain.append(first_block)

    def addBlock(self, block):
        if self.verifyBlock(block):
            self.chain.append(block)

    def verifyBlock(self, block):
        for bl in self.chain:
            if bl.id == block.id:
                return False
        if block.hash[:4] != "0000":
            return False
        return True

    def getLastHash(self):
        return self.chain[-1]

    def getLastId(self):
        return len(self.chain)

    def jsonFile(self, block):
        json_file = open('block-information.json', "w")
        json.dump(block.informationBlock(), json_file, indent = 2)
