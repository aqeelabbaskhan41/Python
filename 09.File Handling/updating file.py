# In this mode you can read and write the same file by using r+ sign in mode and you can append and write in the file at the same time by using a+  sign

# f=open('E:\Python Fundamentals\File Handling\sample.txt','r+')
# b=f.write("This is")
# a=f.read()

# print(a)
# f.close()

f=open('E:\Python Fundamentals\File Handling\sample.txt','a+')  #appending and reading
a=f.write("Nice ")
f.seek(0) #With using this keyword
a=f.read()

print(a)
f.close()