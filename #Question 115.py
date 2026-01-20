'''XOXOXO
   OXOXOX
   XOXOXO
   OXOXOX'''

rows = 4
cols = 6
for i in range(rows):
    for j in range(cols):
        if(i+j) % 2 == 0:
            print("X", end="")
        else:
            print("O",end="")    
    print()        