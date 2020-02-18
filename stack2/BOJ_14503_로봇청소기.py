import sys
input = sys.stdin.readline
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def DFS(row,col,dir):
    ans = 0
    stack = []
    stack.append([row,col])
    while stack:
        cnt = 0
        r, c = stack.pop()
        if arr[r][c] == 0:
            arr[r][c] = 2
            ans += 1
        for i in range(4):
            cnt += 1
            nr = r + dr[(dir-i-1)%4]
            nc = c + dc[(dir-i-1)%4]
            if arr[nr][nc] != 0:
                if cnt == 4:
                    br = r - dr[(dir-i-1)%4]
                    bc = c - dc[(dir-i-1)%4]
                    if arr[br][bc] == 1:
                        return ans
                    stack.append([br,bc])
                    dir = (dir - i-1)%4
                    cnt = 0
            else:
                stack.append([nr,nc])
                dir = (dir-i-1)%4
                break
    return ans


N, M = map(int, input().split())
row, col, dir = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(DFS(row,col,dir))
