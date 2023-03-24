import flask, datetime, json, hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True 
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] == self.hash(previous_block): 
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest() # Fix: Parentheses are misplaced
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

app = flask.Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'congrats, you are now a miner!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block["previous_hash"]} 
    return json.dumps(response), 200

import datetime   # importing the datetime module for current date and time
import hashlib    # importing the hashlib module to perform hashing functions
import json       # importing the json module to work with JSON data
from flask import Flask, jsonify  # importing flask and its features

class Blockchain:    # Defines the Blockchain class
    def __init__(self):
        self.chain = []    # Initializes an empty list for chain
        self.create_block(proof=1, previuos_hash="0")    # Creates a Genesis Block with proof equal to 1 and hash "0"

    def create_block(self, proof, previuos_hash):   
        block + {'index': len(self.chain) + 1,    # Creates a new block with index (length of chain + 1)
                  'timestamp': str(datetime.datetime.now()),    # Timestamp for block creation
                  'proof': proof,    # A cryptographic proof related to mining (mentioned later in code)
                  'previuos_hash': previuos_hash}   # Hash of the previous block
        self.chain.append(block)    # Appends the block in the blockchain
        return block    # Returns the created block

    def get_previuos_block(self):    # Gets the previous block in the chain
        return self.chain(-1)   

    def proof_of_work(self, previuos_proof):   # Function to define a proof-of-work algorithm
        new_proof = 1    # Initialize nonce to 1 initially
        check_proof = False   # Boolean variable to track if found the correct proof or not
        while check_proof is False:    # Loops till check_proof is true
            hash_operation = hashlib.sha256(
                str(new_proof ** 2 - previuos_proof**2).encode()).hexdigest()   # Hashes the result and generates a hexadecimal output
            if hash_operation[:4] == '0000':   # Check the discovered proof against defined constraints, here it starts with 4 zeroes.
                check_proof = True   # If matched set the flag to true
            else:
                new_proof +=1   # try with next such that hash becomes valid
        return new_proof

    def hash(self, block):    # Function to generate the hash for given block
        encoded_block = json.dumps(block, sort_keys=True).encode()   # Converts the block data to JSON and encodes it using utf-8 encoding
        return hashlib.sha256(encoded_block).hexdigest()     # returns the generated SHA256 hash of the block

    def chain_valid(self, chain):   # function to validate a whole blockchain
        previuos_block = chain[0]   # set first block to previous block variable
        block_index = 1            # start from second block
        while block_index < len(chain):   # loop all blocks in chain
            block = chain[block_index]
            if block['previuos_hash'] != self.hash(previuos_block):  # validate the hashes
                return False
            previuos_proof = previuos_block ['proof']
            proof = block [proof]
            hash_operation = hashlib.sha256(str(proof ** 2 - previuos_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previuos_block = block    # if validation passes set prev one as current
            block_index += 1
        return True

app = Flask(__name__)    # Instance of flask app created with unique name

@app.route('/mine_block', methods=['GET'])    # A function to mine a block on request by user through GET method
def mine_block():
    previuos_block = blockchain.get_previuos_block() # Get the last block in chain
    previuos_proof = previuos_block['proof']
    proof = blockchain.proof_of_work(previuos_proof)
    previuos_hash = blockchain.hash(previuos_block)    # operate on last block to compare hash of previous block

    block = blockchain.create_block(proof, previuos_hash)  # create the new block with data about transactions or as here just for demo

    response = {'message': 'Congrats, you are now a miner!',    # Response in JSON format with details of the recently mined block
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previos_hash': block['previos_hash']}
    
    return jsonify(response), 200   # Returns response message in JSON format with status code as 200 (indicating success)
    