for i in range (1,11):
    if(i==5):
        break
    print(i)
else:
    print("Now it is in else statement")  #It will not run after break statement so we can asssume that if loop fully complete than else work otherwise it exit due to break statement bcz after break else will not execute. But after continue  statement it will work properly