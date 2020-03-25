def comb(k,n,order):
    global MIN
    if k==M:
        s_dis = 0
        for h in home:
            dis = N ** 2
            for c in order:
                dis = min(dis,abs(h//N-c//N) + abs(h%N-c%N))
            s_dis += dis
            if s_dis>=MIN-M+k:return
        MIN = min(s_dis, MIN)
        return

    for i in range(n,len(chicken)):
        order[k] = chicken[i]
        comb(k+1,i+1,order)
        if MIN == M:
            return

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr += list(map(int, input().split()))

home = []
chicken = []
order = [-1]*M
MIN = N**5
for i in range(N**2):
    if arr[i] == 1:
        home += [i]
    elif arr[i] == 2:
        chicken +=[i]

comb(0,0,order)
print(MIN)


# def combination(chosen):
#     if len(chosen) == M:
#         c = chosen[:]
#         return combo.append(c)
#
#     start = chiken.index(chosen[-1]) + 1 if chosen else 0
#     for nxt in range(start, len(chiken)):
#         chosen.append(chiken[nxt])
#         combination(chosen)
#         chosen.pop()
#
#
# def distance(v,N):
#     dis = []
#     for i in House:
#         Min = 2*N
#         r, c = i
#         for j in v:
#             r2, c2 = j
#             k = abs(r-r2)+abs(c-c2)
#             if Min > k:
#                 Min = k
#         dis.append(Min)
#     return sum(dis)
#
#
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
#
# N_ch = 0
# chiken = []
# House = []
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 2:
#             chiken.append([i, j])
#             N_ch += 1
#         elif city[i][j] == 1:
#             House.append([i, j])
#
# combo = []
# combination([])
# MIN_dis = 0
# for i in combo:
#     if MIN_dis == 0:
#         MIN_dis = distance(i,N)
#     elif MIN_dis > distance(i,N):
#         MIN_dis = distance(i,N)
#
# print(MIN_dis)