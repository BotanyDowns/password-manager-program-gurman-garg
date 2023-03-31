#Version 2: Basic Password Manager w/ usernames saved

#creating an empty dictionary to store account name and password, and another empty dictionary to store account name and username
passwords = {}
usernames = {}

#using functions like adding passwords to account and asking to get password from dictionary and adding username to account and getting username from dictionary
def add_password(account, password):
    passwords[account] = password

def add_username(account, username):
    usernames[account] = username
    
def get_password(account):
    return passwords.get(account, None)

def get_username(account):
    return usernames.get(account, None)

def main():
    while True:
        print("")
        print("1. Add Username/Password")
        print("2. Get Username/Password")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            account = input("Enter account/website name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(account, password)
            add_username(account, username)
        elif choice == "2":
            account = input("Enter account/website name: ")
            username = get_username(account)
            password = get_password(account)
            if password:
                print(f"Username for {account}: {username}")
                print(f"Password for {account}: {password}")
            else:
                print(f"No password found for {account}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
## It allows you to execute code when the file runs as a script, but not when it's imported as a module




