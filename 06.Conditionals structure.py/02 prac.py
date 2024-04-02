sub1=int(input("Enter the marks of subject1"))
sub2=int(input("Enter the marks of subject2"))
sub3=int(input("Enter the marks of subject3"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed due to less tha 33 marks in one subject.")

elif ((sub1+sub2+sub3)/3 < 40):
    print("You are failed due to less than 40% marks!")

else:
    add=sub1+sub2+sub3
    a=(add/300)*100
    print("Congratulation! You are passed with " + str(a)+ "% marks")


