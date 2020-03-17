from itertools import permutations
import sys

MAX = 0
def Scoring(order):
    score = 0
    idx = 0
    for n in arr:
        out_cnt = 0
        b1,b2,b3=0,0,0
        while out_cnt < 3:
            if n[order[idx]] == 0:
                out_cnt += 1
            elif n[order[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif n[order[idx]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif n[order[idx]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif n[order[idx]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for per in permutations(range(1, 9)):
    order = list(per[:3]) + [0] + list(per[3:])
    MAX = max(MAX,Scoring(order))
print(MAX)

