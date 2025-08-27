# find the index of the non zero indecies
lst=[234,4,5,54,0,34,34,34,34,43,43,445,45,44,0,35434,43,0,23,0,3,0,3,0]
non_zero_indicies=[i for i ,x in enumerate(lst) if x!=0]
print(non_zero_indicies)