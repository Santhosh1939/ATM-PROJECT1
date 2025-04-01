
def display_menu():
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

def get_choice():
    return input("Enter your choice (1-4): ")

class ATM_program():
    def __init__(self,Bank_name,Location,balance):
        self.Bank_name = Bank_name
        self.Location = Location
        self.balance = balance
    def Credit(self):
        amount = float(input("Enter amount to credit: "))
        if amount <=0:
            print("Please enter positive amount")
        else:
            self.balance += amount
            print(f"Rs {amount} is credited to your account")

    def Debit(self):
        amount = float(input("Enter amount to debit: "))
        if amount <=0:
            print("Please enter positive amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Rs {amount} is debited from your account")

    def Balance(self):
        print(f"Your current avilable balance is: Rs {self.balance}")

    def Exit(self):
        print("Thank you for using the ATM")
        return True
    
print()
print(f"Welcome to Thomson bank,Atlanta GA")
print()
    
Bank = ATM_program("Thmoson  bank","Atlanta",600)
while True:
    display_menu()
    choice = get_choice()

    if choice == '1':
        Bank.Credit()
    elif choice == '2':
        Bank.Debit()
    elif choice == '3':
        Bank.Balance()
    elif choice == '4':
        Bank.Exit()
        break
    else:
        print("Invalid choice.Please try again")




        
