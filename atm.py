class ATM:
    
        def __init__(self, card_number, pin_number):
            self.balance = 10000
            self.card_number = card_number
            self.pin_number = pin_number

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


# Enter any pin and any card number, remember the pin and enter the pin when prompted.
my_atm = ATM(card_number=922200001111, pin_number=1111)
my_atm.start()
