with open('09.File Handling\copy file.txt') as f:
    content=f.read()

with open('09.File Handling\copied file.txt','w') as f:
    f.write(content)