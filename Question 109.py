# Write a program to find the largest element in each row of a matrix.

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

# Taking matrix input
for i in range(rows):
    row = []
    print(f"Enter elements of row {i+1}:")
    for j in range(cols):
        value = int(input())
        row.append(value)
    matrix.append(row)

# Finding largest element in each row
largest_elements = []

for row in matrix:
    largest_elements.append(max(row))

print("Matrix:", matrix)
print("Largest element in each row:", largest_elements)
