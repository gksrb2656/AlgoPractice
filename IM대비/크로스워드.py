A, B = input().split()
arr = [['.']*len(A) for _ in range(len(B))]

idx_a = ''
idx_b = ''
# key = ''

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            idx_a = i
            idx_b = j
            # key = A[i]
            break
    if idx_a != '':
        break


for i in range(len(A)):
    arr[idx_b][i] = A[i]
for i in range(len(B)):
    arr[i][idx_a] = B[i]

for i in arr:
    print(''.join(i))
