power = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}

def cal(i,j):
    sum_h = 0
    for h in arr[i][j:j+M]:
        h = power[h]
        sum_h += h
    return sum_h

def cal2(n,i,j):
    global MAX
    s = 0
    for d in order:
        s += d ** 2
    if s > MAX:
        MAX = s

    for k in range(n,M):
        if sum(order) + li[k]<=C:
            order.append(li[k])
            cal2(k+1,i,j)
            order.pop()

def honey_comb(depth):
    global sum_h
    global ans
    if depth == 2:
        if sum_h>ans:
            ans = sum_h
        return

    for i in range(N):
        for j in range(N-M+1):
            if visit[i][j:j+M] == [0]*M:
                sum_h += values[i][j]
                visit[i][j:j+M] = [1]*M
                honey_comb(depth+1)
                visit[i][j:j + M] = [0] * M
                sum_h -= values[i][j]


T = int(input())
for t in range(1,T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    values = [[0] * (N-M+1) for _ in range(N)]
    honey = [0,0]
    sum_h = 0
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            if sum(arr[i][j:j + M]) <= C:
                MAX = cal(i, j)
            else:
                li = arr[i][j:j + M]
                order = [0]
                MAX = max(arr[i][j:j + M]) ** 2
                cal2(0, i, j)
            values[i][j] = MAX
    honey_comb(0)

    print("#{} {}".format(t,ans))

