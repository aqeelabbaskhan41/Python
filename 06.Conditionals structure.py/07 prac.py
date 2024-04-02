post=input("Enter the post: ")
if("Aqeel" in post):
    check="Yes"
elif("aqeel" in post):
    check="Yes"
elif("AQEEL"):
    check="Yes"
else:
    check="No"

if(check=="Yes"):
    print("Yes talking about Aqeel")
# if("Yes" in check): #Other method
#     print("Yes talking about Aqeel")
else:
    print("No, not talking about Aqeel")