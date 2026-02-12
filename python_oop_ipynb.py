# -*- coding: utf-8 -*-


***OOP - object, class, abstraction, inheritence, encapsulation, polymorphism***
"""

class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            choice = input("""
Hello, how would you like to proceed?
1. Create PIN
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
""")
            if choice == '1':
                self.create_pin()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Thank you for Choosing us. Goodbye!")
                break
            else:
                print("Please select a valid option.")

    def create_pin(self):
        while True:
            try:
                pin = int(input("Set your 4-digit PIN: "))
                if 1000 <= pin <= 9999:
                    self.pin = pin
                    print("PIN set successfully!")
                    break
                else:
                    print("PIN must be 4 digits.")
            except ValueError:
                print("Please enter numbers only.")

    def validate_pin(self):
        try:
            temp = int(input("Enter your PIN: "))
            return temp == self.pin
        except ValueError:
            print("Invalid input. Enter numbers only.")
            return False

    def deposit_money(self):
        if self.validate_pin():
            try:
                amount = int(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print(f"Amount deposited successfully! Current balance: {self.balance}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Enter a valid number.")

    def withdraw_money(self):
        if self.validate_pin():
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawal successful! Remaining balance: {self.balance}")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Enter a valid number.")

    def check_balance(self):
        if self.validate_pin():
            print(f"Your account balance is: {self.balance}")

sbi = Atm()
