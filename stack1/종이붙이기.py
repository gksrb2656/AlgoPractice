



arr = [10,20]
# def dfs(H,G):
#     global cnt
#     for i in G:
#         if i == 20:
#             cnt2+=1
#         if H-i>0:
#             dfs(H-i, G)

def dfs(H,G, C=0):
    global cnt
    for i in G:
        if i == 20:
            C += 1
        if H-i>0:
            dfs(H-i, G, C)
        elif H - i == 0:
            cnt = cnt + 2**C


T = int(input())
for t in range(1,T+1):
    cnt = 0
    H = int(input())
    dfs(H,arr)
    print("#{} {}".format(t,cnt))