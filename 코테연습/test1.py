def inspections(r,c,n):
    check = set()
    for j in range(9):
        if arr[r][j] == n:
            return 0
    for i in range(9):
        if arr[i][c] == n:
            return 0
    R, C = r // 3, c // 3
    for i in range(R * 3, (R + 1) * 3):
        for j in range(C * 3, (C + 1) * 3):
            if arr[i][j] == n:
                return 0
    arr[r][c] = n
    return 1

for t in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 0
    inspector = []
    for _ in range(N):
        r, c, n = map(int, input().split())
        inspector.append((r,c,n))
    for ins in inspector:
        if inspections(*ins):
            ans += 1
        else:
            break
    print("#{} {}".format(t,ans))