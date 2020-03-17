# import sys
# def DFS(v,K,visit,s_s):
#     global flag
#     global cnt
#     visit.append(v)
#     if v in s_s:
#         cnt += 1
#     if cnt == K:
#         flag = True
#         return
#     for j in range(1,N+1):
#         if arr[v][j] == 1 and j not in visit and j in s_s:
#             DFS(j,K,visit,s_s)
#
#
# def comb(k,n,K):
#     global cnt
#     global sub
#     global flag
#     if k == K:
#         for j in order:
#             cnt = 0
#             visit = []
#             flag = False
#             DFS(j,K,visit,order)
#             if flag:
#                 for l in li:
#                     cnt = 0
#                     flag = False
#                     DFS(l,N-K,visit,li)
#                     if flag:
#                         s1 = 0
#                         s2 = sum(people)
#                         c = order[:]
#                         for p in order:
#                             s1 += people[p-1]
#                         s2 -= s1
#                         if abs(s1-s2) < sub:
#                             sub = abs(s1-s2)
#                             break
#             if sub != sum(people):
#                 break
#     for i in range(n + 1, N + 1):
#         li.remove(i)
#         order.append(i)
#         comb(k+1,i, K)
#         order.pop()
#         li.append(i)
#
#
# N = int(input())
# people = list(map(int,input().split())) #구역은 인덱스로 접근
# graph = [list(map(int, input().split())) for _ in range(N)] #구역별 인접구역
# arr = [[0]*(N+1) for _ in range(N+1)]
# for i in range(N):
#     for j in range(1,graph[i][0]+1):
#         arr[i+1][graph[i][j]] = 1
# sub = sum(people)
# flag = False
# cnt = 0
# for i in range(N//2, N):
#     order = []
#     li =[j for j in range(1,N+1)]
#     comb(0,0,i)
#
# if sub<sum(people):
#     print(sub)
# else:
#     print(-1)
#
