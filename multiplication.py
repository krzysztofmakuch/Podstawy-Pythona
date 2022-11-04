#here is where you add numbers to your desired matrices
matrix1=[[5,-1,0],
         [4,9,4],
         [-10,0,-7]]
matrix2=[[1,-5,5],
         [6,-2,1],
         [2,13,-3]]
def MultiplyMatrix(m1,m2):
    result2=[]
    for row1 in range(len(m1)):
        result1=[]
        for col in range(len(m2)):
            num = 0
            for row2 in range(len(m2[0])):
                num=num+m1[row1][row2]*m2[row2][col]
            result1.append(num)#creating a matrix row
        result2.append(result1)#adding the row to matrix
    return result2
result=MultiplyMatrix(matrix1,matrix2)
print(result)

