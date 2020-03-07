bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
def bing(bingo, call):
    visit_r = []
    visit_c = []
    cnt = 0
    d1 = 0
    d2 = 0
    for i in range(len(call)):
        for r in range(5):
            for c in range(5):
                if bingo[r][c] == call[i]:
                    visit_r.append(r)
                    visit_c.append(c)
                    if visit_r.count(r) == 5:
                        cnt +=1
                        if cnt == 3:
                            return i
                    if visit_c.count(c) == 5:
                        cnt +=1
                        if cnt == 3:
                            return i
                    if r-c == 0:
                        d1 += 1
                        if d1 == 5:
                            cnt += 1
                            if cnt == 3:
                                return i
                    if r+c == 4:
                        d2 += 1
                        if d2 == 5:
                            cnt += 1
                            if cnt == 3:
                                return i

for i in range(5):
    call = call + list(map(int, input().split()))

c = bing(bingo, call)+1
print(c)