# from collections import deque
# Q=deque()
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
                        if nr - dr[dir] * 6 >= 0 and nc - dc[dir] * 6 > 0 and omoc[nr - dr[dir] * 6][nc - dc[dir] * 6] != 1:
                            print(1)
                            s1.append((nr-dr[dir]*5+1,nc-dc[dir]*5+1))
                            print(nr - dr[dir] * 5 + 1, nc - dc[dir] * 5 + 1)
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
                        if nr-dr[dir]*6 >= 0 and nc-dc[dir]*6>0 and omoc[nr-dr[dir]*6][nc-dc[dir]*6] != 2:
                            print(2)
                            s2.append((nr-dr[dir]*5+1,nc-dc[dir]*5+1))
                            print((nr-dr[dir]*5+1,nc-dc[dir]*5+1))
                    r2, c2 = i,j
                    dir += 1
                    cnt = 1
if len(s1) == 0 and len(s2)==0:
    print(0)
# elif len(s1) != 0:
#     print(1)
#     for i in min(s1):
#         print(i, end = ' ')
# else:
#     print(2)
#     for i in min(s2):
#         print(i, end = ' ')





