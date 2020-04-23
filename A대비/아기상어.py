from collections import deque
dr = [-1,0,0,1]
dc = [0,-1,1,0]

def move():
    dis = 0
    n = 0
    size = 2
    while Q:
        r1, c1 = Q.popleft()
        arr[r1][c1] = 0
        Q2 = deque()
        Q2.append((r1,c1,0))
        visit = [[0] * N for _ in range(N)]
        visit[r1][c1] = 1
        def BFS():
            global Q
            nonlocal Q2, n, size, dis
            s_dis = s_r = s_c = -1
            while Q2:
                r, c, k= Q2.popleft()
                for d in range(4):
                    nr,nc = r+dr[d],c+dc[d]
                    if nr>N-1 or nc>N-1 or nr<0 or nc<0 or visit[nr][nc]:continue
                    if not arr[nr][nc] or arr[nr][nc]==size:
                        Q2.append((nr,nc,k+1))
                        visit[nr][nc] = 1
                    elif 0<arr[nr][nc]<size:
                        if s_dis == -1:
                            s_dis = k+1
                            s_r,s_c = nr,nc
                        elif s_dis == k+1:
                            if s_r>nr:
                                s_r,s_c = nr,nc
                            elif s_r ==nr:
                                if s_c>nc:
                                    s_r,s_c = nr,nc
                        else:
                            n+=1
                            if size == n:
                                n=0
                                size += 1
                            arr[s_r][s_c] = 0
                            dis += s_dis
                            return Q.append((s_r,s_c))
            if s_dis != -1:
                n += 1
                if size == n:
                    n = 0
                    size += 1
                arr[s_r][s_c] = 0
                dis += s_dis
                return Q.append((s_r, s_c))
        BFS()
    return dis

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j]==9:
                return i,j
Q.append(find_shark())
print(move())
