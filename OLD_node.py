from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet

class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)


    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        # this is a tuple
        return tx_recipient, tx_amount


    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
        # Output the blockchain list to the console with for loop
        for block in self.blockchain.chain:
            print('Outputting block')
            print(block)
        else:
            print('-' * 20)


    def listen_for_input(self):
        waiting_for_input = True

        # loop while
        while waiting_for_input:
            print('Please choose: ')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output blockchain')
            # print('4: Output participants')
            # print('5: Manipulate the chain')
            print('4: Create wallet')
            print('5: Load wallet')
            print('6: Check transaction validity')
            print('7: Save keys')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                # tuple unpacking since tx_data holds a tuple
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failed. Try creating a wallet')
            elif user_choice == '3':
                self.print_blockchain_elements()
            # elif user_choice == 4:
            #     print(participants)
            # elif user_choice == 5:
            #     if len(blockchain) >= 1:
            #         blockchain[0] = {
            #             'previous_hash': '',
            #             'index': 0,
            #             'transactions': [{'sender': 'Ole', 'recipient': 5, 'amount': 100}]
            #         }
            elif user_choice == '4':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '5':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            # check in any case if blockchain is valid or not
            if not Verification.verify_chain(self.blockchain.chain):
                print("Invalid blockchain")
                break
            # output formatted balance of owner with 6 digits and 2 decimal places
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print('User left!')


        print('Done!')

# to make sure that this is the main file & we are not importing this file from anywhere
if __name__ == '__main__':
    node = Node()
    node.listen_for_input()

