# Input for the first matrix
Mat1 = [list(map(int, input("Enter row of Mat1: ").split())) for _ in range(2)]

# Input for the second matrix
Mat2 = [list(map(int, input("Enter row of Mat2: ").split())) for _ in range(2)]

# Matrix addition
MatSum = [[Mat1[i][j] + Mat2[i][j] for j in range(2)] for i in range(2)]

# Print the result matrix
for row in MatSum:
    print(" ".join(map(str, row)))
