num=int(input("Enter the number: "))
factorial=1
# for i in range(num,1,-1): or
for i in range(1,num+1):
    factorial=factorial*i
print(factorial) #it give answer
#using fstream
print(f"The factorial of {num} is {factorial}") #it is more convinient