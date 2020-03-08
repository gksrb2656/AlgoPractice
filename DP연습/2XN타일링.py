n = int(input())
tile = [1,2]
visit = [0]*(n+1)
visit[0] = 1

for i in range(n):
    for t in tile:
        if visit[i]:
            if t+i>n:break
            visit[i+t] += visit[i]
print(visit[n]%10007)