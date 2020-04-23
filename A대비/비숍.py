# def bishop(possible,depth):
#     global ans,cnt
#     cnt+=1
#     if len(possible)<=ans-depth:
#         return
#
#     for i in range(len(possible)):
#         r,c = possible[i]
#         if R_visit[r-c] or L_visit[r+c]:continue
#         R_visit[r-c]=1
#         L_visit[r+c]=1
#         bishop(possible[i+1:],depth+1)
#         R_visit[r-c]=0
#         L_visit[r+c]=0
#     ans = max(depth, ans)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# R_visit = [0]*(2*N)
# L_visit = [0]*(2*N)
# possible = []
# ans = 0
# cnt = 0
# possible_w = []
# possible_b = []
# answer = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             if i%2 and j%2:
#                 possible_w.append((i,j))
#             elif not i%2 and not j%2:
#                 possible_w.append((i,j))
#             else:
#                 possible_b.append((i,j))
#
# bishop(possible_w,0)
# answer += ans
# ans = 0
# bishop(possible_b,0)
# answer += ans
# print(answer)
# print(cnt)
#

def bishop(n, depth, possible, total):
    global ans,cnt
    cnt += 1
    if total - n - 1 <= ans - depth:
        return

    for i in range(n, total):
        r, c = possible[i]
        if R_visit[r - c] or L_visit[r + c]: continue
        R_visit[r - c] = 1
        L_visit[r + c] = 1
        bishop(i + 1, depth + 1, possible, total)
        R_visit[r - c] = 0
        L_visit[r + c] = 0
    ans = max(ans, depth)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
odd_possible = []
even_possible = []
sum_ans = 0
even_total = 0
odd_total = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if i % 2 and j % 2:
                odd_possible.append((i, j))
                odd_total += 1
            elif not i % 2 and not j % 2:
                odd_possible.append((i, j))
                odd_total += 1
            else:
                even_possible.append((i, j))
                even_total += 1

R_visit = [0] * (2 * N)
L_visit = [0] * (2 * N)
ans = 0
cnt = 0
bishop(0, 0, even_possible, even_total)
sum_ans += ans
ans = 0
bishop(0, 0, odd_possible, odd_total)
sum_ans += ans
print(sum_ans)
print(cnt)