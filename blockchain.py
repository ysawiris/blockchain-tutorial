from time import time
import hashlib
import json


class Blockchain(object):
    def __init__(self):
        # stores blockchains
        self.chain = []
        # stores transactions
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # This function creates new blocks and then adds to the existing chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        #Set the current transaction list to empty 
        self.current_transactions = []

        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        # This function adds a new transaction to already existing transactions
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1 

    @staticmethod    
    def hash(block):
        # Used for hashing a block
        # The follow code will create a SHA-256 block hash and also ensure that the dictionary is ordered
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
        

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        return self.chain[-1]