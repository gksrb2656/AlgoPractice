# import sys
# sys.stdin = open("input.txt", "r")
for t in range(10):
    T = int(input())
    li = [list(map(int, input().split())) for i in range(100)]
    li_r = []
    li_c = []
    li_d1 = []
    li_d2 = []
    M = 0
    for i in range(100):
        r = 0
        c = 0
        d1 = 0
        d2 = 0
        for j in range(100):
            r += li[i][j]
            c += li[j][i]
            if i == j:
                d1 += li[i][j]
            if i == 100-j:
                d2 += li[i][j]
        li_r.append(r)
        li_c.append(c)
        li_d1.append(d1)
        li_d2.append(d2)
    s_li = li_r + li_c + li_d1 + li_d2
    for k in s_li:
        if k > M:
            M = k
     print(M)


