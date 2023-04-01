#Version 3: GUI version of Basic Password Manager

#import tkinter and create a window

from tkinter import*

root = Tk()
root.geometry("400x300")
root.title("Password Manager")

#create empty dictionaries to store {account:username} and {account:password}

passwords = {}
usernames = {}

pw_username = "abc.admin"
pw_password = "abc.pw-manager"

#declare "account" as global variable

global account
account = ""

#functions to get/add passwords in new window called root
def add_username(account, username):
    usernames[account] = str(username)

def add_password(account, password):
    passwords[account] = str(password)

def add_account(account, username, password):
    add_username(account.get(), username.get())
    add_password(account.get(), password.get())

def get_password(account):
    return passwords.get(account, None)

def get_username(account):
    return usernames.get(account, None)

def get_username_password(account):
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    if str(account) in passwords:
        t2.insert(END, str(get_username(account)))
        t3.insert(END, str(get_password(account)))
    else:
        t2.insert(END, "Account not found")
        t3.insert(END, "Account not found")

#checks sign in into password manager, if access granted, creates new window with program for adding/getting passwords
#main function that everything is happening in

def sign_in():
    #declare username, password, account, t2, and t3 as global variables
    global username, password, account, t2, t3
    if str(username_entry.get()) == str(pw_username) and str(password_entry.get()) == str(pw_password):
        t1.delete("1.0", END)
        t1.insert(END, "Access Granted!")
        
        #creating new window which is the actual password manager as the previous window was to log into this password manager
        
        root = Tk()
        root.geometry("500x400")
        root.title("Add/Get Passwords")
        
        acc_label = Label(root, text="Enter Account/Website Name: ")
        acc_label.grid(column=0, row=0)
        
        account = Entry(root)
        account.grid(column=1, row=0)
        
        user_label = Label(root, text="Username: ")
        user_label.grid(column=0, row=1)
        
        username = Entry(root)
        username.grid(column=1, row=1)
        
        pw_label = Label(root, text="Password: ")
        pw_label.grid(column=0, row=2)
        
        password = Entry(root)
        password.grid(column=1, row=2)         
        
        t2_label = Label(root, text="Username: ")
        t2_label.grid(column=0, row=7)
        
        t3_label = Label(root, text="Password: ")
        t3_label.grid(column=0, row=8)        
        
        t2 = Text(root, width=30, height=2)
        t2.grid(column=1, row=7)
        
        t3 = Text(root, width=30, height=2)
        t3.grid(column=1, row=8)        
        
        #buttons for adding/getting passwords
        
        add_button = Button(root, text="Add Account", command=lambda: add_account(account, username, password))        
        add_button.grid(column=1, row=5)
        
        get_button = Button(root, text="Get Password", command=lambda: get_username_password(account.get()))
        get_button.grid(column=1, row=6)         
        
        root.mainloop()        
        
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Access Denied! Try Again!")

info_label = Label(root, text = "Login to Password Manager")
info_label.grid(column = 1)

username_label = Label(root, text = "Username: ")
username_label.grid(column = 0, row = 1)

password_label = Label(root, text = "Password: ")
password_label.grid(column = 0, row = 2)

username_entry = Entry(root)
username_entry.grid(column = 1, row = 1)

password_entry = Entry(root)
password_entry.grid(column = 1, row = 2)

#login button that checks login into password manager by calling the sign in function

login_button = Button(root, text = "Login", command = sign_in)
login_button.grid(column = 1, row = 3)

t1 = Text(root, width = 30, height = 2)
t1.grid(column = 1, row = 4)


root.mainloop()
