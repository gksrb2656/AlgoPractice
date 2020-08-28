for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    memo = [[N*N]*N for _ in range(N)]
    h_n = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                h_n += 1

    max_val = h_n*M
    max_size = 1
    while max_size**2+((max_size-1)**2)<=max_val:
        max_size += 1
    max_size -= 1

    MAX_hn = 0
    for k in range(max_size, -1, -1):
        for i in range(N):
            for j in range(N):
                if memo[i][j]<=MAX_hn:continue
                cnt = 0
                for ii in range(i-k+1,i+k):
                    if ii<0 or ii>N-1:continue
                    for jj in range(j-k+1,j+k):
                        if abs(i-ii)+abs(j-jj)>=k:continue
                        if jj<0 or jj>N-1:continue
                        if MAP[ii][jj]:
                            cnt += 1
                if cnt*M>=k**2+((k-1)**2):
                    MAX_hn = max(MAX_hn,cnt)
                    memo[i][j] = cnt
    print("#{} {}".format(t,MAX_hn))
#
# for t in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     memo = [[N*N]*N for _ in range(N)]
#     h_n = 0
#     for i in range(N):
#         for j in range(N):
#             if MAP[i][j]:
#                 h_n += 1
#
#     max_val = h_n*M
#     max_size = 1
#     while max_size**2+((max_size-1)**2)<=max_val:
#         max_size += 1
#     max_size -= 1
#
#     MAX_hn = 0
#     def solve():
#         global MAX_hn,max_size
#         for k in range(max_size, -1, -1):
#             flag = 0
#             for i in range(N):
#                 for j in range(N):
#                     if memo[i][j]<=MAX_hn:continue
#                     cnt = 0
#                     for ii in range(i-k+1,i+k):
#                         if ii<0 or ii>N-1:continue
#                         for jj in range(j-k+1,j+k):
#                             if abs(i-ii)+abs(j-jj)>=k:continue
#                             if jj<0 or jj>N-1:continue
#                             if MAP[ii][jj]:
#                                 cnt += 1
#                     if cnt*M>=k**2+((k-1)**2):
#                         MAX_hn = max(MAX_hn,cnt)
#                         flag = 1
#                         memo[i][j] = cnt
#             if flag:return
#     solve()
#     print("#{} {}".format(t,MAX_hn))
