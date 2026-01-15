#  Write a program to generate a matrix where each element is a Fibonacci number.
def generate_fibonacci_matrix(rows,cols):

    #generate fibonacci numbers
    total_elements = rows * cols
    fib = [0,1]

    while len(fib) < total_elements:
        fib.append(fib[-1] + fib[-2])

        # fill the matrix
    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(fib[index])
            index += 1
        matrix.append(row)
    return matrix
r = int(input("enter number of rows: "))   
c = int(input("enter number of columns: "))  

result = generate_fibonacci_matrix(r,c)

print("fibonacci matrix: ")
for row in result:
    print(row)