from collections import deque
m_dir = [(1,0),(0,1),(-1,0),(0,-1)]
h_dir = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]

def BFS():
    while Q:
        r,c,cnt,h_cnt = Q.popleft()
        for dr1, dc1 in m_dir:
            nr = r+dr1
            nc = c+dc1
            if nr>H-1 or nc>W-1 or nr<0 or nc<0 or arr[nr][nc] or visit[nr][nc][h_cnt]:continue
            if (nr, nc) == (H - 1, W - 1): return cnt + 1
            visit[nr][nc][h_cnt] = 1
            Q.append((nr,nc,cnt+1,h_cnt))
        if h_cnt<K:
            for dr2, dc2  in h_dir:
                nr = r+dr2
                nc = c+dc2
                if nr > H - 1 or nc > W - 1 or nr < 0 or nc < 0 or arr[nr][nc] or visit[nr][nc][h_cnt+1]: continue
                if (nr,nc)==(H-1,W-1):return cnt+1
                visit[nr][nc][h_cnt+1] = 1
                Q.append((nr,nc,cnt+1,h_cnt+1))
    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visit = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
visit[0][0][0] = 1
Q = deque()
Q.append((0,0,0,0))
print(BFS())