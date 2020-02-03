'''Provides verification helper methods'''

from utility.hash_util import hash_string_256, hash_block
from wallet import Wallet

class Verification:

    # proof of work for blockchain
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        return guess_hash[0:2] == '00'
        """check if blockchain blocks are valid"""

    @classmethod
    def verify_chain(self, blockchain):
        '''' enumerate will extract index and values of the element (here blockchain)'''
        for (index, block) in enumerate(blockchain):
            '''we just skip the genesis block'''
            if index == 0:
                continue
            ''' for any other block, we compare the previous hash with the hashed block of the current block'''
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        if check_funds:
            sender_balance = get_balance(transaction.sender)
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_transactions(self, open_transactions, get_balance):
        # check if all transactions are valid aka positive here
        return all([self.verify_transaction(tx, get_balance, False) for tx in open_transactions])
        # is_valid = True
        # for tx in open_transactions:
        #     if verify_transaction(tx):
        #         is_valid = True
        #     else:
        #         is_valid = False
        # return is_valid