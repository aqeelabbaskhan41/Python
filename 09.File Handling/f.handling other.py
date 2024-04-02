# import os
# # with open('E:\Python Fundamentals\File Handling\other.cpp','r') as f:
# #     a=f.read()
# #     print(a)

# os.remove("E:\Python Fundamentals\File Handling\other.cpp")
file=open('09.File Handling/append file.txt','a+')
a=file.write("Hey you")
file.write(" its me ")

file.seek(0) #it starts reading file at given index
print(file.read())

# a=file.read()
# print(a)