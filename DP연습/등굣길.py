def solution(m, n, puddles):
    arr =[[0]*(m+1) for _ in range(n+1)]
    arr[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j == 1: continue
            if [j,i] in puddles:continue
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[n][m]

print(solution(	4, 3, [[2, 2]]))