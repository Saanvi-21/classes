class ATM:
    
        def __init__(self):
            self.balance = 10000

        def show_details(self, card_number, pin_number):
            try:
                self.card_number = card_number
                self.pin_number = pin_number
                print("Card number: " + self.card_number)
                print("Balance: " + str(self.balance))
            except ValueError:
                print("Invalid Value! Try a number")
        
        def withdrawMoney(self, amount):
            try:
                if amount <= self.balance:
                    money_left = int(self.balance) - int(amount)
                    print("Money left: " + str(money_left))
                    self.balance = money_left
                else: 
                    print("Not enough money")
                    print("Balance: " + self.balance)
            except ValueError:
                print("Wrong Value! Try a number")
        
        def balanceEnquiry(self):
            print("Current balance: " + str(self.balance))

        def start(self):
            try:
                card_number = input("Enter card number: ")
                pin = input("Enter pin: ")
                if int(pin) == 1111: 
                    self.show_details(card_number, pin)
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

# Pin is 1111
my_atm = ATM()
my_atm.start()