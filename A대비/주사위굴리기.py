dir = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
dice_ho = [0,0,0,0]
dice_ver = [0,0,0,0]
N,M,x,y,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

for i in command:
    nx = x + dir[i][0]
    ny = y + dir[i][1]
    if nx>N-1 or ny>M-1 or nx<0 or ny<0:continue
    if i == 1:
        h = dice_ho.pop(0)
        dice_ho += [h]
        dice_ver[0] = dice_ho[0]
        dice_ver[2] = dice_ho[2]
    elif i == 2:
        h = dice_ho.pop()
        dice_ho = [h] + dice_ho
        dice_ver[0] = dice_ho[0]
        dice_ver[2] = dice_ho[2]
    elif i == 3:
        v = dice_ver.pop(0)
        dice_ver += [v]
        dice_ho[0] = dice_ver[0]
        dice_ho[2] = dice_ver[2]
    else:
        v = dice_ver.pop()
        dice_ver = [v] + dice_ver
        dice_ho[0] = dice_ver[0]
        dice_ho[2] = dice_ver[2]
    if arr[nx][ny]:
        dice_ver[0]= dice_ho[0] = arr[nx][ny]
        arr[nx][ny] = 0
        x,y=nx,ny
    elif arr[nx][ny] == 0:
        arr[nx][ny] = dice_ho[0]
        x,y=nx,ny
    print(dice_ho[2])
