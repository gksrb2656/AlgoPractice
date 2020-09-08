# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
#
# def dfs(v):
#     if check[v]:
#         return
#     if not check[prev_visit[v]]:
#         next_visit[prev_visit[v]] = v
#         return
#     check[v] = 1
#     if next_visit[v]:
#         dfs(next_visit[v])
#     for i in graph[v]:
#         dfs(i)
#
#
# def solution(n, path, order):
#     global N, graph, prev_visit, check, next_visit
#
#     N = n
#     start_room = 0
#     num_of_room = 0
#
#     # 그래프를 저장하는 배열
#     graph = [[] for _ in range(N)]
#     # 선방문해야 하는 방을 저장하는 배열, prev_visit[후방문방] = 선방문방
#     prev_visit = [0 for _ in range(N)]
#     # 그래프의 노드 방문여부를 저장하는 배열
#     check = [0 for _ in range(N)]
#     # 후방문해야 하는 방을 저장하는 배열, next_visit[선방문방] = 후방문방
#     next_visit = [0 for _ in range(N)]
#
#     for room_A, room_B in path:
#         graph[room_A].append(room_B)
#         graph[room_B].append(room_A)
#
#     for room_A, room_B in order:
#         prev_visit[room_B] = room_A
#
#     if prev_visit[start_room]:
#         return False
#
#     check[start_room] = 1
#     for i in graph[start_room]:
#         dfs(i)
#
#     for i in range(N):
#         if check[i]:
#             num_of_room += 1
#
#     return True if num_of_room == N else False
#
# solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])


import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def dfs(node):
    visited[node] = 1
    check2[node] = 1
    for next_node in dir_graph[node]:
        if not check2[next_node]:
            if dfs(next_node):
                return True
        if visited[next_node]:
            return True
    visited[node] = 0
    return False


def bfs():
    queue = deque([start_room])
    check[0] = 1
    dir_graph = [[] for _ in range(N + 1)]
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not check[n]:
                check[n] = 1
                dir_graph[node].append(n)
                queue.append(n)
    return dir_graph


def solution(n, path, order):
    global graph, dir_graph, check, check2, visited
    global N, start_room

    N = n
    start_room = 0
    # 그래프 저장 배열
    graph = [[] for _ in range(N + 1)]
    # 그래프의 노드 방문여부 저장 배열
    check = [0 for _ in range(N + 1)]
    # 방향그래프 탐색시 현재경로에 속한 노드를 나타내는 배열
    visited = [0 for _ in range(N + 1)]
    # 방향그래프의 노드 방문여부 저장 배열
    check2 = [0 for _ in range(N + 1)]

    for room_A, room_B in path:
        graph[room_A].append(room_B)
        graph[room_B].append(room_A)

    dir_graph = bfs()
    for room_A, room_B in order:
        dir_graph[room_A].append(room_B)

    check2[0] = 1
    visited[0] = 1
    is_cycle = dfs(start_room)

    return False if is_cycle else True