#
# def dfs(visited, S, G):
#     if G in visited:
#         global ans
#         ans = 1
#         return
#     for i in range(1, V + 1):
#         if arr[S][i] == 1 and i not in visited:
#             visited.append(i)
#             dfs(visited, i, G)

# T = int(input())
# for t in range(1,T+1):
#     ans = 0
#     V, E = map(int, input().split())
#
#     arr = [[0] * (V + 1) for _ in range(V + 1)]
#
#     for i in range(E):
#         st, ed = map(int, input().split())
#         arr[st][ed] = 1
#
#     S, G = map(int, input().split())
#
#     dfs([S], S, G)
#     print("#{} {}".format(t, ans))



def dfs(S,G):
    global ans
    if S == G:
        ans = 1
        return

    for i in arr:
        if i[0] == S:
            dfs(i[1],G)

T = int(input())
for t in range(1,T+1):
    ans = 0
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    dfs(S,G)
    print("#{} {}".format(t, ans))

