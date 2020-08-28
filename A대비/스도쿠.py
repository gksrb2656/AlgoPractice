def possible(idx):
    check = set()
    pos = []
    global flag
    if flag: return
    for b in range(idx,len(blank)):
        i,j = blank[b]
        if arr[i][j]: continue
        for r in range(9):
            if arr[r][j]:
                check.add(arr[r][j])
        for c in range(9):
            if arr[i][c]:
                check.add(arr[i][c])
        R, C = i // 3, j // 3
        for r in range(R * 3, (R + 1) * 3):
            for c in range(C * 3, (C + 1) * 3):
                if arr[r][c]:
                    check.add(arr[r][c])
        pos = check_ori - check
        for p in pos:
            arr[i][j] = p
            possible(b + 1)
            arr[i][j] = 0
        return
    if flag: return
    for a in arr:
        print(*a)
    flag = 1


arr = [list(map(int, input().split())) for _ in range(9)]
check_ori = {1, 2, 3, 4, 5, 6, 7, 8, 9}
blank = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            blank.append((i,j))
flag = 0
possible(0)
