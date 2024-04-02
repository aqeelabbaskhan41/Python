def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
        
m=max(2,90,11)
print(m)

#Built in method
# l=[432,4,2]
# a=max(l)
# print(a)

#Append in the list
# l=[]
# for i in range(3):
#     a=int(input("enter number:"))
#     l.append(a)
# print(l)
