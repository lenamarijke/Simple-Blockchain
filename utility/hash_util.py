import hashlib
# json ormat makes it easy to convert stuff to a string
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()

def hash_block(block):

    # convert block into a dictionary 
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hashlib.sha256(json.dumps(hashable_block, sort_keys=True).encode()).hexdigest()

