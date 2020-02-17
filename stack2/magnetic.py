for t in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1 and not stack:
                stack.append(1)
            elif arr[j][i] == 2 and stack:
                cnt += 1
                stack = []
    print("#{} {}".format(t,cnt))

