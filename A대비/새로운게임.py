dir = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}

N, K = map(int, input().split())
arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
arr_copy = [[[] for _ in range(N+1)] for _ in range(N+1)]
players = [list(map(int, input().split()))+[0] for _ in range(K)]
for i in range(K):
    if arr_copy[players[i][0]][players[i][1]]:
        players[i][3] = len(arr_copy[players[i][0]][players[i][1]])
        arr_copy[players[i][0]][players[i][1]].append(i+1)
    else:
        arr_copy[players[i][0]][players[i][1]].append(i+1)

def move():
    answer = 0
    while True:
        answer += 1
        if answer>=1000:
            return -1
        for i in range(K):
            x,y = players[i][0],players[i][1]
            nxt_x,nxt_y=x+dir[players[i][2]][0],y+dir[players[i][2]][1]
            if nxt_x>N or nxt_x<1 or nxt_y>N or nxt_y<1 or arr[nxt_x][nxt_y] == 2:
                if players[i][2]%2:
                    players[i][2] += 1
                else:
                    players[i][2] -= 1
                nxt_x, nxt_y = x + dir[players[i][2]][0], y+dir[players[i][2]][1]
                if nxt_x>N or nxt_x<1 or nxt_y>N or nxt_y<1 or arr[nxt_x][nxt_y] == 2:
                    continue
                if arr[nxt_x][nxt_y] == 0:
                    cnt = 0
                    rev = arr_copy[x][y][players[i][3]:]
                    arr_copy[x][y] = arr_copy[x][y][:players[i][3]]
                    for i_s in rev:
                        players[i_s-1][3] = len(arr_copy[nxt_x][nxt_y]) + cnt
                        players[i_s-1][0], players[i_s-1][1] = nxt_x, nxt_y
                        cnt += 1
                    arr_copy[nxt_x][nxt_y] += rev
                    if len(arr_copy[nxt_x][nxt_y])>=4:
                        return answer
                elif arr[nxt_x][nxt_y] == 1:
                    rev = arr_copy[x][y][players[i][3]:]
                    rev = rev[::-1]
                    cnt = 0
                    arr_copy[x][y] = arr_copy[x][y][:players[i][3]]
                    for i_s in rev:
                        players[i_s-1][3] = len(arr_copy[nxt_x][nxt_y]) + cnt
                        players[i_s-1][0], players[i_s-1][1] = nxt_x, nxt_y
                        cnt += 1
                    arr_copy[nxt_x][nxt_y] += rev
                    if len(arr_copy[nxt_x][nxt_y])>=4:
                        return answer
            elif arr[nxt_x][nxt_y] == 0:
                cnt = 0
                rev = arr_copy[x][y][players[i][3]:]
                arr_copy[x][y] = arr_copy[x][y][:players[i][3]]
                for i_s in rev:
                    players[i_s-1][3] = len(arr_copy[nxt_x][nxt_y])+cnt
                    players[i_s-1][0], players[i_s-1][1] = nxt_x, nxt_y
                    cnt += 1
                arr_copy[nxt_x][nxt_y] += rev
                if len(arr_copy[nxt_x][nxt_y]) >= 4:
                    return answer
            elif arr[nxt_x][nxt_y] == 1:
                rev = arr_copy[x][y][players[i][3]:]
                rev = rev[::-1]
                cnt = 0
                arr_copy[x][y] = arr_copy[x][y][:players[i][3]]
                for i_s in rev:
                    players[i_s-1][3] = len(arr_copy[nxt_x][nxt_y])+cnt
                    players[i_s-1][0], players[i_s-1][1] = nxt_x, nxt_y
                    cnt += 1
                arr_copy[nxt_x][nxt_y] += rev
                if len(arr_copy[nxt_x][nxt_y]) >= 4:
                    return answer
print(move())