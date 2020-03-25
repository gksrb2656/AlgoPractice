def game():
    for i in range(N):
        r,c = 1,i
        nc = c
        while r<H+2:
            if ladder[r][nc]:
                nc = ladder[r][nc]-1
            r+=1
        if nc != c:
            return 0
    return 1

def combo(k, r_n, n):
    global MIN
    global Flag
    if k == r_n:
        if game():
            MIN = r_n
            Flag=True
        return

    for i in range(n,N*(H+1)):
        r = i // N
        c = i % N
        if c+1>N-1:continue
        if ladder[r][c] or ladder[r][c+1]:continue
        ladder[r][c] = c+2
        ladder[r][c+1] = c+1
        combo(k+1,r_n,i+2)
        if Flag: return
        ladder[r][c] = 0
        ladder[r][c+1] = 0

N, M, H = map(int, input().split())
ladder = [[0]*N for _ in range(H+2)]
MIN = H
if M == 0:
    print(0)
else:
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b-1] = b+1
        ladder[a][b] = b
    Flag = False
    for i in range(4):
        combo(0,i,N)
        if Flag: break
    if MIN>3 or not Flag:print(-1)
    else:print(MIN)