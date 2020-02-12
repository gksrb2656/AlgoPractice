dr = [1, -1, 0]
dc = [0, 0, 1]

for t in range(1,11):
    T = int(input())
    s_p = []
    visit = []
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[0][i] == 1:
            s_p.append([0,i])

    for i in s_p:
        r, c = i[0], i[1]
        for j in range(2):
            nr = r + dr[j]
            nc = c + dc[j]
            if nr >= 0 and nr<=99 and nc>=0 and nc<=99:
                if ladder[nr][nc] == 1 and [nr,nc] not in visit:
                    visit.append([nr,nc])
                    r, c = nr, nc
            else:
                for k in range(2,3):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if nr >= 0 and nr <= 99 and nc >= 0 and nc <= 99:
                        if ladder[nr][nc] == 1 and [nr, nc] not in visit:
                            visit.append([nr, nc])
                            r, c = nr, nc
                        elif ladder[nr][nc] == 2:
                            print(c)



