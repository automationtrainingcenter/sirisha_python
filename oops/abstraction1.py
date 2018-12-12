from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def update_address(self, address):
        pass

    def display_balance(self):
        print(self._balance)

    def __str__(self):
        return f'name={self.name}\naddress={self.address}'

class SavingsAccount(Account):

        def __init__(self, address, name):
            self._balance = 10000
            self.address = address
            self.name = name

        def deposit(self, amount):
            print('Transaction succesfully')
            if amount > 0:
                self._balance += amount
            else:
                print('invalid amount')

        def withdraw(self, amount):
            if amount > 0:
                if amount <= self._balance:
                    print('Transaction succesfull please collect your money')
                    self._balance -= amount
                else:
                    print('insuffcient balance')
            else:
                print('invalid amount')

        def update_address(self, address):
            self.address = address

class CurrentAccount(SavingsAccount):
    def __init__(self, address, name):
        self._balance = 25000
        self.address = address
        self.name = name

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance-25000:
                print('Transaction succesfull please collect your money')
                self._balance -= amount
            else:
                print('insuffcient balance')
        else:
            print('invalid amount')


class CreditCard(SavingsAccount):
    def __init__(self, address, name):
        self._balance = 50000
        self.address = address
        self.name = name

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                print('Transaction succesfull please collect your money')
                self._balance -= amount+50
            else:
                print('insuffcient balance')
        else:
            print('invalid amount')



account1 = SavingsAccount(['123', 'lingampally', 'hyderabad'], 'sirisha')
account1.display_balance()
print(account1)

account2 = CurrentAccount(['244', 'chanda nagar', 'hyderabad'], 'surya')
account2.deposit(10000)
account2.withdraw(5000)
account3 = CreditCard(['1245', 'kukat pally', 'hyderabad'], 'lakshmi')
account3.withdraw(5000)
account3.display_balance()
account3._balance = 30000
account3.display_balance()

print(account2)
print(account3)
