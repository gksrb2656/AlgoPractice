dir = {0:(1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)}
g = [[[i]] for i in range(4)]
for i in range(4):
    cnt = 0
    while cnt<10:
        sub_g_copy = g[i][-1][:]
        for gg in reversed(g[i][-1]):
            sub_g_copy.append((gg+1)%4)
        g[i].append(sub_g_copy)
        cnt += 1
arr = [[0]*101 for _ in range(101)]
cnt = 0
N = int(input())
for _ in range(N):
    x, y, d, ge = map(int, input().split())
    cnt += 1
    arr[y][x] = 1
    for dd in g[d][ge]:
        x,y = x+dir[dd][0],y+dir[dd][1]
        arr[y][x]=1
ans = 0
for r in range(101):
    for c in range(101):
        if arr[r][c] == 1:
            if r+1>100 or c+1>100:continue
            if arr[r+1][c] == 1 and arr[r+1][c+1] == 1 and arr[r][c+1]==1:
                ans +=1
print(ans)