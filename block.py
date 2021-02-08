import hashlib
from datetime import datetime


class Block:

    def __init__(self, id, previousHash, data):
        self.id = id
        self.time = datetime.utcnow().timestamp()
        self.previousHash = previousHash
        self.data = data
        self.nonce = 0
        self.hash = self.generateHash()

    def generateHash(self):
        hash_data = ""
        while hash_data[:4] != "0000":
            data = "{}:{}:{}:{}:{}".format(self.id, self.time, self.data, self.previousHash, self.nonce)
            hash_data = hashlib.sha256(data.encode("UTF-8")).hexdigest()
            self.nonce += 1
        return hash_data

    def informationBlock(self):
        information = {
            "Id": self.id,
            "Time": self.time,
            "Data": self.data,
            "Hash": self.hash
            }
        return information

