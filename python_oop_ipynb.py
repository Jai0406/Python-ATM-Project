class atm:

    def __init__(self):
        self.__balance = 0
        self.__Pin = None

    def menu(self):
        while True:
            choice = input("""
Hi, How can I help you today?
1. Create PIN
2. Change PIN
3. Deposit
4. Withdraw
5. Check Balance
6. Exit
""")

            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.change_pin()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.withdraw()
            elif choice == "5":
                self.check_balance()
            elif choice == "6":
                print("Thank you for choosing us. Goodbye!")
                break
            else:
                print("Invalid selection.")

    # ---------------- PIN METHODS ----------------

    def create_pin(self):
        while True:
            try:
                pin = int(input("Set your 4-digit PIN: "))
                if 1000 <= pin <= 9999:
                    self.__Pin = pin
                    print("PIN created successfully.")
                    break
                else:
                    print("PIN must be exactly 4 digits.")
            except ValueError:
                print("Numbers only.")

    def validate_pin(self):
        if self.__Pin is None:
            print("Please create PIN first.")
            return False

        for attempts in range(3, 0, -1):
            try:
                temp = int(input("Enter your PIN: "))
                if temp == self.__Pin:
                    return True
                else:
                    print(f"Incorrect PIN. Attempts left: {attempts-1}")
            except ValueError:
                print("Numbers only.")
        return False

    def change_pin(self):
        if not self.validate_pin():
            return

        while True:
            try:
                new_pin = int(input("Enter new 4-digit PIN: "))
                if 1000 <= new_pin <= 9999 and new_pin != self.__Pin:
                    self.__Pin = new_pin
                    print("PIN changed successfully.")
                    break
                else:
                    print("Invalid PIN or same as old PIN.")
            except ValueError:
                print("Numbers only.")

    # ---------------- TRANSACTIONS ----------------

    def deposit(self):
        if self.validate_pin():
            try:
                amount = int(input("Enter deposit amount: "))
                if amount > 0:
                    self.__balance += amount
                    print(f"Deposited! Current balance: {self.__balance}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount.")

    def withdraw(self):
        if self.validate_pin():
            try:
                amount = int(input("Enter withdrawal amount: "))
                if 0 < amount <= self.__balance:
                    self.__balance -= amount
                    print(f"Withdrawn! Remaining balance: {self.__balance}")
                else:
                    print("Invalid amount or insufficient funds.")
            except ValueError:
                print("Invalid amount.")

    def check_balance(self):
        if self.validate_pin():
            print(f"Your current balance is: {self.__balance}")
