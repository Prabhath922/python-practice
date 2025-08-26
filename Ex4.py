# extract all the odd no from a list of integers
lst=[1,4,2,4,2,5,6,7,8,4,3,6]
odd=[x for x in lst if x% 2 !=0]
print(odd)