
from backend.blockchain.block import Block


class Blockchain:
    """
    BockCchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain =[Block.genesis()]

    def add_block(self, data):
        #since last block in only called once it is inlaid in the self.chain[-1]
        self.chain.append(Block.mine_block(self.chain[-1],data))

    #wrapper method to overide default behavior to just print out method address.
    #official string representation of the Blockchain class
    def __repr__(self):
        return f'Blockchain: {self.chain}'





###Investigation code to check only this file
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')


    print(blockchain)
    print (f'blockchain.py__name__: {__name__}')

if __name__ == '__main__':
    main()