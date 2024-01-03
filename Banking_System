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
    
    def change_password(self, old_password, new_password):
        if self.authenticate(old_password):
            self.password = new_password
            print("Password changed successfully!")
        else:
            print("Unable to change password: Incorrect old password.")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful!\nCurrent Balance: {self.balance}" ) 

    def display_details(self):
        print("\n")
        print("Personal Details of User")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Balance:", self.balance)

    def withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount 
            print(f"Withdrawal successful!\nCurrent Balance: {self.balance}")
        else:
            print("Cannot withdraw amount requested.")

def access_user(users):
    print("Enter your username and password for the account you would like to access: ")
    entered_username = input("Username: ")
    entered_password = input("Password: ")

    for user in users:
        if user.username == entered_username and user.authenticate(entered_password):
            return user
            
    print("Invalid username or password. Please try again.")
    return None 
    
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
    return user # returns the created use1r 


def main():
    print("\n*********************************")
    print("* WELCOME TO INST BANK DATABASE *")
    print("*********************************")

    users = [] # list to store User instances  

    while True:
        print("\nOptions")
        print("1. Create a New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Information")
        print("5. Change Password")
        print("6. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1': # creating an account 
            user = create_account()
            users.append(user)
        
        elif choice == '2': # deposit

            if users: 
                selected_user = access_user(users)
                if selected_user:
                     selected_user.deposit()
                else:
                    print("No matching account found.")
            else: 
                print("\n-----------------------------------------------------------------------")
                print("No accounts found. An account must be created first before depositing")
                print("-----------------------------------------------------------------------")

        elif choice == '3': # withdrawal
            if users:   
                selected_user = access_user(users)
                if selected_user:
                     selected_user.withdrawal()
                else:
                    print("No matching account found.")
            else:
                print("\n------------------------------------------------------------------------")
                print("No accounts found. An account must be created first before withdrawing")
                print("------------------------------------------------------------------------")

        elif choice == '4': # displaying bank information 
            if users:
                selected_user = access_user(users)
                if selected_user:
                    selected_user.display_details()
            else: 
                print("\n--------------------------------------------------------------------------------")
                print("No accounts found. An account must be created first before displaying an account")
                print("--------------------------------------------------------------------------------")

        elif choice == '5': # changing password 
            if users:
                selected_user = access_user(users)
                if selected_user:
                    old_password = input("Enter your old password: ")
                    new_password = input("Enter your new password: ")
                    selected_user.change_password(old_password, new_password)
                else:
                    print("No matching account found. Please try again.")
            else:
                print("\n--------------------------------------------------------------------------------")
                print("No accounts found. An account must be created first before changing your password")
                print("---------------------------------------------------------------------------------")

        elif choice == '6': # exiting program
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-5).") 

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
    
