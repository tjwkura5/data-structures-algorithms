import threading
import random
import string 
from abc import ABC, abstractclassmethod
from enum import Enum
# Imagine that you're writing software for a credit card provider. 
# Your task is to implement a program that will add new credit card accounts, 
# process charges and credits against them, and display summary information.

# You are given a list of commands:

# Add <card_holder> <card_number> $: Add command will create a new credit card 
# for the given card_holder, card_number, and limit. It is guaranteed that the 
# given card_holder didn't have a credit card before this operation.
# New cards start with a $0 balance.
# Cards numbers should be validated using basic validation.
# (Bonus) Card numbers should be validated using the Luhn 10 algorithm.
# Charge <card_holder> $: Charge command will increase the balance of the card associated 
# with the provided name by the amount specified.
# Charges that would raise the balance over the limit are ignored as if they were declined.
# Charges against invalid cards are ignored.
# Credit <card_holder> $: Credit command will decrease the balance of the card associated 
# with the provided name by the amount specified.
# Credits that would drop the balance below $0 will create a negative balance.
# Credits against invalid cards are ignored.
# Credit Card validation
# In order to ensure the credit card number is valid, we want to run some very basic validation.
# You need to ensure the string is only composed of digits [0-9] and is 
# between 12 and 16 characters long (although most cards are 15 to 16, let's keep it simple).
# Your Challenge

# Return the card holder names with the balance of the card associated with the provided name. 
# The names in output should be displayed in lexicographical order.
# Display "error" instead of the balance if the credit card number does not pass validation

class TransactionEnum(Enum):
    ADD = 0
    CHARGE = 1
    CREDIT = 2

class Transaction(ABC):
    def __init__(self, customer, account):
        self._id = ''.join(random.choices(string.digits, k=12))
        self._customer = customer
        self._account = account

    def get_id(self):
        return self._id
    
    def get_customer(self):
        return self.get_customer
    
    def get_account(self):
        return self.get_account
    
    @abstractclassmethod
    def get_transaction_description(self):
        pass 

class Add(Transaction):
    def __init__(self, customer, account, limit):
        super().__init__(customer, account)
        self._type = TransactionEnum.ADD
        self._limit = limit

    def get_limit(self):
        return self._limit

    def get_transaction_description(self):
        return f'Created new credit card {self.get_account()} for customer {self.get_customer()} with limit {self.get_limit()}'
    
class Charge(Transaction):
    def __init__(self, customer, account, charge):
        super().__init__(customer, account)
        self._type = TransactionEnum.CHARGE
        self._charge = charge 

    def get_charge(self):
        return self._charge

    def get_transaction_description(self):
        return f'A charge of {self.get_charge()} was posted to the account {self.get_account()} for customer {self.get_customer()}'
    

class Credit(Transaction):
    def __init__(self, customer, account, credit):
        super().__init__(customer, account)
        self._type = TransactionEnum.CREDIT
        self._credit = credit

    def get_credit(self):
        return self._credit

    def get_transaction_description(self):
        return f'A charge of {self.get_credit()} was posted to the account {self.get_account()} for customer {self.get_customer()}'

class CreditCard:
    def __init__(self, customer, limit, account_num):
        self._customer = customer
        self._limit = limit
        self._balance = 0
        self._account = account_num

    def get_customer(self):
        return self._customer
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account
    
    def set_balance(self, amount):
        self._balance += amount 
    
    def invalid_acct(self):
        self._balance = 'ERROR'


class CreditOperations:
    _instance_lock = threading.Lock()
    _unique_instance = None

    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super(CreditOperations, cls).__new__(cls)
                cls._unique_instance.__init__Operations

        return cls._unique_instance

    def __init__Operations(self):
        self._credit_cards = {}
        self._transactions = []
        self._customers = []

    @staticmethod
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10

    def _validate_account(self, account):
        if self.luhn_checksum(account) == 0:
            return True
        else:
            return False
    
    def get_card_customer(self, customer):
        return self._credit_cards[customer]

    def open_account(self, customer, card_number, limit):
        account = CreditCard(customer, limit, card_number)
        self._credit_cards[customer] = account
        self._customers.append(customer)
        if self._validate_account(card_number):
            #Log Transaction
            transaction = Add(customer, account.get_account_number(), limit)
            self._log_transaction(transaction)
        else:
            print(f'This card for customer {customer} is Invalid. Please check the card number {card_number}.')
            account.invalid_acct()

    def charge(self, customer, amount):
        account = self.get_card_customer(customer)
        balance = account.get_balance()
        if balance != 'ERROR' and balance + amount <= account.get_limit():
            account.set_balance(amount)

            #Log Transaction
            self._log_transaction(Charge(customer, account.get_account_number(), amount))
        else: 
            print(f'Unsuccessfully tried to charge {amount} to customer {customer}')

    def credit(self, customer, amount):
        account = self.get_card_customer(customer)
        balance = account.get_balance()

        if balance != 'ERROR':
            account.set_balance(-amount)
            self._log_transaction(Credit(customer, account.get_account_number(), amount))
        else:
            print(f'Unsuccessfully tried to credit {amount} to customer {customer}')

    def _log_transaction(self, transaction):
        self._transactions.append(transaction)
        print(transaction.get_transaction_description())

    def print_card_balances(self):
        for customer in self._customers.sort():
            account = self.get_card_customer(customer)
            print([customer, account.get_balance()])

  

print(CreditOperations.luhn_checksum('12345678901234'))

