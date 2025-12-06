import threading
#start of matrixes using threading


def matrix_logics(n, m):
    matrix = []  # Initialize an empty matrix
    for i in range(n):
        print(f"Enter the values separated by space for row {i+1}:")
        while True:
            try:
                rows = list(map(int, input().split()))
                if len(rows) != m: 
                  print("Invalid input. Number of elements doesn't match the number of columns.")
                  continue
                matrix.append(rows)  
                break
            except ValueError:
                 print("Invalid input. Please enter numbers only.")
    return matrix  

def matrix_addition(matrix1,matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print("The sum of matrix1 and matrix2 is :")
    for rows in result:
        print(rows)

def matrix_subtraction(matrix1,matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print("The subtraction of matrix1 and matrix2 is :")
    for rows in result:
        print(rows)
# Input for matrix dimensions
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))


# Input for the first matrix
print("\nInput for Matrix 1:")
matrix1 = matrix_logics(n, m)

# Input for the second matrix
print("\nInput for Matrix 2:")
matrix2 = matrix_logics(n, m)

# Print the matrices
print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

# matrix_addition(matrix1,matrix2)
# matrix_subtraction(matrix1,matrix2)
print("1 = for Addition of Matrix1 and Matrix2) \n2 = for Subtraction of Matrix1 and Matrix2")
formatrix=int(input("1 or 2 "))
if formatrix==1:
  add=threading.Thread(target=matrix_addition,args=(matrix1,matrix2,))
  add.start()
  add.join()
elif formatrix==2:
    minus=threading.Thread(target=matrix_subtraction,args=(matrix1,matrix2,))
    minus.start()
    minus.join()
else:
    print("Invalid choice")


#end of matrixes using threading