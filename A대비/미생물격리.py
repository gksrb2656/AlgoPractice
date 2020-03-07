dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

def Move(r,c,k,d):
    nr = r +dir[d][0]
    nc = c +dir[d][1]
    if nr == 0 or nc == 0 or nr==N-1 or nc==N-1:
        k //= 2
        if d%2:
            d += 1
        else:
            d -= 1
    return nr, nc, k, d

def change(m):
    ans = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j][0]:
                arr[i][j][0] = Map[i][j][0]
                Map[i][j][0] = 0
                arr[i][j][1] = Map[i][j][1]
                Map[i][j][1] = 0
                Map[i][j][2] = 0
    if m+1 == M:
        for i in range(N):
            for j in range(N):
                ans += arr[i][j][0]
        return ans

T = int(input())
for t in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = [[[0,0] for _ in range(N)] for _ in range(N)]
    Map = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(K):
        r, c, k, d = map(int, input().split())
        arr[r][c][0] = k
        arr[r][c][1] = d
    for m in range(M):
        for i in range(N):
            for j in range(N):
                if arr[i][j][0] :
                    r,c,k,d = Move(i,j,arr[i][j][0],arr[i][j][1])
                    if not Map[r][c][0]:
                        Map[r][c][0] = k
                        Map[r][c][1] = d
                        Map[r][c][2] = k
                    else:
                        if Map[r][c][2] < k:
                            Map[r][c][0] += k
                            Map[r][c][1] = d
                            Map[r][c][2] = k
                        else:
                            Map[r][c][0] += k
                    arr[i][j][0] = 0
                    arr[i][j][1] = 0
        ans = change(m)
    print(ans)


##좋은 풀이
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#  
# def turn(dir):
#     if dir == 1:
#         return 2
#     elif dir == 2:
#         return 1
#     elif dir == 3:
#         return 4
#     elif dir == 4:
#         return 3
#  
# for tc in range(int(input())):
#     n,m,k = map(int,input().split())
#     orgs = []
#     for _ in range(k):
#         orgs.append([int(char) for char in input().split()])
#     for _ in range(m):
#         state = {}
#         for org in orgs:
#             x,y,dir = org[0],org[1],org[3]
#             nx,ny = x+dx[dir-1],y+dy[dir-1]
#             if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
#                 org_n = org[2]//2
#                 org_dir = turn(dir)
#             else:
#                 org_n = org[2]
#                 org_dir = dir
#             if (nx,ny) in state.keys():
#                 state[(nx,ny)].append((org_n,org_dir))
#             else:
#                 state[(nx,ny)] = [(org_n,org_dir)]
#         orgs = []
#         for key in state.keys():
#             N = 0
#             max_n = 0
#             for l in range(len(state[key])):
#                 N += state[key][l][0]
#                 if state[key][l][0] > max_n:
#                     dir = state[key][l][1]
#                     max_n = state[key][l][0]
#             orgs.append([key[0], key[1], N, dir])
#     ans = 0
#     for o in orgs:
#         ans += o[2]
#     print('#{} {}'.format(tc+1,ans))