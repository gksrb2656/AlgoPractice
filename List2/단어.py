import sys
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puz = [list(map(int,input().split())) for _ in range(N)]
    nums = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puz[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    nums += 1
                cnt = 0
        if cnt == K:
            nums += 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puz[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    nums += 1
                cnt = 0
        if cnt == K:
            nums += 1
    print(nums)




