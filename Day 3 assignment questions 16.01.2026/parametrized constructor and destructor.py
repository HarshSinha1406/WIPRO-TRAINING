class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created:", self.account_number)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Updated Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient balance")

    def __del__(self):
        print("Account deleted:", self.account_number)


acc1 = BankAccount("BA101", 5000)

acc1.deposit(2000)
acc1.withdraw(3000)

del acc1
