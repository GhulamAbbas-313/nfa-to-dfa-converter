import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=[]
for i in range(len(a)):
	row=[]
	for j in range(len(a[i])):
		row.append(a[i][j]+b[i][j])
	x.append(row)
wow=np.array([x])
print(f"a matrix numpy:\n {a}")
print(f"b matrix numpy:\n {b}")


for row in wow:
	print(f"Mean of every row:\n ,{sum(a+b)/len(a)}")
	print(f"This is the sum of the two matrixes 'a' and 'b':\n {row}")
print(a.dtype,b.dtype)
