from datetime import datetime

class ATM:
    def __init__(self):
        self.pin = 12345
        self.balance = 0.0
        self.attempts = 2

    def welcome(self):
        print("\n********** WELCOME TO V25 ATM **********\n\n-------------------------------------\n")

    def display_date_time(self):
        current_time = datetime.now()
        print("Currunt Date and Time:", current_time)
        print("-------------------------------------\n")

    def login(self):
        while self.attempts > 0:
            entered_pin = int(input("Enter your PIN.(Only 2 attempts are allowed): "))    
            if entered_pin == self.pin:
                self.show_menu()
                return
            else:
                self.attempts -= 1
                if self.attempts > 0:
                    print("Invalid PIN !!!", self.attempts, "attempt left.")
                else:
                    print("Invalid PIN. No more attempts left. You can visit your nearest branch.")
                    return 

    def show_menu(self):
        choice = -1
        while choice != 0:
            print("\n************ ATM Main Menu Screen ************\n")
            print("Enter 1 to Check balance")
            print("Enter 2 to Cash Deposit")
            print("Enter 3 to Cash Withdrawal")
            print("Enter 4 to Reset PIN")
            print("Enter 5 to Exit/Cancel\n")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.cash_withdrawal()
            elif choice == 4:
                self.reset_pin()
            elif choice == 5:
                print("Thank you for using V25 ATM.")
                break
            else:
                print("Invalid choice. Please try again.") 

    def check_balance(self):    
        print("Your current balance is: $", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: $")) 
        if amount > 0:
            self.balance += amount
            print("Deposit Successfull. Current Balance is: $", self.balance)
        else:
            print("Invalid amount. Please try again.")       

    def cash_withdrawal(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > 0:
            if amount <= self.balance: 
                self.balance -= amount
                print("Withdrawal successful. Current Balance is: $", self.balance)
            else:
                print("Insufficient balance!! Please try again.")
        else:
            print("Invalid amount. Please try again.")

    def reset_pin(self):
        new_pin = int(input("Enter a new PIN(in Digits only): ")) 
        self.pin = new_pin
        print("PIN successfully reset.")

def main():
    atm = ATM()
    atm.welcome()
    atm.display_date_time()
    atm.login()
    
if __name__ == "__main__":
    main()    
