def percent(marks):
    return (sum(marks)/400)*100

marks=[33,52,76,69]
percentage=percent(marks)

mark2=[43,76,64,55]
p=percent(mark2)
print(percentage,p)
# percentage=(sum(marks)/400)*100 #Here sum is built in fuction to calculate the sum of list 
# or
# percentage=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 #Here we calculate sum using index
# print(percentage)

