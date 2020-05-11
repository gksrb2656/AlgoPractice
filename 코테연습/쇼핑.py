# def solution(gems):
#     gems_unique = set(gems)
#     gems_dict = dict()
#     N = len(gems)
#     answer = [0, N]
#     ans_len = 0
#     cnt = 0
#     cnt2 = 0
#     for i in gems_unique:
#         gems_dict[i] = 0
#     st = 0
#     for i in range(N):
#         if gems_dict[gems[i]]==cnt2+1:
#             if gems[st] == gems[i]:
#                 st += 1
#             while gems[st] == gems[st+1]:
#                 st += 1
#         else:
#             gems_dict[gems[i]] = 1
#             cnt += 1
#         if cnt == len(gems_unique):
#             cnt = 0
#             cnt2+=1
#             if i-st<answer[1]-answer[0]:
#                 answer = [st+1,i+1]
#                 st = i - len(gems_unique)
#     return answer

# def solution(gems):
#     gems_unique = set(gems)
#     min_l = len(gems_unique)
#     max_l = N = len(gems)
#     answer = []
#
#     def gem_search(mid):
#         nonlocal answer
#         for i in range(0,N-mid+1):
#             flag = 1
#             for j in gems_unique:
#                 if j in gems[i:i+mid]:
#                     continue
#                 else:
#                     flag = 0
#                     break
#             if flag:
#                 answer = [i+1,i+mid]
#                 return 1
#
#
#     def B_search():
#         nonlocal min_l, max_l
#         while min_l <= max_l:
#             mid = (min_l + max_l) // 2
#             if gem_search(mid):
#                 max_l = mid-1
#             else:
#                 min_l = mid+1
#
#     B_search()
#     return answer
#
# def solution(gems):
#     gems_unique = set(gems)
#     unique_N = len(gems_unique)
#     min_l = len(gems_unique)
#     max_l = N = len(gems)
#     visit = [[] for _ in range(N)]
#     answer = []
#
#     def gem_search(mid, depth):
#         nonlocal answer
#         for i in range(0,N-mid+1):
#             if len(visit[i])>1:
#                 visit[i] = list(gems_unique - set(gems[i:i + mid]))
#                 continue
#             if depth >=1 and visit[i][0]==gems[i+mid-1]:
#                 answer = [i + 1, i + mid]
#                 return 1
#             elif not depth and unique_N == len(set(gems[i:i+mid])):
#                 answer = [i+1,i+mid]
#                 return 1
#             elif not depth:
#                 visit[i] = list(gems_unique - set(gems[i:i + mid]))
#
#
#     def B_search():
#         nonlocal min_l, max_l
#         # while min_l <= max_l:
#         #     mid = (min_l + max_l) // 2
#         #     if gem_search(mid):
#         #         max_l = mid-1
#         #     else:
#         #         min_l = mid+1
#         depth = 0
#         while 1:
#             if gem_search(min_l,depth):
#                 return 1
#             else:
#                 min_l += 1
#             depth += 1
#     B_search()
#     return answer

def solution(gems):
    st = ed = 0
    answer = [st+1,ed+1]
    gem_uniques = set(gems)
    ss = []
    ss.append(gems[st])
    if gem_uniques == set(gems[st:ed]):
        return answer
    else:
        flag = 0
        ed += 1
        ss.append(gems[ed])
        while ed<len(gems):
            if ss == gem_uniques:
                if not flag:
                    flag = 1
                    answer = [st+1,ed]
                    ss.remove(gems[st])
                    st += 1
                else:
                    if answer[1]-answer[0]>ed-st-1:
                        answer = [st+1,ed]
                        ss.remove(gems[st])
                        st+=1
            else:
                ed += 1
                ss.append(gems[ed])
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))