T = int(input())
# import sys
# sys.stdin = open("input.txt", "r")
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T+1 ):
    N = int(input())
    li = list(input().split())
    ma = 0
    mi = 0
    for j in li:
        if int(j) > ma:
            ma = int(j)
        if mi ==0:
            mi = int(j)
        elif mi > int(j):
            mi = int(j)
    sub = ma - mi
    print('#{0} {1}'.format(i,ma-mi))