'''code for the gpu database'''
import sqlite3
from colorama import Fore, Style, init

#Define user name and password saparate by user and admin
users = {
"Eric":{'password':'123456','role':'admin'},
}

#Initialize colorma
init()

def listeverything():
    print("hi")
    print("hi")