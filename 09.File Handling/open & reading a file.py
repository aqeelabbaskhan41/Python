# f= open('E:\Python Fundamentals\File Handling\sample.txt','r') #(adress of file,mode(r,w,append))
# f=open('E:\Python Fundamentals\File Handling/test write file.txt')
f=open('File Handling/sample.txt') #By defalut mode is reading

# a=f.read()# It reads the full file
# a=f.readlines() #It read the file as a list
a=f.read(5) #it will read first 5 characters
# a=f.readline()#it will read first line
# a=f.readline()#it will read second line and so on you can use
print(a)
f.close()
