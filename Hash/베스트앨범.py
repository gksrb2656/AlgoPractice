# def solution(genres, plays):
#     answer = []
#     music_n = len(genres)
#     Dic = {}
#     for i in range(music_n):
#         if genres[i] in Dic:
#             Dic[genres[i]] += [plays[i]]
#         else:
#             Dic[genres[i]] = [plays[i]]
#     for key in Dic:
#         li = Dic[key]
#         Dic[key] = sorted(li, reverse=True)
#     sDic = sorted(Dic.items(), key=lambda item: sum(item[1]), reverse=True)
#     plays_Dic = {}
#     for i in range(music_n):
#         if plays[i] in plays_Dic:
#             plays_Dic[plays[i]] += [i]
#         else:
#             plays_Dic[plays[i]] = [i]
#     for key in plays_Dic:
#         li = plays_Dic[key]
#         plays_Dic[key] = sorted(li)
#
#     for g, num in sDic:
#         check = 0
#         for n in num:
#             for p_n in plays_Dic[n]:
#                 if g == genres[p_n]:
#                     answer.append(p_n)
#                     check += 1
#             if check == 2:
#                 break
#     return print(answer)

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])