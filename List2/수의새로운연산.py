T = int(input())
dic = dict()
for i in range(200):
    if i == 0:
        dic[i + 1] = 1
    else:
        dic[i + 1] = dic[i] + i
# print(dic)
def find_point(p_q):
    for k, v in dic.items():
        if k < 200:
            if p_q == v:
                point = [k, 1]
                return point
            elif dic[k + 1] > p_q > dic[k]:
                point = [k - (p_q - dic[k]), (p_q - dic[k]) + 1]
                return point
for t in range(1, T+1):
    p, q = map(int, input().split())
    # print(p, q)
    p_point = find_point(p)
    q_point = find_point(q)
    # print(p_point,q_point)
    s1 = p_point[0] + q_point[0]
    s2 = p_point[1]+ q_point[1]
    # print(s1, s2)
    star = [s1, s2]
    star_n = dic[s1+(star[1] - 1)] + star[1] - 1
    print("#{} {}".format(t, star_n))