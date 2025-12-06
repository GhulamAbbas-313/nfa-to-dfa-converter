allocation=[
	[0,1,0],
	[2,0,0],
	[3,0,2],
	[2,1,1],
	[0,0,2]
]
maxneed=[
	[7,5,3],
	[3,2,2],
	[9,0,2],
	[2,2,2],
	[4,3,3]
]
available=[]
need=[]
A=10
B=5
C=7
for i in range(len(maxneed)):
	row=[]
	for j in range(len(maxneed[i])):
		row.append(abs(maxneed[i][j]-allocation[i][j]))
	need.append(row)
totalallocatebya_b_c=[
sum(allocation[i][0] for i in range(len(allocation))),
sum(allocation[i][1] for i in range(len(allocation))),
sum(allocation[i][2] for i in range(len(allocation)))

]
available=[

]
allocation[0] -= totalallocatebya_b_c[0]
allocation[1] -= totalallocatebya_b_c[1]
allocation[2] -= totalallocatebya_b_c[2]
print("Available",available)

print("Allocation")
for i in allocation:
	print(i)
print("Need")
for row in need:
  print(row)


	 

	
	
