class Blockchain(object):
    def __init__(self):
        # stores blockchains
        self.chain = []
        # stores transactions
        self.current_transactions = []

    def new_block(self):
        # This function creates new blocks and then adds to the existing chain
        pass

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
        pass

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        pass