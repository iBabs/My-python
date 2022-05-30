


print( 'Welcome to calculator')
print ('select your options')
print("1.Addition")
print ("2.Subtraction")
print ("3. Multiplication")
print ("4.Division")
print ("5. Remainder")

slcted_option = int(input("choose an optin from above: "))

if (slcted_option == 1):
                    print("you have selected %s" %slcted_option)
                    numb1 = int(input("Enter a first number to be added: "))
                    num2 = int(input("%d plus: " %numb1))
                    result = (numb1 + num2)
                    print("your answer is %d" %result)
                    


elif (slcted_option == 2):
                    print("you have selected %s" %slcted_option)
                    numb1 = int(input("Enter a first number: "))
                    num2 = int(input("%d minus: " %numb1))
                    result = (numb1 - num2)
                    print("your answer is %d" %result)
                    

elif (slcted_option == 3):
                    print("you have selected %s" %slcted_option)
                    numb1 = int(input("Enter a first number: "))
                    num2 = int(input("%d multipled by: " %numb1))
                    result = (numb1 * num2)
                    print("your answer is %d" %result)
                    

elif (slcted_option == 4):
                    print("you have selected %s" %slcted_option)
                    numb1 = int(input("Enter a first number: "))
                    num2 = int(input("%d divided by: " %numb1))
                    result = (numb1 / num2)
                    print("your answer is %d" %result)

elif (slcted_option == 5):
                    print("you have selected %s" %slcted_option)
                    numb1 = int(input("Enter a first number: "))
                    num2 = int(input("Enter a second number: "))
                    result = (numb1 % num2)
                    print("your answer is %d" %result)
                    
                    

else:
    print("Selected option is not available")

