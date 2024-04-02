# n!=1*2*3*4...*n
#n!=[1*2*3*4...(n-1)]*n
# n!=n*(n-1)!  apply this formula in recursive 
# It is a function which calls itself
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
      return  n*factorial(n-1)

print(factorial(5))