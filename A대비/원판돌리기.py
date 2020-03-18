dr = [1,-1,0,0]
dc = [0,0,1,-1]

def find():
    global cnt
    flag = False
    total = 0
    for i in range(1,N+1):
        total += sum(arr[i])
        for j in range(M):
            for k in range(4):
                nr= i + dr[k]
                nc= (j + dc[k])%M
                if nr<1 or nr>N: continue
                if arr[i][j] and arr[i][j] == arr[nr][nc]:
                    flag = True
                    visit[i][j] = 1
                    visit[nr][nc] = 1

    if flag:
        for i in range(1,N+1):
            for j in range(M):
                if visit[i][j]:
                    total -= arr[i][j]
                    cnt -= 1
                    arr[i][j] = 0
                    visit[i][j] = 0
    else:
        if cnt:
            avr = total/cnt
            for i in range(1,N+1):
                for j in range(M):
                    if arr[i][j]:
                        if arr[i][j]>avr:
                            arr[i][j] -= 1
                            total -= 1
                        elif arr[i][j]<avr:
                            arr[i][j] += 1
                            total += 1
    return total

N, M, T = map(int, input().split())
arr = [[0]*M]
for i in range(N):
    arr.append(list(map(int, input().split())))
xdk = [list(map(int, input().split())) for _ in range(T)]
visit = [[0]*M for _ in range(N+1)]
cnt = N*M

for t in range(T):
    X, D, K = xdk[t]
    for _ in range(K):
        for i in range(1,N+1):
            if not i%X:
                if D:
                    a = arr[i].pop(0)
                    arr[i].append(a)
                else:
                    a = arr[i].pop()
                    arr[i] = [a]+arr[i]

    ans = find()

print(ans)