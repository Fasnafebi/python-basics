class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            print("Error: Balance cannot be negative!.")
            self.balance = 0
        else:
            self.balance = balance

    def get_balance(self):
        print(f"Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print(" Error: Deposit amount must be positive!")
        else:
            print(f"Depositing ₹{amount}")
            self.balance += amount
            print(f"New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Error: Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(" Error: Insufficient funds")
        else:
            print(f"Withdrawing ₹{amount}")
            self.balance -= amount
            print(f"New Balance: ₹{self.balance}")


print("Welcome to Python Bank!")
account = BankAccount("Alice", 5000)

account.get_balance()
account.deposit(1000)
account.withdraw(7000)
