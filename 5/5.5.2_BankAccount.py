class NegativeDepositError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError('Нельзя пополнить счет отрицательным значением')
        self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            raise InsufficientFundsError('Недостаточно средств для снятия')
        self.balance -= value