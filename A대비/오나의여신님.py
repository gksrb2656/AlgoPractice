from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS():
    global Flag
    while Q:
        r,c,type,depth = Q.popleft()
        for k in range(4):
            nr, nc = r+dr[k],c+dc[k]
            if nr>N-1 or nc>M-1 or nr<0 or nc<0:continue
            if arr[nr][nc] =='.':
                arr[nr][nc] = type
                Q.append((nr,nc,type,depth+1))
            if arr[nr][nc] == 'D':
                if type == 'S':
                    Flag = True
                    return depth + 1




T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    Q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                Q.append((i,j,'*',0))
    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'S':
                flag = True
                Q.append((i,j,'S',0))
                break
        if flag:break

    Flag = False
    ans = BFS()
    if Flag:
        print("#{} {}".format(t,ans))
    else:
        print("#{} GAME OVER".format(t))