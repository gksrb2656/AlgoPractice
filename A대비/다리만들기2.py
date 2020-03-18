from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bridge(point):
    r,c = point
    for d in range(4):
        nr, nc = r,c
        leng = 0
        while 1:
            nr += dr[d]
            nc += dc[d]
            if nr>N-1 or nc>M-1 or nr<0 or nc<0 :break
            if not arr[nr][nc]:
                leng += 1
            elif arr[nr][nc] and arr[nr][nc] != arr[r][c] and leng>1:
                if (arr[nr][nc], arr[r][c]) in nodes: break
                elif (arr[r][c],arr[nr][nc]) in nodes:
                    nodes[(arr[r][c],arr[nr][nc])].add(leng)
                else:
                    nodes[(arr[r][c], arr[nr][nc])] = {leng}
                break
            else: break


def BFS(i,j):
    Q.append((i,j))
    land = [(i,j)]
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr>N-1 or nc>M-1 or nr<0 or nc<0 or visit[nr][nc]:continue
            if arr[nr][nc] and arr[nr][nc] != n_isl:
                Q.append((nr,nc))
                visit[nr][nc] = 1
                arr[nr][nc] = n_isl
                land += [(nr,nc)]
    islands.append(land)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
n_isl = 1
islands = []
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visit[i][j]:
            n_isl += 1
            Q = deque()
            arr[i][j] = n_isl
            BFS(i,j)

nodes = dict()
for i in range(n_isl-1):
    for j in islands[i]:
        bridge(j)


distances = []
for v in map(list,nodes.values()):
    distances += v

distances.sort()
union = list()
ans = 0

for dis in distances:
    for key,val in nodes.items():
        if dis in val:
            if not union:
                union.append({key[0],key[1]})
                ans += dis
                break
            flag = False
            flag2 = False
            for u in range(len(union)):
                if u == len(union)-1:
                    flag2 = True
                if key[0] in union[u]:
                    if key[1] in union[u]:
                        break
                    else:
                        for u2 in range(u+1,len(union)):
                            if key[1] in union[u2]:
                                flag = True
                                ans += dis
                                union.append(union[u]|union[u2])
                                union.pop(u)
                                union.pop(u2-1)
                                break
                        if flag:
                            break
                        if not flag:
                            union[u].add(key[1])
                            ans += dis
                            flag = True
                            break
                elif key[1] in union[u]:
                    for u2 in range(u+1,len(union)):
                        if key[0] in union[u2]:
                            flag = True
                            ans += dis
                            union.append(union[u] | union[u2])
                            union.pop(u)
                            union.pop(u2-1)
                            break
                    if flag:
                        break
                    if not flag:
                        union[u].add(key[0])
                        ans += dis
                        flag = True
                        break
                if not flag and flag2:
                    union.append({key[0], key[1]})
                    ans += dis

if len(union)>1 or not union:
    print(-1)
elif len(union)==1:
    if len(union[0])<n_isl-1:
        print(-1)
    else:
        print(ans)