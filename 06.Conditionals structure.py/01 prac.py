no1=int(input("Enter the number 1:"))
no2=int(input("Enter the number 2:"))
no3=int(input("Enter the number 3:"))
no4=int(input("Enter the number 4:"))

# if(no1>no2 and no1>no3 and no1>no4):
#     print("Number 1 is greater number")
# elif(no2>no1 and no2>no3 and no2>no4):
#     print("Number 2 is greater number")
# elif(no3>no1 and no3>no2 and no3>no4):
#     print("Number 3 is greater number")
# elif(no4>no1 and no4>no2 and no4>no3):
#     print("Number 4 is greater number")

# Other method
if(no1>no4):
    f1=no1
else:
    f1=no4

if(no2>no3):
    f2=no2
else:
    f2=no3

if(f1>f2):
    print(str(f1) + "is greatest") # Covertion into string for concetination
else:
    print(f2 , "is greatest")

