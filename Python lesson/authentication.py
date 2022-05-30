import email
import random
from operator import truediv

database = {}
def accontGenerator():
    print("Your account number is:")
    return random.randrange(111111111, 999999999)


def login():
    print("this is login")




def bankOpp():
    print("welcome to operations")

def register():
    print('****REGISTER****')
    email1= input("Pleaase enter your email: ")
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    password= input("Enter password: ")
    account_num = accontGenerator()
    
    database[ account_num ] = [first_name,  last_name, email1, password]
    
    print('Your Account Has Been created Successfully')
    login()
    bankOpp()
    return database


def check():
    print("Welcome to IZBbank")
    validOption = False

    while (validOption == False):
        
        print("Do you have an account with us?")
    

        haveAccount = int(input("if Yes press 1. \n if no press 2: \n"))
        if( haveAccount == 1):
            validOption = True
            login()
        elif (haveAccount == 2):
            validOption = True
            print(register())

        else:
            print("invalid option entered")

check()    



print(accontGenerator())



