from collections import deque

dir = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}

def fishing(C):
    global ans, arr
    for i in range(C):
        flag = 0
        move = [[[0] * 3 for _ in range(C)] for _ in range(R)]
        for j in range(R):
            if arr[j][i][2]:
                flag = 1
                d_r, d_c = j, i
                ans += arr[j][i][2]
                # arr[j][i] = [0]*4
                break
        for _ in range(len(Q)):
            r,c = Q.popleft()
            s,d,z = arr[r][c]
            if flag and (r,c) == (d_r,d_c):continue
            nr = r+dir[d][0]*s
            nc = c+dir[d][1]*s
            if nr>R-1:
                if (nr//(R-1))&1:
                    d=1
                    nr = (R-1)-nr%(R-1)
                else:
                    nr = nr%(R-1)
            elif nr<0:
                if (nr // (R - 1)) & 1:
                    d=2
                    nr = (R - 1) - nr % (R - 1)
                else:
                    nr = nr%(R-1)
            elif nc>C-1:
                if (nc//(C-1))&1:
                    d=4
                    nc = (C-1)-nc%(C-1)
                else:
                    nc = nc%(C-1)
            elif nc<0:
                if (nc // (C - 1)) & 1:
                    d=3
                    nc = (C - 1) - nc % (C - 1)
                else:
                    nc = nc%(C-1)
            if move[nr][nc][2]:
                if move[nr][nc][2]<z:
                    move[nr][nc][0] = s
                    move[nr][nc][1] = d
                    move[nr][nc][2]=z
            else:
                move[nr][nc][0] = s
                move[nr][nc][1] = d
                move[nr][nc][2] = z
                # arr[nr][nc][3] = i+1
                Q.append((nr,nc))
        arr = [data[:] for data in move]

R, C, M = map(int, input().split())
arr = [[[0]*3 for _ in range(C)] for _ in range(R)]
Q = deque()
ans = 0
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    arr[r-1][c-1][0] = s
    arr[r-1][c-1][1] = d
    arr[r-1][c-1][2] = z
    Q.append((r-1,c-1))

fishing(C)
print(ans)


