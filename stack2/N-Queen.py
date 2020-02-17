dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]
dr = [1, 1, -1, -1]
dc = [1, -1, 1, -1]

def backtrack(v, visit1, visit2, cnt):
    for i in range(N):
        if i not in visit1 and (v-i) not in visit2:
            visit1.append(i)
            visit2.append(v-i)
            cnt += 1
            backtrack(v+1, visit1, visit2, cnt)
            visit1.pop()
            visit2.pop()
            cnt -= 1
    if v == N:
        print(visit1, visit2)
        global ans
        if cnt == N:
            ans += 1
            return

T = int(input())
for t in range(1, T+1):
    ans = 0
    N = int(input())
    visit1=[]
    visit2=[]
    backtrack(0, [], [], 0)
    print(ans)