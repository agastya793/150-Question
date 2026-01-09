'''  * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *    '''

#for upperpart

n= 5
for i in range(5,0,-1):
    print(" " *(n-i) + "* " *(i))

#for lowerpart

n= 5
for i in range(1,n+1):
    print(" " *(n-i)+ "* " * (i))