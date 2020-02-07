T = int(input())
for t in range(1, T+1):
    N = int(input())
    for i in range(N):
        for j in range(N):
            li.append([i, j])
    for x,y in li:
        num = N
        li = []
        li_x = []
        li_y = []
        li_d = []
        cnt = 0
        for x in range(N):
            for y in range(N):
                Queen_p = [x, y]
                if (x not in li_x) and (y not in li_y):
                    if [x, y] not in li_d:
                        li_x.append(x)
                        li_y.append(y)
                        for d in range(N):
                            if x+d < N and y+d < N and 0<= x-d and 0<= y-d:
                                li_d.append([x+d, y+d])
                                li_d.append([x-d, y+d])
                                li_d.append([x+d, y-d])
                                li_d.append([x-d, y+d])
                        num -= 1
