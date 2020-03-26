from collections import deque

dr = [1,0,-1,0,1,1,-1,-1]
dc = [0,1,0,-1,1,-1,1,-1]

def breed():
    global total
    for i in range(1,N+1):
        for j in range(1,N+1):
            nutrition[i][j] += A[i][j]
            if area[i][j]:
                for k in area[i][j]:
                    if k%5==0:
                        for d in range(8):
                            nr = i+dr[d]
                            nc = j+dc[d]
                            if nr>N or nc>N or nr<1 or nc<1:continue
                            area[nr][nc] += [1]
                            total += 1

def feed():
    global total
    for i in range(1,N+1):
        for j in range(1,N+1):
            if area[i][j]:
                n_trees = 0
                area[i][j].sort()
                for k in range(len(area[i][j])):
                    if nutrition[i][j]<area[i][j][k]:
                        for k2 in range(k,len(area[i][j])):
                            nutrition[i][j] += area[i][j][k2]//2
                        area[i][j] = area[i][j][:k]
                        break
                    else:
                        nutrition[i][j] -= area[i][j][k]
                        area[i][j][k] += 1
                        n_trees += 1
                total += n_trees

N, M, K = map(int, input().split())
A = [[0]*(N+2)]
for _ in range(N):
    A += [[0]+list(map(int, input().split()))+[0]]
A.append([0]*(N+2))

nutrition = [[0]*(N+2)]
nutrition += [[0]+[5]*N+[0] for _ in range(N)] + [[0]*(N+2)]
area = [[[] for _ in range(N+2)] for _ in range(N+2)]

for _ in range(M):
    x,y,z = map(int, input().split())
    area[x][y] += [z]

for _ in range(K):
    total = 0
    feed()
    breed()
print(total)