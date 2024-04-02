# n!=n* (n-1)!
#Sum(n)= sum(n-1)+n

def sum(n):
    if  n==0:
        return 0
    else:
        return n+ (sum(n-1))

s=sum(100)
print(s)