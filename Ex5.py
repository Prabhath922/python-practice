# replase all odd no in a list with -1
lst=[3,4,5,6,6,4,3,456,62,5,6,4,4,3,5,9]
odd=[-1 if x %2!=0 else x for x in lst]
print(odd)