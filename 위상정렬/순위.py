from collections import defaultdict
def solution(n, results):
    wins = defaultdict(set)
    loses = defaultdict(set)
    answer = 0
    for r in results:
        wins[r[0]].add(r[1])
        loses[r[1]].add(r[0])
    for i in range(1,n+1):
        for w in wins[i]:
            loses[w].update(loses[i])
        for l in loses[i]:
            wins[l].update(wins[i])

    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) >= n-1:
            answer += 1
    return answer

solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])