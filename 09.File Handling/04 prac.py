with open("09.File Handling\donkey rep.txt") as f:
   r= f.read()
r = r.replace('donkey','######')

with open("09.File Handling\donkey rep.txt",'w') as f:
   f.write(r)



   

