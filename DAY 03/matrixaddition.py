mat1=[[1,2],
      [2,1]]
mat2=[[2,1],
      [1,2]]

if len(mat1)==len(mat2):

    matsum=[[mat1[i][j]+mat2[i][j] for j in range (len(mat1[0]))]
    for i in range (len(mat1))]
    print("Sum of Matrix ")
    print()

for row in matsum:
    print(" ".join(map(str,row)))
