T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]

    Min = 2500
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            cnt = 0
            for ii in range(i+1):
                cnt += M-arr[ii].count('W')
            for jj in range(i+1,j+1):
                cnt += M-arr[jj].count('B')
            for kk in range(j+1,N):
                cnt += M-arr[kk].count('R')
            if cnt<Min:
                Min = cnt
    print("#{} {}".format(t,Min))