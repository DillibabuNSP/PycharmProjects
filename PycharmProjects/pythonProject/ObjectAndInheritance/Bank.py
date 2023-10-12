class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account name {self.owner} and balance {self.balance}'

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print(f'Amount Deposited and balance is {self.balance}')

    def with_draw(self, withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            print(f'Get your cash and balance is {self.balance}')

        else:
            print('Insufficient Fund')


if __name__ == "__main__":
    acc = Account('Jose', 100)
    acc.owner
    acc.balance
    acc.with_draw(75)
    acc.deposit(50)
