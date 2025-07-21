# Bank Account Assignment:
class BankAccount:
    def __init__(self, int_rate , balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self , amount):
        self.balance += amount
        return self
    
    def withdraw(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self , name = ""):
        print(f"{name} - Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Interest added: ${interest: .2f}")
        else:
            print("No interest added. Balance is non-positive")
        return self


# Class User:
class User:
    def __init__(self, name, int_rate = 0.01 , starting_balance = 0):
        self.name = name
        self.account = BankAccount(int_rate , starting_balance)
        print(f"Create Account, User Name: {self.name}, Account Balance: {self.account.balance}")
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"User Name: {self.name}, Make a deposit of {amount}")
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        print(f"User {self.name} made a Withdrawal of {amount}")
    
    def display_user_balance(self):
        self.account.display_account_info(self.name)

    def add_interest(self):
        self.account.yield_interest()

# Add Users:
guido = User("Guido van Rossum", int_rate = 0.02 , starting_balance = 250)
Jacob = User("Jacob Qumsiyeh", int_rate = 0.03 , starting_balance = 750)

# For The Guido User:
guido.make_deposit(100)
guido.make_deposit(63.9)
guido.make_deposit(14.2)
guido.make_withdrawal(120.5)
guido.display_user_balance()

# For Jacob The User:
Jacob.make_deposit(1500)
Jacob.make_deposit(550)
Jacob.make_withdrawal(1500)
Jacob.display_user_balance()