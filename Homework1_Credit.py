 # Samuel Conteh Bank


class User():
    def __init__(self, username, password, name, age, gender, initial_balance = 0):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = initial_balance

    # I have heard that this is not foolproof. Some considerations to improve security are:
        # Hashed passwords, salted hashes, authentication libraries, password policies, 
    
    def authenticate(self, entered_password):
        return entered_password == self.password
    
    def deposit(self, amount):
        entered_password = input("Enter your password: ")
        if self.authenticate(entered_password):
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"Deposit successful!\nCurrent Balance: {self.balance}" )
        else: 
            print("Unable to deposit: Incorrect password.")

    def withdrawal(self, amount):
        entered_password = input("Enter your password: ")
        if self.authenticate(entered_password):
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount 
                print(f"Withdrawal successful!\nCurrent Balance: {self.balance}")
            else:
                print("Cannot withdraw amount requested.")
        else: 
            print("Unable to deposit: Incorrect password.")
        
    def display_details(self):
        print("Personal Details of User")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Balance:", self.balance)

def create_account():
    # Getting User Details
    print("Before we can create a bank account, you must first create a username and password associat1e with it.\n")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    user = User(username, password, name, age, gender) # creation of the instance of the user class  
    print("\nAccount Created!\n")
    user.display_details() # displaying the user information 
    return user # returns the created user 


def main():
    print("*********************************")
    print("* WELCOME TO INST BANK DATABASE *")
    print("*********************************")

    user = None  # Initialize user outside the loop

    while True:
        print("Options\n")
        print("1. Create a New Account\n")
        print("2. Deposit\n")
        print("3. Withdraw\n")
        print("4. Display Account Information\n")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1': 
            user = create_account()
        
        elif choice == '2': 
            if user: 
                 user.deposit()
            else: 
                print("\n--------------------------------------------------------------------------------------")
                print("\nNo accounts found. An account must be created first before depositing.")            
        elif choice == '3': 
            if user: 
                user.withdrawal()
            else:
                print("\n--------------------------------------------------------------------------------------")
                print("\nNo accounts found. An account must be created first before withdrawing.\n")

        elif choice == '4':
            if user:
                user.display_details()
            else: 
                print("\n--------------------------------------------------------------------------------------")
                print("No accounts found. An account must be created first before displaying an account.\n")

        elif choice == '5': 
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-5).") 

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
    