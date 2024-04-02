file= open('E:\Python Fundamentals/09.File Handling\poem.txt','r')
a=file.read()
# print(a.find("twinkle"))
if "twinkle" in a:
    print("twinkle is present")
else:
    print ("twinkle is not present")

file.close()
