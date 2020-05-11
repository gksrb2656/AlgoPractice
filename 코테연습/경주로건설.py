from collections import deque
dr=[1,0,-1,0]
dc=[0,1,0,-1]
def solution(board):
    N = len(board)
    visit = [[10000000]*N for _ in range(N)]
    visit[0][0] = 0
    Q = deque()
    Q.append((0,0,0,-1))
    def BFS():
        while Q:
            r,c,m,dd = Q.popleft()
            for d in range(4):
                nr = r+dr[d]
                nc = c+dc[d]
                if nr>N-1 or nc>N-1 or nr<0 or nc<0 or board[nr][nc]:continue
                if dd == d or dd == -1:
                    if visit[nr][nc] < m+100: continue
                    Q.append((nr, nc, m+100, d))
                    visit[nr][nc] = m+100
                else:
                    if visit[nr][nc] < m+600: continue
                    Q.append((nr, nc, m+600, d))
                    visit[nr][nc] = m+600
    BFS()
    answer = visit[N-1][N-1]
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))