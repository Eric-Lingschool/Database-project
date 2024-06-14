'''code for the gpu database'''
import sqlite3
from colorama import Fore, Style, init

#initialize variables


#Initialize colorma
init()

#Count lines in password file
with open('username and password.txt', 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1
file.close()

#code to connect to database
def connectdatabase(sql1, heading, spc1, spc2, spc3, spc4): #sql is what command in the sql interface you want to use     The spc# varables are to determine the spacing between the data
    db = sqlite3.connect("GPU.db") #connect to database
    cursor = db.cursor()
    cursor.execute(sql1)
    results = cursor.fetchall()
    print(heading)
    for gpus in results:
        print(Fore.WHITE + f"{gpus[1]:<{spc1}}{gpus[2]:<{spc2}}{gpus[3]:<{spc3}}{gpus[4]:<{spc4}}")
    print("")
    


def new_user(): #creating new user code
    with open('username and password.txt', 'r') as file:
        userpass = file.read()
        recuruser = 0
        repeat = False
        sectiondvd = 0
        user_id = line_count + 1
        admin = False
        adminpass = "adminpower"
        new_username = input(Fore.LIGHTBLUE_EX + "Please enter your desired username: \n")
        while new_username.lower() == "c":
            print(Fore.RED + "This username already exists, please choose another one.")
            new_username = input(Fore.LIGHTBLUE_EX + "Please enter your desired username: \n")
        sections = userpass.split(", ")
        while repeat == True or sectiondvd == 0:
            sectiondvd = 1
            for i in range(line_count):
                recuruser = sections[i * 4 + 1]
                while new_username == recuruser:
                    print(Fore.RED + "This username already exists, please choose another one.")
                    new_username = input(Fore.LIGHTBLUE_EX + "Please enter your desired username: \n")
                    repeat = True
                repeat = False
        if new_username == adminpass:
            new_username = input(Fore.GREEN + "You are now an admin of the database, please choose a new username! \n")
            admin = True
        new_password = input(Fore.LIGHTBLUE_EX + "Please enter your desired password: \n")
        with open('username and password.txt', 'a') as file:
            userpass = file.write(f"\n{user_id}, {new_username}, {new_password}, {admin}, ")
            file.close()




#login code
def login():
    global loginstate
    loginstate = False
    breakingpt = False
    with open('username and password.txt', 'r') as file:
        userpass = file.read()
        passtrials = 0  #how many tries they took to enter their password
    while loginstate == False:
        print(Fore.WHITE + "Type 'exit' to exit the login interface")
        if passtrials == 0:
            print(Fore.GREEN + "If you don't have an existing account and want to create a new one, type 'c'.")
        username = input(Fore.WHITE + "Please enter your username: \n")
        if username.lower() == "c":
            new_user()
            print(Fore.RED + "Please start the program again, your username and password is being saved. (If you dont, it might not register your new account.)")
        if username == 'exit':
            break
        password = input(Fore.WHITE + "Please enter your password: \n")
        sections = userpass.split(", ")
        for trys in range(line_count):
            if sections[trys * 4 + 1] == username and sections[trys * 4 + 2] == password:
                print(Fore.GREEN + 'Login successful!')
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
    file.close()






def askingquestions():
    print(Fore.WHITE + "Welcome to 'totally not inaccurate or unessesary database'. Choose what you want to do before you go on with your day.\n")
    print(f"{Fore.WHITE}Type {Fore.GREEN}1{Fore.WHITE} to access EVERYTHING at the same time.")
    print(f"{Fore.WHITE}Type {Fore.GREEN}2{Fore.WHITE} to access the 'gpu' table.")
    print(f"{Fore.WHITE}Type {Fore.GREEN}3{Fore.WHITE} to access the 'Memory' table.")
    print(f"{Fore.WHITE}Type {Fore.GREEN}4{Fore.WHITE} to access the 'clock speed' table.")
    print(f"{Fore.WHITE}Type {Fore.GREEN}5{Fore.WHITE} to exit the program.\n")
    global access
    access = input()



#Main code
login()
loginstate = True
while loginstate == True:
    askingquestions()
    if access == "1":
        connectdatabase("SELECT * FROM GPU;", Fore.GREEN + "Name                Manufacturer  Clock speed id  Memory id", 20, 14, 16, 14)
        connectdatabase("SELECT * FROM Memory;", Fore.GREEN + "Memory size  Memory bus", 13, 10, 0, 0)
        connectdatabase("SELECT * FROM clock_speed;", Fore.GREEN + "Base clock  Memory clock", 13, 10, 0, 0)
        print(Fore.RED + "It's a bit messy but YOU asked for everything at once.")
    elif access == "2":
        connectdatabase("SELECT * FROM GPU;", Fore.GREEN + "Name                Manufacturer  Clock speed id  Memory id", 20, 14, 16, 14)
    elif access == "3":
        print(f"{Fore.WHITE}If you want it to be in ascending order for Memory size, type {Fore.GREEN}1.")
        print(f"{Fore.WHITE}If you want it to be in ascending order for Memory bus, type {Fore.GREEN}2.")
        print(f"{Fore.WHITE}If you want it to be in descending order for Memory size, type {Fore.GREEN}3.")
        print(f"{Fore.WHITE}If you want it to be in descending order for Memory bus, type {Fore.GREEN}4.")
        print(f"{Fore.WHITE}If you want it to be natural like some brand of yogurt(origional order), type {Fore.GREEN}5.")
        memory = input(Fore.WHITE)
        if memory == "1":
            connectdatabase("SELECT * FROM Memory ORDER BY memory_size ASC;", Fore.GREEN + "Memory Size(GB)     Memory Bus(bit)", 20, 14, 16, 14)
        elif memory == "2":
            connectdatabase("SELECT * FROM Memory ORDER BY memory_bus ASC;", Fore.GREEN + "Memory Bus(bit)     Memory Size(GB)", 20, 14, 16, 14)
        elif memory == "3":
            connectdatabase("SELECT * FROM Memory ORDER BY memory_size DESC;", Fore.GREEN + "Memory Size(GB)     Memory Bus(bit)", 20, 14, 16, 14)
        elif memory == "4":
            connectdatabase("SELECT * FROM Memory ORDER BY memory_bus DESC;", Fore.GREEN + "Memory Bus(bit)     Memory Size(GB)", 20, 14, 16, 14)
        elif memory == "5":
            connectdatabase("SELECT * FROM Memory", Fore.GREEN + "Memory Size(GB)     Memory Bus(bit)", 20, 14, 16, 14)
        else:
            print(Fore.RED + "That is not an option!")
    elif access == "4":
        print(f"{Fore.WHITE}If you want it to be in ascending order for Base clock, type {Fore.GREEN}1.")
        print(f"{Fore.WHITE}If you want it to be in ascending order for Memory clock, type {Fore.GREEN}2.")
        print(f"{Fore.WHITE}If you want it to be in descending order for Base clock, type {Fore.GREEN}3.")
        print(f"{Fore.WHITE}If you want it to be in descending order for Memory clock, type {Fore.GREEN}4.")
        print(f"{Fore.WHITE}If you want it to be natural like some brand of yogurt(origional order), type {Fore.GREEN}5.")
        clockspeed = input(Fore.WHITE)
        if clockspeed == "1":
            connectdatabase("SELECT * FROM clock_speed ORDER BY base_clock ASC;", Fore.GREEN + "Base clock(MHz)     Memory clock(MHz)", 20, 14, 16, 14)
        elif clockspeed == "2":
            connectdatabase("SELECT * FROM clock_speed ORDER BY memory_clock ASC;", Fore.GREEN + "Memory clock(MHz)   Base clock(MHz)", 20, 14, 16, 14)
        elif clockspeed == "3":
            connectdatabase("SELECT * FROM clock_speed ORDER BY base_clock DESC;", Fore.GREEN + "Base clock(MHz)     Memory clock(HMz)", 20, 14, 16, 14)
        elif clockspeed == "4":
            connectdatabase("SELECT * FROM clock_speed ORDER BY memory_clock DESC;", Fore.GREEN + "Memory Bus(HMz)   Base clock(HMz)", 20, 14, 16, 14)
        elif clockspeed == "5":
            connectdatabase("SELECT * FROM clock_speed", Fore.GREEN + "Memory clock(HMz)    Memory size(HMz)", 20, 14, 16, 14)
        else:
            print(Fore.RED + "That is not an option!")
    elif access == "5":
        print(Fore.GREEN + "Have fun doing something else in your day!")
        break
    elif access == "$$$":
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        print(Fore.RED + "That is not an option!")



#limit on value on each thing