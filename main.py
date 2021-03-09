import hashlib


# when creating a blockchain, create a genesis block first with prev_hash = None and add it to the blockchain
# then use build_block() for creating more blocks

class Block:
    prev_hash = None
    nonce = -1

    data = None

    current_hash = None

    def __init__(self, prev_hash, data):
        self.prev_hash = prev_hash
        self.data = data

    def __repr__(self):  # wie Objekt als String später dargestellt werden soll (represent)
        return "Block{0} (prev. {1})".format(
            self.current_hash,
            self.prev_hash
        )

    def block_string(self):
        return "{0}-{1}-{2}".format(
            self.prev_hash,
            self.data,
            self.nonce
        )

    def hash(self):
        return hashlib.sha256(bytes(self.block_string(), "utf-8")).hexdigest()

    def mine(self, difficulty):  # find a nonce where the hash has #difficulty zeros in the front of the hash
        found = False
        while not found:
            self.nonce += 1
            self.current_hash = self.hash()
            if self.current_hash[0:difficulty] == "0" * difficulty:
                found = True


class Blockchain:
    blocks = []
    difficulty = 4

    def add(self, block):
        block.mine(self.difficulty)
        self.blocks.append(block)

    @property
    def last_block(self):
        return self.blocks[-1] if len(self.blocks) else None

    def build_block(self, data):
        if self.last_block:
            block = Block(self.last_block.current_hash, data)
            self.add(block)
        else:
            raise Exception("Missing Genesis block")
