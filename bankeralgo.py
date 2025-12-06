allocation = [ 
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
maxneed = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [4, 2, 2],
    [5, 3, 3]
]
A = 10
B = 5
C = 7
print(f"Instance of A={A}, B={B} and C={C}")
need = []
available = [A, B, C]  # Initialize available with total resources

print(f"Allocation :")
for i in allocation:
    print(i)

print(f"Max Need :")
for i in maxneed:
    print(i)

for i in range(len(maxneed)):
    row = []
    for j in range(len(maxneed[i])):
        row.append(maxneed[i][j] - allocation[i][j])
    need.append(row)

TotalAllocation = [
    sum(allocation[i][0] for i in range(len(allocation))),
    sum(allocation[i][1] for i in range(len(allocation))),
    sum(allocation[i][2] for i in range(len(allocation))),
]
print("Total Allocation of A, B and C", TotalAllocation)
available[0] -= TotalAllocation[0]
available[1] -= TotalAllocation[1]
available[2] -= TotalAllocation[2]
print("Available", available)

print("Remaining Need :")
for row in need:
    print(row)

# Check for safe sequence
safe_sequence = []
while len(safe_sequence) < len(allocation):
    found = False
    for i in range(len(need)):
        if i not in safe_sequence and all(need[i][j] <= available[j] for j in range(len(available))):
            safe_sequence.append(i)
            available = [available[j] + allocation[i][j] for j in range(len(available))]
            found = True

            break
    if not found:
        print("No Safe Sequence exists")
        break
else:
    print("Safe Sequence exists:", safe_sequence)
