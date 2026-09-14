class BankAccount:

    # Constructor to initialize attributes
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)

    # Method to display details
    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# Taking input from user
acc_no = int(input("Enter account number: "))
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating BankAccount object
acc1 = BankAccount(acc_no, name, acc_type, balance)

# Display initial account details
acc1.display()

# Deposit money
deposit_amt = float(input("\nEnter amount to deposit: "))
acc1.deposit(deposit_amt)

# Withdraw money
withdraw_amt = float(input("Enter amount to withdraw: "))
acc1.withdraw(withdraw_amt)

# Display final account details
acc1.display()