visit = []
dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]

def DFS(omoc, s, color):
    for i in range(len(s)):
        if s[i] not in visit:
            visit.append(s[i])
            r, c = visit[i]
        else:
            continue
        cnt = 1
        dir = 0
        while dir < 8:
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr >= 0 and nr < 19 and nc >= 0 and nc < 19 and ([nr, nc] not in visit) and omoc[nr][nc] == color:
                visit.append([nr, nc])
                r, c = nr, nc
                cnt += 1
            else:
                if cnt == 5:
                    print(color)
                    for p in visit[-5]:
                        print(p+1, end =' ')
                    return
                r, c = visit[i]
                dir += 1
                cnt = 1
    return 1

omoc = [list(map(int,input().split())) for _ in range(19)]
s1 = []
s2 = []
for i in range(19):
    for j in range(19):
        if omoc[i][j] == 1:
            s1.append([i,j])
        elif omoc[i][j] == 2:
            s2.append([i,j])

o_1 = DFS(omoc, s1, 1)
# o_2 = DFS(omoc, s2, 2)
# if o_1 and o_2:
#     print(0)
