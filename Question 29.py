'''    *        *
       **      **
       * *    * *
       *  *  *  *
       *   **   *
       *   **   *
       *  *  *  *
       * *    * *
       **      **
       *        *        '''

n = 10 
for i in range(n):
    for j in range(n):
        #border star
        if j == 0 or j == n-1:
            print("*" , end="")
        # diagonal star
        elif j == i or j == n-i-1:
            print("*",end = "")    
        else:
            print(" " , end= "")    
    print()