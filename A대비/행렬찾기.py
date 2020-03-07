def p_arr(r,c):
    size_r = 0
    size_c = 0
    nr= r
    nc = c
    while arr[nr][nc]:
        nr += 1
        size_r += 1
        if nr>N-1:
            break
    nr -= 1
    while arr[nr][nc]:
        visit[nr][nc] = 1
        nc += 1
        size_c += 1
        if nc>N-1:
            break
    nc -= 1
    for i in range(r,nr+1):
        for j in range(c,nc+1):
            visit[i][j] = 1
    return (size_r*size_c,size_r,size_c)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    p_s = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not visit[i][j]:
                p_s.append(p_arr(i,j))

    p_s.sort()
    print("#{} {}".format(t,len(p_s)), end = ' ')
    for a in p_s:
        print(a[1],a[2],end = ' ')
    print()