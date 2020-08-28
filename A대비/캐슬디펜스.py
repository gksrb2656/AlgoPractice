def kill(ar_1,ar_2,ar_3,depth,cnt): #매개변수로 궁수 1,2,3과 행 깊이, 잡을 수 있는 적 카운트
    global MAX # 가장 많은 적을 잡을 때 값 저장
    combo = [(N,ar_1),(N,ar_2),(N,ar_3)] # N행에 궁수들의 열 위치
    anemies = set() # 잡을 수 있는 적들
    while depth<=N:
        for k in combo:
            r, c = k #행, 열
            MIN_d = N**M #최소 거리 저장
            anemy = 0 #죽일 수 있는 적 명수 계산
            for i in range(N-depth,-1,-1): # 적들이 내려오는 대신 궁수들의 행 위치를 올리는 방식으로 범위를 지정
                if r-i>D+depth-1:break # 잡을 수 있는 사정거리를 벗어나면 브레이크
                for j in range(M):
                    if not arr_copy[i][j] or abs(r-i)+abs(c-j)>D+depth-1:continue # 적이 없는 좌표거나 사정거리를 벗어나면 넘기기
                    if abs(r-i)+abs(c-j)<MIN_d: # 적이 있는 좌표가 현재까지의 최소 거리보다 작으면 갱신
                        MIN_d = abs(r - i) + abs(c - j)
                        anemy = (i, j)
                    elif MIN_d == abs(r-i)+abs(c-j): # 그렇지 않고 같으면
                        if anemy[1]>j: # 더 왼쪽에 있으면 갱신
                            anemy = (i, j)
            if anemy: # 적이 존재하면
                anemies.add(anemy) # 잡을 수 있는 적 set에 추가
        for a in anemies:
            if arr_copy[a[0]][a[1]]: # 잡을 수 있는 적 카운트
                cnt += 1
                arr_copy[a[0]][a[1]] = 0
        depth+=1 # 궁수들 위치 한 행 올리기

    if cnt>MAX: # 잡은 적의 수가 최대값보다 크면 갱신
        MAX = cnt
        return

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
for i in range(M): # 궁수가 3명이므로 for문을 통해서 궁수 위치 조합 생성
    for j in range(i+1,M):
        for k in range(j+1,M):
            arr_copy = [data[:] for data in arr]
            kill(i,j,k,1,0)
print(MAX)
