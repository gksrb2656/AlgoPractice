dr = [0,1,0,-1]
dc = [1,0,-1,0]

def permu(depth,order):
    global MIN
    if depth == K:
        arr_copy = [data[:] for data in arr]
        for o in order:
            r,c,s = o
            turn(r,c,s,arr_copy)
        for i in range(1, N + 1):
            MIN = min(MIN, sum(arr_copy[i]))
        return

    for i in range(K):
        if visit[i]:continue
        order.append(rcs[i])
        visit[i] = 1
        permu(depth+1,order)
        order.pop()
        visit[i] = 0



def turn(r,c,s,G):
    while s>0:
        nr,nc = r-s,c-s
        nxt = 0
        for d in range(4):
            while 1:
                if not nxt:
                    temp = G[r-s][c-s]
                else:
                    temp = nxt
                nr += dr[d]
                nc += dc[d]
                if nr>N or nc>M or nr<1 or nc<1 or nr<r-s or nc<c-s or nr>r+s or nc>c+s:
                    nr -= dr[d]
                    nc -= dc[d]
                    break
                nxt = G[nr][nc]
                G[nr][nc] = temp
        s -= 1


N,M,K = map(int,input().split())
arr = [[0]*(M+2)]
for i in range(N):
    arr.append([0]+list(map(int, input().split()))+[0])
arr.append([0]*(M+2))

rcs = [0]*K
for i in range(K):
    r,c,s = map(int, input().split())
    rcs[i] = (r,c,s)

visit = [0]*K
order =[]
MIN = 250000
permu(0,order)
print(MIN)
