import random
#Snake,water and gun or Rock ,paper and scissor
def game(you,comp):
    if comp==you:
        return None
    elif you=='s':
        if comp=='g':
            return False
        elif comp=='w':
            return True
    elif you=='g':
        if comp=='w':
            return False
        elif comp=='s':
            return True
    elif you=='w':
        if comp=='g':
            return True
        elif comp=='s':
            return False


rand_no=random.randint(1,3)
comp=print("Computer turn: Snake(s) ,Water(w) ,Gun(g)")
if rand_no==1:
    comp='s'
elif rand_no==2:
    comp='w'
else:
    comp=='g'

you=input ("Your turn: Snake(s) ,Water(w) ,Gun(g): ")
print(f"Computer={comp}")
print(f"You={you}")
a=game(you,comp)

if (a==None):
    print("Game is tie")
elif a: # a==True
    print("You win!")
else:
    print("You loose the game!")