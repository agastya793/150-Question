''' *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *       '''
# for upperpart
for i in range(1,6):
    for j in range(i):
        print("*" , end="")
    print()

# for lowerpart
for i in range(1,5):
    for j in range(4-i+1):
       print("*" , end="")
    print()
