import sys
sys.stdin = open('input.txt', 'r')
for t in range(1,11):
    T = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    Min = 10000
    point = 0
    # print(li)
    for j in range(100):
        cnt = 1
        if li[0][j] == 1:
            r = 0
            c = j
            while r < 99:
                if li[r+1][c] == 1:
                    r += 1
                    cnt += 1
                    if c < 99 and li[r][c+1]==1:
                        while c < 99 and li[r][c+1]:
                            cnt += 1
                            c += 1
                        continue
                        # while (li[r][c+1] == 0) or (li[r][c+1] == 0):
                        #     cnt += 1
                        #     r += 1
                    elif c > 0 and li[r][c-1]==1:
                        while c > 0 and li[r][c-1]:
                            cnt += 1
                            c -= 1
            if cnt < Min:
                Min = cnt
                point = j
    print('#{} {}'.format(t, point))






