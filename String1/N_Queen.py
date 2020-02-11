# from collections import deque
# def Queen(s, v, rule):
#     rule.append(v)
#     visit.append(s)
#     while 1:
#         # r, c = Q.popleft()
#         for i in range(r+1, N):
#             for j in range(N):
#                 d1 = i+j
#                 d2 = i-j
#                 if (i, j, d1, d2) not in visit:
#                     Queen(s, v, )
#                     visit.append((i, j, d1, d2))
#
# # dr = [1,2,1,2,-1,-2,-1,-2]
# # dc = [2,1,-2,-1,2,1,-2,-1]
# #
# # def Queen():
#
# T = int(input())
# for i in range(1, T+1):
#     N = int(input())
#     for r in range(N):
#         for c in range(N):
#             d1 = r+c
#             d2 = r-c
#             rule = (r, c, d1, d2)
#             visit = []
T = int(input())
for t in range(1, T+1):
    N, C = map(int, input().split())
    N = list(str(N))
    cnt = 0
    m_cnt = 0
    idx = 0
    idx_li = []
    Max ='0'
    Min = '9'
    cnt2 = 0
    num = 0
    while num < C and cnt<len(N)-1:
        for i in range(cnt,len(N)):
            if N[i]>=Max:
                Max = N[i]
                Max_idx = i
        if cnt == len(N)-1:
                break
        idx_li.append(Max_idx)
        for i in range(cnt, len(N)):
            if N[cnt] == Max:
                cnt += 1
                Max = '0'
                break
            elif N[i] != Max:
                N[i], N[Max_idx] = N[Max_idx], N[i]
                cnt += 1
                num += 1
                Max = '0'
                break
    k = len(idx_li)
    while cnt2 < N.count(max(N))-1:
        if N[idx_li[0]] > N[idx_li[k-1]]:
            N[idx_li[0]],N[idx_li[k-1]] = N[idx_li[k-1]],N[idx_li[0]]
            k -= 1
        cnt2+=1
    if (C-num)%2 and N.count(max(N))<C-1:
        N[-1],N[-2] = N[-2],N[-1]
    print("#{} {}".format(t, ''.join(N)))