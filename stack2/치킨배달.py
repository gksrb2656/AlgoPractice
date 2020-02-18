def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            c = chosen[:]
            # print(c)
            return combo.append(c)

        # 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])


def distance(v,N):
    dis = []
    for i in House:
        Min = 2*N
        r, c = i
        for j in v:
            r2, c2 = j
            k = abs(r-r2)+abs(c-c2)
            if Min > k:
                Min = k
        dis.append(Min)
    return sum(dis)




N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

N_ch = 0
chiken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chiken.append([i, j])
            N_ch += 1

House = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            House.append([i, j])

combo = []
bit = [0] * N_ch
sub_ch = []
combination(chiken,M)
MIN_dis = 0
for i in combo:
    if MIN_dis == 0:
        MIN_dis = distance(i,N)
    elif MIN_dis > distance(i,N):
        MIN_dis = distance(i,N)

print(MIN_dis)


