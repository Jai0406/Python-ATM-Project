class ATM:

    def __init__(self):
        self.balance = 0
        self.Pin = None

    def menu(self):
        while True:
            User_input = input("""
Hi, How can I help you today?
1. Press 1 to Create PIN
2. Press 2 to Deposit
3. Press 3 to Withdraw money
4. Press 4 to check Balance
5. Press 5 to exit
""")

            if User_input == "1":
                self.create_pin()
            elif User_input == "2":
                self.deposit()
            elif User_input == "3":
                self.withdraw()
            elif User_input == "4":
                self.check_balance()
            elif User_input == "5":
                print("Thank you for Choosing us. Goodbye !")
                break
            else:
                print("Invalid Entry Please select from above")

    def create_pin(self):
        while True:
            try:
                Pin = int(input("**** Set your 4 digit PIN **** "))
                if 1000 <= Pin <= 9999:
                    self.Pin = Pin
                    print("Pin Created Successfully")
                    break
                else:
                    print("Kindly set the PIN in 4 digits")
            except ValueError:
                print("Only Numerics allowed")

    def validate_pin(self):
      if self.Pin is None:
          print("Please create PIN first.")
          return False

      attempts = 3
      while attempts > 0:
          try:
              temp = int(input("Enter your PIN: "))

              if temp == self.Pin:
                  return True
              else:
                  attempts -= 1
                  print(f"Incorrect PIN  Attempts left: {attempts}")

          except ValueError:
              print("Invalid Input, Enter numbers only")

      print("Too many incorrect attempts. Returning to main menu.")
      return False

    def deposit(self):
      if self.validate_pin():
        try:
          amount = int(input("Please enter the amount"))
          if amount > 0:
            self.balance += amount
            print(f"Amount deposited sucessfully ! Current balance --> {self.balance}")
          else:
            print("Amount must be positive")
        except ValueError:
          print("Enter a valid number.")

    def withdraw(self):
      if self.validate_pin():
        try:
          amount = int(input("Enter the amount to be withdrawn --> "))
          if amount <= self.balance:
            self.balance -= amount
            print(f"Amount of {amount} deducted remaining balance {self.balance}")
          else:
            print("Insufficient Funds !!")
        except ValueError:
          print("Enter a Valid number")

    def check_balance(self):
      if self.validate_pin():
        print(f"Your account balance is {self.balance}")
