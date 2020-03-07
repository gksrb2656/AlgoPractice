dir = [(1,0),(0,1)] # 행 검사, 열 검사 구분

def contruct(r,c,d):
    road_cnt = 0
    for i in range(N):
        nr = r + dir[d][0]*i # 행 또는 열 바꿈
        nc = c + dir[d][1]*i
        cnt = 1 # 활주로 길이 계산
        flag = True # 활주로 높이 체크
        for j in range(N-1):
            nr2 = nr + dir[d][1]*j # 현재 위치
            nc2 =  nc + dir[d][0]*j
            nr2_1 = nr + dir[d][1]*(j+1) # 다음 위치
            nc2_1 =  nc + dir[d][0]*(j+1)
            if flag and cliff[nr2][nc2] != cliff[nr2_1][nc2_1]: # 다르면 체크
                flag = False
                if cliff[nr2][nc2] - cliff[nr2_1][nc2_1] ==1: # 현재 위치가 더 높으면 활주로 길이 초기화
                    cnt = 0
                elif cliff[nr2][nc2] - cliff[nr2_1][nc2_1] ==-1 and cnt >= X: # 현재 위치가 더 낮으면 구조물 설치 가능성 확인
                    cnt = 0
                    flag = True
                else:                                            # 활주로 높이 차가 1 이상이면 행 또는 열 바꿈
                    break
            elif not flag and cliff[nr2][nc2] != cliff[nr2_1][nc2_1]: # 높이 변화가 있었을 경우 구조물 설치 없이 높이 변화 생기면 행 또는 열 바꿈
                break
            cnt += 1                                             # 활주로 길이 추가
            if not flag and cnt >= X:                            # 높이 변화가 있었을 경우 구조물 설치 가능성 확인
                flag = True                                      # 가능하면 높이 변화 체크 초기화
                cnt -= X                                         # 구조물 길이 만큼 활주로 길이 빼주기
            if j+1 == N-1 and flag:                              # 절벽의 끝까지 높이 변화 커버 가능한 경우 활주로 구역 1 추가
                road_cnt += 1
    return road_cnt
T =  int(input())
for t in range(1,T+1):
    N, X = map(int, input().split())
    cliff = [list(map(int,input().split())) for _ in range(N)]
    print("#{} {}".format(t,contruct(0,0,0)+contruct(0, 0, 1)))