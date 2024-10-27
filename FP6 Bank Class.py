class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit successful. ${amount} has been added to your account.")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrawal successful. ${amount} has been withdrawn from your account.")
        else:
            print("\nInsufficient funds. Withdrawal canceled.")
    
    def check_balance(self):
        print(f"\nCurrent balance: ${self.balance}")

# Create instance of Bank class
account = Bank(123456, 0)

print("Welcome to the Python Banking System!")

# Verify account number before main loop
verified = False
while not verified:
    user_account = int(input("\nPlease enter your account number: "))
    
    if user_account == account.account_number:
        print("\nAccount verified! You may now proceed with transactions.")
        verified = True
    else:
        print("Invalid account number. Please try again.")

# Start main program loop
while True:
    # Display menu
    print("\nWhat would you like to do?")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        account.check_balance()
    
    elif choice == "2":
        amount = float(input("\nEnter amount to deposit: $"))
        if amount > 0:
            account.deposit(amount)
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
    elif choice == "3":
        amount = float(input("\nEnter amount to withdraw: $"))
        if amount > 0:
            account.withdraw(amount)
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
    elif choice == "4":
        print("\nThank you for using Python Banking System. Goodbye!")
        break
    
    else:
        print("\nInvalid choice. Please select 1-4.")