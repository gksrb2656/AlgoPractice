from copy import deepcopy

dr = [1,0,-1,0]
dc = [0,1,0,-1]


def clean(v, side):
    st_r, st_c = r, c = v, 0
    dir = 1
    nxt = 0
    cur = 0
    while 1:
        if side == 'up':
            d = (dir+1)%4
        else:
            d = (dir-1)%4
        nr = r + dr[dir]
        nc = c + dc[dir]
        if (nr, nc) == (st_r, st_c):
            return
        if nr > R-1 or nr < 0 or nc > C-1 or nc <0 :
            dir = d
        elif room[nr][nc] >=0:
            cur = room[nr][nc]
            room[nr][nc] += nxt
            room[nr][nc] -= cur
            nxt = cur
            r = nr
            c = nc


def spread(i,j):
    cnt = 0
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if nr<0 or nc<0 or nr>R-1 or nc>C-1:
            continue
        if room[nr][nc] == -1:
            continue
        room[nr][nc] += room_copy[i][j]//5
        cnt += 1
    room[i][j] -= (room_copy[i][j] // 5)*cnt

def find_air(R):
    A_f = 0
    for j in range(R):
        if room[j][0] == -1:
            A_f = j
            return A_f


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

Air = find_air(R)

for _ in range(T):
    room_copy = deepcopy(room)
    for i in range(R):
        for j in range(C):
            if room[i][j]>0:
                spread(i,j)
    if Air != 0:
        clean(Air,'up')
    if Air+1 != R-1:
        clean(Air+1,'down')

cnt = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            cnt += room[i][j]
print(cnt)



