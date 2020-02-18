def backtrack(v, cnt):
    global ans
    for i in range(N):
        if i not in visit1 and v-i not in visit2 and v+i not in visit3:
            cnt += 1
            if cnt-1 != v:
                return
            if cnt == N:
                ans += 1
            visit1.append(i)
            visit2.append(v-i)
            visit3.append(v+i)
            backtrack(v+1, cnt)
            visit1.pop()
            visit2.pop()
            visit3.pop()
            cnt -= 1
    return ans


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    ans = 0
    visit1 = []
    visit2 = []
    visit3 = []
    print('#{} {}'.format(t, backtrack(0,0)))