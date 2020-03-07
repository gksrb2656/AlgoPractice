from copy import deepcopy

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def connect(v, pcr, length, visit):
    global pc
    global leng
    if pcr + (len(sp)-v)<pc:
        return
    if v == len(sp):
        if pc == pcr and leng > length:
            leng = length
        elif pc < pcr:
            pc = pcr
            leng = length
        return

    r, c = sp[v]
    for i in range(5):
        if i == 4:
            connect(v + 1, pcr, length, visit)
            continue
        visit1 = deepcopy(visit)
        nr = r + dr[i]
        nc = c + dc[i]
        s_length = 0
        while 1:
            if arr[nr][nc] != 0 or visit1[nr][nc] != 0:
                break
            if nr == N - 1 or nc == N - 1 or nr == 0 or nc == 0:
                visit1[nr][nc] = 1
                connect(v + 1, pcr + 1, length + s_length + 1, visit1)
                break
            else:
                visit1[nr][nc] = 1
                s_length += 1
                nr += dr[i]
                nc += dc[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sp = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                sp.append([i, j])

    visit = [[0] * N for _ in range(N)]
    pc = 0
    leng = 0
    connect(0, 0, 0, visit)
    print('#{} {}'.format(t,leng))

