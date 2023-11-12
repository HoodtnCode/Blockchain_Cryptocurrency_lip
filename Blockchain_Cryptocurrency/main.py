from dataclasses import dataclass


#generic hash that will just add a * to the data input into the method
def lighting_hash(data):
    return data + '*'


print ('hello blockchain')

#defined block class this is what will be in each block data, hash, and last hash
class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data 
        self.hash = hash
        self.last_hash = last_hash

#foo_block = Block('foo_data', 'foo_hash', 'foo_last_hash')

#create the chain start with the genesis block and then create method to add block to chain
class Blockchain:
    def __init__(self):
        genesis = Block('gen_data', 'gen_hash', 'gen_last_hash')

        self.chain = [genesis]
    #add block takes the new data, last hash, and a new hash value
    def add_block(self, data):
        #pulls the hash value from the last block in the chain
        last_hash = self.chain[-1].hash
        #create a new hash for the new block call the hash method and add the data and last_hash as inputs to the method
        hash = lighting_hash(data + last_hash)
        #create the block Block method, data from add_block, hash from add_block, and last_hash from add_block method
        block = Block(data, hash, last_hash)
        #append block to chain
        self.chain.append(block)


 #make blockchain instance= asssign variable and call Blockchain method. then can call sub-method to add block
foo_blockchain = Blockchain()
foo_blockchain.add_block('one')
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

 #test and iterate through printing out the blocks in the chain
for block in foo_blockchain.chain:
    #this will turn the three block attricture into a dictionary representation for print out (key value collection)
    print(block.__dict__)
