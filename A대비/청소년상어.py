# dr = (1,0,-1,0,1,-1,1,-1)
# dc = (0,1,0,-1,1,1,-1,-1)
dir = {1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}
def s_move():
    global shark_p
    while shark_p[0]>=0 or shark_p[0]<4 or shark_p[1]>=0 or shark_p[1]<4:
        shark_p = shark_p+dir[shark_dir]





arr = [[[0,0] for _ in range(4)] for _ in range(4)]

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(0,8,2):
        arr[i][j//2][0] = data[j]
        arr[i][j//2][1] = data[j+1]

shark_dir = arr[0][0][1]
shark_p = [0,0]
s = arr[0][0][0]
arr[0][0][0] = -1
