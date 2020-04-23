from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find_island(i,j,k):
    global ans # 전역변수에 답 저장
    Q = deque() # 섬 탐색을 위한 큐
    Q.append((i,j))
    Q2 = deque() # 섬과 바다 경계선을 담는 큐
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if nr>N-1 or nc>N-1 or nr<0 or nc<0 or arr[nr][nc]==k:continue # 배열을 벗어나거나 이미 체크한 영역일 경우 패스
            if not arr[nr][nc]:
                Q2.append((nr,nc,1))
                continue
            arr[nr][nc] = k # 섬 영역 체크
            Q.append((nr,nc))
    def bridge(n): # 짧은 다리 길이 탐색
        nonlocal Q2
        while Q2:
            r, c, dis = Q2.popleft() # 좌표 및 거리 큐에 저장
            if dis>=ans: # 거리가 지금까지 나온 가장 짧은 다리길이보다 같거나 길면 중단
                return ans
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr > N - 1 or nc > N - 1 or nr < 0 or nc < 0 or arr[nr][nc] == n or visit[nr][nc]: continue # 경로가 겹치는 경우는 최단 거리가 아니므로 방문한 영역은 넘기기.
                if not arr[nr][nc]: #바다 일 경우 큐에 추가
                    Q2.append((nr, nc, dis+1))
                    visit[nr][nc] = 1
                elif arr[nr][nc]: # 다른 섬일 경우 거리 반환
                    return dis
        return ans # 큐가 빈큐가 되도록 섬에 도착 못한 경우,(모두 방문)

    distance = bridge(k)
    if ans>distance:
        ans = distance

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
n_island = 1
ans = 100**2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            n_island += 1
            arr[i][j] = n_island
            find_island(i,j,n_island)

print(ans)