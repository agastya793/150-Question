'''    ****
       *  *
       *  *
       *  *
       ****     '''

n = 5

for i in range(1,n+1):
    if i == 1 or i ==n:
        print("*" * 4)
    else:
        print("*" + " " * 2 + "*")