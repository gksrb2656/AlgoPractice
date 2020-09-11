from itertools import combinations

def solution(relation):
    answer = 0
    candidates = set()
    column_len = len(relation[0])
    column_num = [i for i in range(column_len)]

    for i in range(1, column_len + 1):
        for comb in combinations(column_num, i):
            check = set()
            flag = 0
            for candy in candidates:
                if len(set(list(candy)+list(comb)))==len(comb):
                    flag = 1
                    break
                if flag: break
            if flag: continue
            for cnt in range(len(relation)):
                count = 0
                c = []
                while count < i:
                    c.append(relation[cnt][comb[count]])
                    count += 1
                check.add(tuple(c))
            if len(check) == len(relation):
                candidates.add(comb)
    answer = len(candidates)
    return answer

solution(	[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])