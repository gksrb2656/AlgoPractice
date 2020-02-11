N = int(input())
arr = [[0]*101 for _ in range(101)]
for i in range(1,N+1):
    r, c, w, h= map(int, input().split())
    for k in range(r, r+w):
        for j in range(c, c+h):
            arr[k][j] = i
for i in range(1,N+1):
    summ = 0
    for r in range(101):
        for c in range(101):
            if arr[r][c] == i:
                summ += 1
    print(summ)
