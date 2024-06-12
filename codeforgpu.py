'''code for the gpu database'''
import sqlite3
from colorama import Fore, Style, init

#initialize variables
userpass = 0

#Initialize colorma
init()

#Count lines in password file
with open('username and password.txt', 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1

#login code
def login():
    loginstate = False
    breakingpt = False
    with open('username and password.txt', 'r') as file:
        userpass = file.read()
        passtrials = 0  #how many tries they took to enter their password
        while True:
            print(Fore.WHITE + "Type 'exit' to exit the login interface")
            username = input(Fore.WHITE + "Please enter your username: ")
            if username == 'exit':
                break
            password = input("Please enter your password: ")
            sections = userpass.split(", ")
            for i in range(line_count):
                if sections[i * 4 + 1] == username and sections[i * 4 + 2] == password:
                    print(Fore.WHITE + 'Login successful!')
                    breakingpt = True
            if breakingpt == True:
                loginstate = True
                break
            if username == 'exit':
                break
            if passtrials == 3:
                print(Fore.RED + "You have inputted the wrong username or password too many times.")
                break
            if loginstate == False:
                print(Fore.RED + "Incorrect username or password. Please try again. To exit, enter 'exit' as the username.")
                passtrials += 1
            if passtrials != 0 and loginstate == False:
                print(Fore.RED + f"You have {3 - passtrials} trys left.")


def new_user(): #creating new user code
    user_id = line_count
    admin = False
    adminpass = "adminpower"
    new_username = input("Please enter your desired username:")
    if new_username == adminpass:
        new_username = input(Fore.GREEN + "You are now an admin of the database, please choose a new username!")
        admin = True
    new_password = input(Fore.LIGHTBLUE_EX + "Please enter your desired password:")
    with open('username and password.txt', 'w') as file:
        userpass = file.write(f"{user_id}, {new_username}, {new_password}, {admin}, ")



def getall():
    '''print all data in gpu table'''
    db = sqlite3.connect()
    cursor = db.cursor()
   
    #Lakers_Player
    sql= "SELECT * FROM Lakers_Player_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()



login()







