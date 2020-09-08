from collections import deque
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def BFS_st():
    global energy, st, ed
    Q = deque()
    Q.append(st)
    dst = -1
    visit = [[0] * (N+1) for _ in range(N+1)]
    while Q:
        clients = []
        dst += 1
        flag = 0
        for _ in range(len(Q)):
            r, c = Q.popleft()
            if (r,c) in st_ed:
                clients.append([r,c])
                flag = 1
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if nr>N or nr<1 or nc>N or nc<1 or visit[nr][nc] or MAP[nr][nc]==1:continue
                visit[nr][nc] = 1
                Q.append((nr,nc))
        if flag:
            clients.sort()
            if energy <= dst:
                return 0
            else:
                energy -= dst
                st = tuple(clients[0])
                ed = st_ed[st]
                st_ed.pop((st))
                return 1
    return 0

def BFS_ed():
    global energy, st, ed
    Q = deque()
    Q.append(st)
    dst = -1
    visit = [[0] * (N+1) for _ in range(N+1)]
    while Q:
        dst += 1
        for _ in range(len(Q)):
            r, c = Q.popleft()
            if (r,c) == ed:
                if dst>energy:
                    return 0
                else:
                    energy += dst
                    st = ed
                    return 1
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if nr > N or nr < 1 or nc >N or nc < 1 or visit[nr][nc] or MAP[nr][nc]==1: continue
                Q.append((nr,nc))
                visit[nr][nc] = 1
    return 0


N, M, energy = map(int,input().split())
MAP = [[0]*(N+1)]
for _ in range(N):
    MAP.append([0]+list(map(int,input().split())))
check = 0
st = list(map(int,input().split()))
ed = (0,0)
st_ed = dict()
for m in range(M):
    st1,st2,ed1,ed2 = map(int,input().split())
    st_ed[(st1,st2)] = (ed1,ed2)

flag = 1
while check<M:
    if BFS_st():
        if BFS_ed():
            check += 1
        else:
            flag = 0
            break
    else:
        flag = 0
        break

if not flag:
    print(-1)
else:
    print(energy)