marks=int(input("Enter your marks: "))
# if(marks>=90 and marks<=100):
#     print("Excellent")
# elif(marks>=80 and marks<90):
#     print("Your grade is: A")
# elif(marks>=70 and marks<80):
#     print("Your grade is: B")
# elif(marks>=60 and marks<70):
#     print("Your grade is: C")
# elif(marks>=50 and marks<60):
#     print("Your grade is: D")
# else:
#     print("Your grade is: F")

# other method
if (marks>=90):
    grade="Ex"    
elif (marks>=80):
    grade="A"
elif (marks>=70):
    grade="B"
elif (marks>=60):
    grade="C"
elif (marks>=50):
    grade="D"
else:
    grade="F"


print("Your grade is " + grade)