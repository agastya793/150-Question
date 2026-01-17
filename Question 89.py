# Write a program to calculate the sum of the diagonal elements in a square matrix.

n = int(input("Enter the size of the matrix: "))

matrix = []
print("Enter the elements row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

diag_sum = 0

for i in range(n):
    diag_sum += matrix[i][i]

print("Sum of diagonal elements:", diag_sum)
