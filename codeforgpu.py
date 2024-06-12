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

#code to connect to database
def connectdatabase(sql, heading, spc1, spc2, spc3, spc4): #sql is what command in the sql interface you want to use             The spc# varables are to determine the spacing between the data
    db = sqlite3.connect("GPU.db") #connect to database
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(heading)
    for gpus in results:
        print(Fore.WHITE + f"{gpus[1]:<{spc1}}{gpus[2]:<{spc2}}{gpus[3]:<{spc3}}{gpus[4]:<{spc4}}")
    print("")
    db.close()
    


#login code
def login():
    loginstate = False
    breakingpt = False
    with open('username and password.txt', 'r') as file:
        userpass = file.read()
        passtrials = 0  #how many tries they took to enter their password
        while True:
            print(Fore.WHITE + "Type 'exit' to exit the login interface")
            username = input(Fore.WHITE + "Please enter your username: \n")
            if username == 'exit':
                break
            password = input("Please enter your password: \n")
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
    new_username = input("Please enter your desired username: \n")
    if new_username == adminpass:
        new_username = input(Fore.GREEN + "You are now an admin of the database, please choose a new username! \n")
        admin = True
    new_password = input(Fore.LIGHTBLUE_EX + "Please enter your desired password: \n")
    with open('username and password.txt', 'w') as file:
        userpass = file.write(f"{user_id}, {new_username}, {new_password}, {admin}, ")



def getallfromdatabase(): #GET EVERYTHING FROM THE DATABASE!
    connectdatabase("SELECT * FROM GPU;", Fore.GREEN + "Name                Manufacturer  Clock speed id  Memory id", 20, 14, 16, 14)
    connectdatabase("SELECT * FROM Memory;", Fore.GREEN + "Memory size  Memory bus", 13, 10, 0, 0)
    connectdatabase("SELECT * FROM clock_speed;", Fore.GREEN + "Base clock  Memory clock", 13, 10, 0, 0)
    print("It's a bit messy but YOU asked for everything at once.")






getallfromdatabase()












