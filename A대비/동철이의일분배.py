# def combe(k,per):
#     global ans
#     if k == N:
#         if per > ans:
#             ans = per
#         return
#     for i in range(N):
#         if per<=ans:
#             return
#         if not visit[i]:
#             if ans>=percentages[k][i]:continue
#             per_copy = per
#             visit[i] = 1
#             per *= percentages[k][i]
#             combe(k+1,per)
#             per = per_copy
#             visit[i] = 0
#
# def divide(x):
#     return x/100
#
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     percentages = [list(map(divide, map(int,input().split())))for _ in range(N)]
#     visit = [0]*N
#     ans = 0
#     combe(0,1)
#     print("#%d %.6f" %(t, ans*100))

def combe(k,per):
    global ans
    if k == N:
        if per > ans:
            ans = per
        return
    if per <= ans:
        return
    for i in range(N):
        if not visit[i]:
            if ans>=percentages[k][i]:continue
            per_copy = per
            visit[i] = 1
            per *= percentages[k][i]
            combe(k+1,per)
            per = per_copy
            visit[i] = 0

def divide(x):
    return x/100

T = int(input())
for t in range(1,T+1):
    N = int(input())
    percentages = [list(map(divide, map(int,input().split())))for _ in range(N)]
    visit = [0]*N
    ans = 0
    combe(0,1)
    print("#%d %.6f" %(t, ans*100))