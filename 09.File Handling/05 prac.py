list=["donkey","kaddu","moty"]
with open("09.File Handling\donkey rep.txt") as f:
   word= f.read()
for i in list:   
    word = word.replace(i,'######')

    with open("09.File Handling\donkey rep.txt",'w') as f:
        f.write(word)