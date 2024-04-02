age= int(input("Enter your age: "))

# logical And
if(age>30 and age<50):
    print("You can work with us")
else:
    print("You cannot work with us")

#Logical OR
if(age>30 or age<50): #one should true
    print("You can work with us")
else:
    print("You cannot work with us")

#Not
if(age != 18): #it is symbol not
    print("you cannot work with us")