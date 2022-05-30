james = 2+2

# print(james)

# name = "johnson"
# age = 25
# print("His name is %s and he is %d years old." %(name, age) )

age = 18
movie = "College Adults"

if (age >= 18):
    print("Allow access to the cinema")
    
age2= 16
age= age2
if (age< 18 and movie == "College Adults"):
    print(" You are not allowed here")

height = 5.9
if(age < 16 or height < 5.9):
    print("You can't make it to the military")

elif(age>= 16 and height >= 5.9):
    print("Welcome to the military")
else:
    ("Something is up somewhere")