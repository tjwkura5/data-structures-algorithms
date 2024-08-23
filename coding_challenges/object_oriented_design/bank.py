import string
import random
import json
import threading


from abc import ABC, abstractclassmethod
from enum import Enum

# Requirements

# Some possible questions to ask:

# What financial services will the bank offer?
# Will customers be required to have accounts? Will the bank manage them?
# Will the bank have physical locations and bank tellers?
# Are we concerned with physical security of the bank? i.e. will the bank have a vault?
# Services

# Customers can open accounts and deposit/withdraw money
# We are only concerned with transactions that take place within a physical location 
# (i.e. through a bank teller)
# Tellers

# Tellers can perform transactions on behalf of customers
# Every transaction is recorded and associated with the Teller and Customer
# Headquarters

# Each branch location will send money to a central location 
# (i.e. the bank's headquarters) at the end of the day
# We don't need to worry about the transporation details

class TransactionType(Enum):
    OPEN = 'Open Account',
    WITHDRAWAL = 'Withdrawal'
    DEPOSIT = 'Deposit'

class Transaction(ABC):
    def __init__(self, customerId, tellerId) -> None:
        self._customerId = customerId
        self._teller = tellerId
    
    def get_customer_id(self):
        return self._customerId
    
    def get_teller_id(self):
        return self._teller
    
    @abstractclassmethod
    def get_transaction_description(self):
        pass

class Deposit(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self._amount = amount
        self._transaction_type = TransactionType.DEPOSIT.value

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} deposited {self._amount} to account {self.get_customer_id()}'

class Withdrawal(Transaction):
    def __init__(self, customerId, tellerId, amount) :
        super().__init__(customerId, tellerId)
        self._amount = amount
        self._transaction_type = TransactionType.WITHDRAWAL.value

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} withdrew {self._amount} from account {self.get_customer_id()}'
    
class OpenAccount(Transaction):
    def __init__(self, customerId, tellerId):
        super().__init__(customerId, tellerId)
        self._transaction_type = TransactionType.OPEN.value

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} opened account {self.get_customer_id()}'
    
class BankTeller:
    def __init__(self) -> None:
        self._id = ''.join(random.choices(string.digits, k=16))

    def get_id(self):
        return self._id
    
class BankAccount:
    def __init__(self, customer_id, name, balance):
        self._id = ''.join(random.choices(string.digits, k=16))
        self._customer_name = name
        self._customerId = customer_id
        self._balance = balance 

    def set_balance(self, amount):
        self._balance += amount

    def get_account_id(self):
        return self._id
        
    def get_balance(self):
        return self._balance
        
    def get_customer_id(self):
        return self._customerId

class BankSystem:
    _instance_lock = threading.Lock()
    _unique_instance = None

    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super(BankSystem, cls).__new__(cls)
                cls._unique_instance._init_bank_system()

        return cls._unique_instance

    def _init_bank_system(self):
        self._accounts = {}
        self._transactions = []

    def _get_account_by_customer(self, customer_id) -> BankAccount:
        if customer_id in self._accounts.keys():
            return self._accounts[customer_id]
        else:
            raise ValueError('This account does not exist')
    
    def get_all_accounts(self):
        return self._accounts
    
    def get_transactions(self):
        return self._transactions
        
    def open_account(self, customer_name, teller_id, initial_balance = 0):
        customer_id = ''.join(random.choices(string.digits, k=12))
        account = BankAccount(customer_id, customer_name, initial_balance)
        self._accounts[customer_id] = account

        #Log Transaction
        transaction = OpenAccount(customer_id, teller_id)
        print(transaction.get_transaction_description())
        self._transactions.append(transaction)

        return customer_id


    def deposit(self, customer_id, teller_id, amount):
        account = self._get_account_by_customer(customer_id)
        account.set_balance(amount)

        #Log Transaction
        transaction = Deposit(customer_id, teller_id, amount)
        print(transaction.get_transaction_description())
        self._transactions.append(transaction)

    def withdraw(self, customer_id, teller_id, amount):
        account = self._get_account_by_customer(customer_id)
        if account.get_balance() > amount:
            account.set_balance(-amount)
        else:
            raise ValueError('The account has insufficient funds for this transaction')
        
        #Log Transaction
        transaction = Withdrawal(customer_id, teller_id, amount)
        print(transaction.get_transaction_description())
        self._transactions.append(transaction)



class BankBranch:
    def __init__(self, address, cash_on_hand, bank_system: BankSystem, num_tellers = 0):
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._system = bank_system
        self._tellers = []
        self._init_tellers(num_tellers)

    def add_teller(self, teller):
        self._tellers.append(teller)
    
    def _init_tellers(self, count):
        for _ in range(count):
            self.add_teller(BankTeller())

    def _get_available_teller(self):
        index = round(random.random() * (len(self._tellers) -1))
        teller = self._tellers[index]
        return teller.get_id()

    def open_account(self, customer_name, initial_balance = 0):
        if not self._tellers:
            raise ValueError('Branch does not have any available tellers')
        teller_id = self._get_available_teller()
        return self._system.open_account(customer_name, teller_id, initial_balance)

    def deposit(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any available tellers')
        if amount > self._cash_on_hand:
            raise ValueError('The branch does not have enough cash on hand to complete this transaction')
        teller_id = self._get_available_teller()
        self._system.deposit(customer_id, teller_id, amount)

    def withdrawal(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any available tellers')
        teller_id = self._get_available_teller()
        self._system.withdraw(customer_id, teller_id, amount)


myBankSystem = BankSystem()
myBankSystem2 = BankSystem()

myBank = BankBranch('123 Main St', 50000, myBankSystem, 5)

customerId1 = myBank.open_account('John Doe', 50)
customerId2 = myBank.open_account('Bob Smith', 100)
customerId3 = myBank.open_account('Jane Doe')

account = myBankSystem2._get_account_by_customer(customerId1)

print(account.get_balance())
myBank.deposit(customerId1, 100)
print(account.get_balance())
myBank.withdrawal(customerId1, 50)
print(account.get_balance())

