import random
matrix=[[random.random() for _ in range(3)]for _ in range(3)]
diag=sum(matrix for i in range(3))
print(diag)

