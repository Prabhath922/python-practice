# convert a lsit of integers to booleans where all non zero no are true
lst=[2,3,4,45,3,2,3,4,3,3,3,3,34,0,3,3,3,0,4,0,3,3,5,6,4,4,4,4,564,4,55,34,534,4533,64]
boolean=[bool(x) for x in lst]
print(boolean)