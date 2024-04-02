
try:
    a=int(input('Enter the dividend: '))
    b=int(input("Enter the divisor:"))
    r=a/b
    print("Result:",r)
except ValueError:
    print("Invalid input please enter an integer!")
except ZeroDivisionError:
    print("Error; cannot divide by zero")
else:
    print("Division performed successfully")
finally:
    print("Execution successfully completed")