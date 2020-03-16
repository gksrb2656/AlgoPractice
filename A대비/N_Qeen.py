def backtrack(v, cnt):
    global ans
    for i in range(N):
        if visit1[i] or visit2[v-i] or visit3[v+i]: continue
        cnt += 1
        if cnt-1 != v:
            return

        if cnt == N:
            ans += 1
        visit1[i] = 1
        visit2[v-i]=1
        visit3[v+i]=1
        backtrack(v+1, cnt)
        visit1[i] = 0
        visit2[v-i] = 0
        visit3[v+i] = 0
        cnt -= 1
    return ans


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    ans = 0
    visit1 = [0]*N
    visit2 = [0]*2*N
    visit3 = [0]*2*N
    print(backtrack(0,0))
    print('#{} {}'.format(t, backtrack(0,0)))
