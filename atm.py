class ATM:
    
        def __init__(self):
            self.balance = 10000
            self.card_number = input("Enter card number: ")
            try:
                self.pin_number = int(input("Enter pin number: "))
            except ValueError:
                print("Pin should contain only numbers!")
                exit()

        def show_details(self):
            print("\nAccount info")
            print("Card number: " + str(self.card_number))
            print("Balance: " + str(self.balance))
        
        def withdrawMoney(self, amount):
            try:
                if amount <= self.balance:
                    money_left = int(self.balance) - int(amount)
                    print("Money left: " + str(money_left))
                    self.balance = money_left
                else: 
                    print("Not enough money")
                    print("Balance: " + str(self.balance))
            except ValueError:
                print("Wrong Value! Try a number")
        
        def balanceEnquiry(self):
            print("Current balance: " + str(self.balance))

        def start(self):
            try:
                print("\nVerification...")
                pin = input("Enter pin: ")
                if int(pin) == int(self.pin_number): 
                    self.show_details()
                    print("\nWhat do you want to do(enter option number)? \n")
                    print("[1] Withdraw")
                    print("[2] Show balance")
                    print("[3] Exit\n")
                    wish = int(input(">> "))
                    if wish == 1:
                        amount = int(input("Enter the amount to withdraw: "))
                        self.withdrawMoney(amount)
                    elif wish == 2:
                        self.balanceEnquiry()
                    elif wish == 3:
                        exit()
                    else:
                        print("Bye!")
                else:
                    print("Wrong pin!")
            except ValueError:
                print("Wrong Value! Try a number")


my_atm = ATM()
my_atm.start()
