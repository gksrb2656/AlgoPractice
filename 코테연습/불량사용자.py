def solution(user_id, banned_id):
    answer = 0
    duples = []
    visit = []
    for i in banned_id:
        flag = 0
        dupl = []
        for j in user_id:
            if len(i) == len(j):
                flag2 = 1
                for k in range(len(i)):
                    if i[k] != '*':
                        if i[k] != j[k]:
                            flag2 = 0
                            break
                if flag2:
                    if not flag:
                        flag = 1
                        temp = [j]
                    else:
                        dupl += temp + [j]
                        temp = []
        if dupl:
            duples.append(dupl)
            visit.append([0]*len(dupl))

    order = []
    combos = []
    def comb(n,depth):
        if depth == n:
            if len(order) == n:
                if sorted(order) in combos:return
                combos.append(sorted(order[:]))
            return

        for j in range(len(duples[depth])):
            if visit[depth][j]:continue
            if duples[depth][j] in order:continue
            visit[depth][j] = 1
            order.append(duples[depth][j])
            comb(n,depth+1)
            order.pop()
            visit[depth][j] = 0
    comb(len(duples),0)
    return len(combos)