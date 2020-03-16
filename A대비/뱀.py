from collections import deque
from copy import deepcopy

def BFS():
    body = 1

    while Q:
        h_r, h_c, t_r, t_c, d_h, d_t, k = Q.popleft()
        hn_r,hn_c = h_r+dir[d_h][0], h_c+dir[d_h][1]
        tn_r, tn_c = t_r+dir[d_t][0], t_c+dir[d_t][1]
        if arr[hn_r][hn_c] == 1:
            return k
        if X[k]:
            if X[k] == 'D':
                d_h = (d_h+1)%4
            else:
                d_h = (d_h-1)%4
        if arr[hn_r][hn_c]==2:
            arr[hn_r][hn_c] = 0
            arr[h_r][h_c] = 1
            Q.append((hn_r,hn_c,t_r,t_c,d_h,d_t,k+1))
            body += 1
        else:
            if X[k-body]:
                if X[k-body] == 'D':
                    d_t = (d_t + 1) % 4
                else:
                    d_t = (d_t - 1) % 4
            arr[h_r][h_c] = 1
            arr[tn_r][tn_c] = 0
            Q.append((hn_r,hn_c,tn_r, tn_c,d_h,d_t,k+1))

dir = [(-1,0),(0,1),(1,0),(0,-1)]
N = int(input())
K = int(input())
X = [0]*10001
arr = [[1]*(N+2)]
for i in range(N):
    arr.append([1]+[0]*N+[1])
arr.append([1]*(N+2))

for _ in range(K):
    r,c = map(int,input().split())
    arr[r][c] = 2

L = int(input())
for _ in range(L):
    sec,d = input().split()
    X[int(sec)] = d

Q = deque()
Q.append((1,1,1,0,1,1,1))
print(BFS())