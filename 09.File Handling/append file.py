# For appending we will use append mode in file writing
file=open('E:\Python Fundamentals\File Handling/append file.txt','a') 
a=file.write(" I am appending") #How many times you will run this it will append the same text in the file 
print(a)
file.close()