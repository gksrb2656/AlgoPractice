# def DFS(p,s_v,b):
#     global MIN
#     if MIN<s_v:
#         return
#
#     if p<=0:
#         if MIN>s_v:
#             MIN = s_v
#         return
#
#     if b>0:
#         DFS(p-B,s_v+1,b-1)
#     elif p//C>0:
#         DFS(p%C,s_v+p//C,b)
#     else:
#         DFS(p-C,s_v+1,b)

# N = int(input())
# A = list(map(int, input().split()))
# B, C = map(int, input().split())
# ans = 0
# for i in A:
#     MIN = i
#     DFS(i,0,1)
#     ans += MIN
# print(ans)

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for i in A:
    n_sum = 1
    k = i-B
    if k>0:
        if k%C:
            n_sum += k//C + 1
        else:
            n_sum += k//C
    ans += n_sum
print(ans)