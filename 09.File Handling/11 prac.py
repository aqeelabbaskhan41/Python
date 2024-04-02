import os
ofile='09.File Handling/11 file.txt'
nfile='09.File Handling/renamed by python.txt'

with open(ofile) as f:
    content=f.read()

with open(nfile,'w') as f:
    f.write(content)

os.remove(ofile)