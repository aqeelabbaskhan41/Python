a=5
for a in range(5):
    if(a==3): #3 will be missing in this bcz it came back to start at 3
        continue #It continues the iteration to next after meeting condition without going below
    print("HI" ,a) 
#Continue with while loop
a=6
while(a>0):
    if (a==2):
        continue #it left the given condition and contine to next iteration 
    print(a)
    a-=1
