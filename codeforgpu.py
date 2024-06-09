'''code for the gpu database'''
import sqlite3
from colorama import Fore, Style, init

#initialize variables

#Define user name and password saparate by user and admin
users = {
"Eric":{'password':'123456'},
}

#Initialize colorma
init()

#login code
def login():
    passtrials = 0  #how many tries they took to enter their password
    while True:
        print("Type 'exit' to exit the login interface")
        user = input(Fore.WHITE + "Please enter your username: ")
        if user == 'exit':
            break
        password = input("Please enter your password: ")
        if passtrials != 0:
            print(Fore.RED + f"You have {3 - passtrials} trys left.")
        if user and user in users and password == users[user]['password']:
            print('Login successful!')
            return 0
        if user == 'exit':
            break
        if passtrials == 3:
            print("You have inputted the wrong username or password too many times.")
            break
        else:
            print(Fore.RED + "Incorrect username or password. Please try again. To exit, enter 'exit' as the username.")
            passtrials += 1


def new_user():
    print("hi")




login()







