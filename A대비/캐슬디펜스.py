def kill(ar_1,ar_2,ar_3,depth,cnt):
    global MAX
    combo = [(N,ar_1),(N,ar_2),(N,ar_3)]
    anemies = set()
    while depth<=N:
        for k in combo:
            r, c = k
            MIN_d = N**M
            anemy = 0
            for i in range(N-depth,-1,-1):
                if r-i>D+depth-1:break
                for j in range(M):
                    if not arr_copy[i][j] or abs(r-i)+abs(c-j)>D+depth-1:continue
                    if abs(r-i)+abs(c-j)<MIN_d:
                        MIN_d = abs(r - i) + abs(c - j)
                        anemy = (i, j)
                    elif MIN_d == abs(r-i)+abs(c-j):
                        if anemy[1]>j:
                            anemy = (i, j)
            if anemy:
                anemies.add(anemy)
        for a in anemies:
            if arr_copy[a[0]][a[1]]:
                cnt += 1
                arr_copy[a[0]][a[1]] = 0
        depth+=1

    if cnt>MAX:
        MAX = cnt
        return

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            arr_copy = [data[:] for data in arr]
            kill(i,j,k,1,0)
print(MAX)
