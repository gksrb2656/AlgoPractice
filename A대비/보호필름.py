def inspection():
    for i in range(W):
        cnt = 1
        flag = False
        for j in range(D - 1):
            if film[j][i] == film[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt == K:
                flag = True
                break
        if not flag:
            return 0
    return 1


def comb(k, n, idx):
    global film
    if k == n:
        chemical(n)
        return

    for i in range(idx, D):
        select_row[i] = 1
        film_copy = [data[:] for data in film]
        comb(k + 1, n, i + 1)
        select_row[i] = 0
        film = film_copy


def chemical(n):
    global Flag
    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                select_ch[j] = 1
            else:
                select_ch[j] = 0
        ch = 0
        for r in range(D):
            if select_row[r]:
                film[r] = [select_ch[ch]] * W
                ch += 1
        if inspection():
            Flag = True
            return


T = int(input())
for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    select_row = [0] * D
    Flag = True
    if not inspection():
        Flag = False
        for i in range(1, K + 1):
            select_ch = [0] * i
            comb(0, i, 0)
            if Flag:
                print("#{} {}".format(t, i))
                break
    else:
        print("#{} {}".format(t, 0))