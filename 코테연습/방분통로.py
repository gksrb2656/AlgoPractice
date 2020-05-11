from collections import deque

def solution(n, path, order):
    path_re = [[]*n]
    visit = [0]*n
    visit[0] = 1
    order_dict=dict()
    order_check = dict()
    for i in order:
        order_dict[i[1]] = i[0]
        order_check[i[0]] = 0
    Q = deque()
    Q.append(0)
    for i in path:
        path_re[i[0]].append(i[1])
        path_re[i[1]].append(i[0])
        while Q:
            v = Q.popleft()
            for p in path_re[v]:
                if p in order_dict:
                    if not order_check[order_dict[p]]: continue

    answer = True
    return answer