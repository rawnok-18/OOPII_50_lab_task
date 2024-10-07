R = [[5, 4, 3],
    [2, 4, 6],
    [4, 7, 9],
    [8, 1, 3]]

transResult = [[0, 0, 0, 0],
            [0, 0, 0, 0],
             [0, 0, 0, 0]]

for a in range(len(R)):
    for b in range(len(R[0])):
        transResult[b][a] = R[a][b]

print("The transpose of matrix R is: ")
for res in transResult:
   print(res)
