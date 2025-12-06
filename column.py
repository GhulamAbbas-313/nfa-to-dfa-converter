list=[
	[1, 2,3],
	[4, 5,6],
	[7, 8,9]
]
mat=[]

print(list[0][0]) # prints 1
print(list[1][0])
print(list[2][0]) 
for i in list:
	print(i[0],i[1],i[2]) # prints 1, 4, 7
print(list[0][0]+list[1][0]+list[2][0])