def solution(dirs):
    # arr = [[0]*10 for _ in range(10)]
    visit = [[0]*20 for _ in range(20)]
    r,c = 5,5
    cnt = 0
    for d in dirs:
        if d=='U':
            if r-1<0:continue
            if not visit[2*r-1][2*c]:
                cnt += 1
                visit[2*r-1][2*c] = 1
            r -= 1
        elif d=='D':
            if r+1>10:continue
            if not visit[2*r+1][2*c]:
                cnt += 1
                visit[2*r+1][2*c] = 1
            r+=1
        elif d=='R':
            if c+1>10:continue
            if not visit[2*r][2*c+1]:
                visit[2*r][2*c+1] = 1
                cnt+=1
            c+=1
        elif d=='L':
            if c-1<0:continue
            if not visit[2*r][2*c-1]:
                visit[2*r][2*c-1] = 1
                cnt+=1
            c-=1
    return cnt

print(solution("ULURRDLLU"))