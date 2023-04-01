#Version 4: GUI version of Basic Password Manager with dictionary printed and an image

#import tkinter and images from PIL, and create window

from tkinter import*
from PIL import ImageTk, Image 


root = Tk()
root.geometry("400x300")
root.title("Password Manager Login")

#create empty account dictionary
accounts = {}

#set username and password to log into password manager

pw_username = "abc.admin"
pw_password = "abc.pw-manager"

#declare account as global variable so it can be used everywhere and not just in one function

global account
account = ""

#functions to get/add passwords in new window called root
def add_uspw(account, username, password):
    accounts[account] = (username, password)

def add_account(account, username, password):
    add_uspw(account.get(), username.get(), password.get())

def get_account(account):
    return accounts.get(account, None)

def get_username_password(account):
    t2.delete("1.0", END)
    if str(account) in accounts:
        t2.insert(END, str(get_account(account)))
    else:
        t2.insert(END, "Account not found")

def print_all():
    print(accounts)

#checks sign in into password manager, if access granted, creates new window with program for adding/getting passwords
#main function that everything is happening in

def sign_in():
    #declare these variables as global so they can be used outside this function
    global username, password, account, t2
    if str(username_entry.get()) == str(pw_username) and str(password_entry.get()) == str(pw_password):
        t1.delete("1.0", END)
        t1.insert(END, "Access Granted!")
        
        #create new window
        
        root = Tk()
        root.geometry("500x400")
        root.title("Account Passwords")
        
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
        
        t2_label = Label(root, text="'Account', 'Password': ")
        t2_label.grid(column=0, row=7)
        
        t2 = Text(root, width=30, height=2)
        t2.grid(column=1, row=7)       
        
        #buttons for saving accounts, getting passwords, and printing all passwords
        
        add_button = Button(root, text="Add Account", command=lambda: add_account(account, username, password))        
        add_button.grid(column=1, row=5)
        
        get_button = Button(root, text="Get Password", command=lambda: get_username_password(account.get()))
        get_button.grid(column=1, row=6)     
        
        print_button = Button(root, text = "Print All Passwords", command = print_all)
        print_button.grid(column = 1, row = 8)
        
        root.mainloop()        
    
    #if login is unsuccessful, shows access denied and new window does not appear    
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Access Denied! Try Again!")

#add profile image
profile_img = ImageTk.PhotoImage(Image.open("Images/profile4.png"))
img_label = Label(root, image=profile_img)
img_label.grid(column = 2, row = 1)

info_label = Label(root, text = "Login to Password Manager")
info_label.grid(column = 1, row = 0)

username_label = Label(root, text = "Username: ")
username_label.grid(column = 0, row = 1)

password_label = Label(root, text = "Password: ")
password_label.grid(column = 0, row = 2)

username_entry = Entry(root)
username_entry.grid(column = 1, row = 1)

password_entry = Entry(root, show = "*") #entrybox entry shows as asterisks
password_entry.grid(column = 1, row = 2)

login_button = Button(root, text = "Login", command = sign_in) #button that calls sign_in function
login_button.grid(column = 1, row = 3)

t1 = Text(root, width = 30, height = 2)
t1.grid(column = 1, row = 4)

root.mainloop()