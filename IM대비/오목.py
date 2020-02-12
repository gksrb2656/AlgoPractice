visit1 = []
visit2 = []
dr = [1,1,0,-1]
dc = [0,1,1,1]
call = []
omoc = [list(map(int,input().split())) for _ in range(19)]
s1 = []
s2 = []
for i in range(19):
    for j in range(19):
        if omoc[i][j] == 1:
            visit1.append([i,j])
            r1, c1 = i,j
            cnt = 1
            dir = 0
            while dir < 4:
                nr = r1 + dr[dir]
                nc = c1 + dc[dir]
                if nr >= 0 and nr < 19 and nc >= 0 and nc < 19 and omoc[nr][nc] == 1:
                    visit1.append([nr, nc])
                    r1, c1 = nr, nc
                    cnt += 1
                else:
                    if cnt == 5 :
                        if i - dr[dir]>= 0 and j - dc[dir] >= 0 :
                            if omoc[i - dr[dir]][j - dc[dir]] != 1:
                                print(1)
                                s1.append((i+1,j+1))
                                print(i+1,j+1)
                        else:
                            print(1)
                            s1.append((i+1, j+1))
                            print(i+1, j+1)
                    r1, c1 = i, j
                    dir += 1
                    cnt = 1
        elif omoc[i][j] == 2:
            visit2.append([i, j])
            r2, c2 = i, j
            cnt = 1
            dir = 0
            while dir < 4:
                nr = r2 + dr[dir]
                nc = c2 + dc[dir]
                if nr >= 0 and nr < 19 and nc >= 0 and nc < 19 and omoc[nr][nc] == 2:
                    visit2.append([nr, nc])
                    r2, c2 = nr, nc
                    cnt += 1
                else:
                    if cnt == 5 :
                        if i-dr[dir] >= 0 and j-dc[dir]>=0 :
                            if omoc[i-dr[dir]][j-dc[dir]] != 2:
                                print(2)
                                s2.append((i+1, j+1))
                                print(i+1, j+1)
                        else:
                            print(2)
                            s2.append((i+1, j+1))
                            print(i+1, j+1)
                    r2, c2 = i,j
                    dir += 1
                    cnt = 1
if len(s1) == 0 and len(s2)==0:
    print(0)