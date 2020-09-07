from copy import deepcopy
dx = (0,-1,-1,0,1,1,1,0,-1)
dy = (0,0,-1,-1,-1,0,1,1,1)

pos = dict()
answer = 0
def f_move(fishes,sx,sy,s_d,s_p,pos):
    global answer
    for i in fishes:
        for key, value in pos.items():
            if value[0] == i:
                x, y = key
                d = value[1]
                nx, ny = x+dx[d], y+dy[d]
                flag = 1
                while True:
                    if 0<=nx<=3 and 0<=ny<=3 and pos[(nx,ny)] != [-1,-1]:
                        break
                    d += 1
                    if d>8:
                        d -= 8
                    if d == value[1]:
                        flag = 0
                        break
                    nx, ny = x + dx[d], y + dy[d]
                if flag:
                    pos[key][1] = d
                    pos[key], pos[(nx,ny)] = pos[(nx,ny)], pos[key]
                break
    nsx,nsy = sx,sy
    while True:
        nsx += dx[s_d]
        nsy += dy[s_d]
        if pos.get((nsx,nsy)):
            if pos[(nsx,nsy)] != [0,0]:
                fishes_copy = fishes[:]
                fishes_copy.remove(pos[(nsx,nsy)][0])
                pos_copy = deepcopy(pos)
                pos_copy[(nsx,nsy)] = [-1,-1]
                pos_copy[(sx,sy)] = [0,0]
                f_move(fishes_copy,nsx,nsy,pos[(nsx,nsy)][1],s_p+pos[(nsx,nsy)][0],pos_copy)
        else:
            answer = max(answer,s_p)
            return

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        pos[(i,j)] = [data[j*2],data[j*2+1]]
s_p = pos[(0,0)][0]
s_d = pos[(0,0)][1]
pos[(0,0)] = [-1,-1]
fishes = [(i+1) for i in range(16)]
fishes.remove(s_p)
f_move(fishes,0,0,s_d,s_p,pos)
print(answer)