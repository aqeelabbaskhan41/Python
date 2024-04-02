# Using this no need to close file by self it automatically close the file
with open('E:\Python Fundamentals\File Handling\sample.txt','r+') as file:
    a=file.read()
    # a=f.write("hiiiiiiii") write or append mode
    print(a)

# for opening file in text mode use rt/r,wt/w or at/t and opening in binary mode use rb,wb or ab