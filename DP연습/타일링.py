tile = [1,2,2]
visit = [0] * (251)
visit[0] = 1
for i in range(250):
    for t in tile:
        if visit[i]:
            if i + t > 250:
                break
            visit[i + t] += visit[i]

from sys import stdin
for n in map(int, stdin.read().split()):
    print(visit[n])


