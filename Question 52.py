# Write a program to generate number patterns (e.g., sequential numbers in a matrix).

rows = int(input("enter number of rows: "))
cols = int(input("enter number of columns: "))

num = 1
for i in range(rows):
    for j in range(cols):
        print(num, end="\t")
        num += 1
    print()
               