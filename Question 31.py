'''      *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *    '''

n = 5   # height of the top half

# upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
