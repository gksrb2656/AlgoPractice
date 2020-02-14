# BFS로 미로 탈출 알고리즘 정의
def bfs(maze, i, j, N, M):
    visited = []  # 방문한 노드
    queue = [[i, j]]  # BFS로 사용될 큐
    distance = [[0 for _ in range(M)] for _ in range(N)]  # 해당 지점까지의 거리를 담는 리스트
    distance[0][0] = 1  # 첫 시작은 1

    while queue:
        [i, j] = queue.pop(0)  # BFS 큐에 넣어줌
        visited.append([i, j])  # 방문 리스트에 쌓아줌

        # 상하좌우 탐색
        if i < N - 1 and maze[i + 1][j] == 1 and [i + 1, j] not in visited and [i + 1, j] not in queue:
            queue.append([i + 1, j])
            distance[i + 1][j] = distance[i][j] + 1
        if j < M - 1 and maze[i][j + 1] == 1 and [i, j + 1] not in visited and [i, j + 1] not in queue:
            queue.append([i, j + 1])
            distance[i][j + 1] = distance[i][j] + 1
        if j > 0 and maze[i][j - 1] == 1 and [i, j - 1] not in visited and [i, j - 1] not in queue:
            queue.append([i, j - 1])
            distance[i][j - 1] = distance[i][j] + 1
        if i > 0 and maze[i - 1][j] == 1 and [i - 1, j] not in visited and [i - 1, j] not in queue:
            queue.append([i - 1, j])
            distance[i - 1][j] = distance[i][j] + 1

    return distance[N - 1][M - 1]  # 마지막 도착지의 거리를 반환


# Input담기
N, M = map(int, input().split())
maze = []
for _ in range(N):  # 미로를 2차원 배열로 받음
    maze.append(list(map(int, str(input()))))

# 정답 출력
print(bfs(maze, 0, 0, N, M))