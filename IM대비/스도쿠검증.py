T = int(input())
for t in range(1,T+1):
    result = 1
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    rsdoku = list(zip(*sdoku))

    for s in sdoku:
        for i in range(1, 10):
            if s.count(i) != 1:
                result = 0
                break
        if result == 0:
            break
    for s in rsdoku:
        for i in range(1, 10):
            if s.count(i) != 1:
                result = 0
                break
        if result == 0:
            break
    for r in range(3):
        for c in range(3):
            dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i in range(r*3,(r+1)*3):
                for j in range(c*3,(c+1)*3):
                    if sdoku[i][j] in dic:
                        # print(i, j)
                        dic[sdoku[i][j]] += 1
            for v in dic.values():
                if v != 1:
                    result = 0
                    break
    if result != 0:
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))
