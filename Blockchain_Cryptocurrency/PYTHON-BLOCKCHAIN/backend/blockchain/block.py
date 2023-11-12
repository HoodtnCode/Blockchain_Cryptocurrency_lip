from operator import ge
import time
from backend.util.crypto_hash import crypto_hash


##Gloabal parameter. In all upper case = scream case

GENESIS_DATA = {
    'timestamp' : 1,
    'last_hash' : 'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : [],
    'difficulty' : 3,
    'nonce' : 'genesis_nonce'
    }

#block in the chain contians timestamp, lst_hash, data hash
class Block:
    """
    Block: a unit of storage.
    Store trnasactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    #return formated string of block class data
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'Block-data: {self.data},'
            f'difficulty : {self.difficluty},'
            f'nonce: {self.nonce})'
        )
    @staticmethod
    #last_block is used to find the last block hash, data is the data to be stored in the block
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data, until a block hash is found that meets the leading 0's proof of work requirement (). 
        """

        timestamp = time.time_ns()
        last_hash = last_block.hash
        #hash = f'{timestamp}-{last_hash}'#timporary until coding a true hash algorythm
        #true hash from crypto_hash
        difficulty = last_block.difficulty
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hash [0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)
    @staticmethod
    def genesis():
        """
        Generate genesis block.
        """
        #return Block(
        #    timestamp = GENESIS_DATA['timestamp'],
        #    last_hash = GENESIS_DATA['last_hash'],
        #    hash = GENESIS_DATA['hash'],
        #    data = GENESIS_DATA['data']
        #     1, 'genesis_last_hash', 'genesis_hash', []
        #    )
        #use of **GENESIS_DATA below will autmoatically add the new attributes to the genesis block data from the dictionaray see above
        return Block(**GENESIS_DATA)

###investigation code to check the code within the file
def main():
    #block = Block('foo')
    #print(block)
    #print (f'block.py__name__: {__name__}')


    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
