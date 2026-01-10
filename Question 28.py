'''    1
       0 1
       1 0 1
       0 1 0 1
       1 0 1 0 1      '''
   
   # If the sum of row number and column number is even → print 1
   #   If it is odd → print 0

for i in range(1,6):
    for j in range(1,i+1):
        if(i+j)% 2 == 0:
           print("1",end= " ")
        else:
            print("0" , end= " ")
    print()