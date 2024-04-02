def game():
    return 9

score=game()

with open("E:\Python Fundamentals/09.File Handling\high score.txt") as fl:
    hscore =fl.read()

if hscore=='':
    with open("E:\Python Fundamentals/09.File Handling\high score.txt",'w') as f:
        f.write(str(score))
elif score > int(hscore) :
    with open("E:\Python Fundamentals/09.File Handling\high score.txt",'w') as f:
        f.write(str(score))

