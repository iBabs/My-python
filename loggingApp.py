name = input("what is your name \n")
allowedName = ["Tunji", "Hadizah", "Gift"]
allowedPass = ["pasoma", "saheed", "obesere"]

if(name in allowedName):
    password = input("Your password? \n")
    usersId = allowedName.index(name)

    if(password == allowedPass[usersId]):
        print("welcome %s" %name)
        print("the following are your available options:")
        print("1. Withdrawal")
        print("2. Transfer")
        print("3. Chaecck Balance")
        print("4. Complaint")

        slctedOption = int(input("Select an option\n"))

        if( slctedOption == 1):
            print("You selected %s" %slctedOption)
        elif( slctedOption == 2):
            print("You selected %s" %slctedOption)
        elif( slctedOption == 3):
            print("You selected %s" %slctedOption)
        elif( slctedOption == 4):
            print("You selected %s" %slctedOption)
        else:
            print("invalid option")

    
    else:
        print("incorrect password")

else:
    print("Name not registered")
    
    
