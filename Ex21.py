# square of 1 with 0 as center
matrix=[[1 if i==0 or i==4 or j==0 or j==4 else 0 for j in range(5)]for i in range(5)]
print(matrix)