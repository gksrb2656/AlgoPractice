def solution(numbers):
    answer = 0
    numbers = list(numbers)
    check = [0]*len(numbers)
    num_set = []
    def perm(k, n, s_s):
        nonlocal answer
        if k == n:
            if int(s_s) in num_set:
                return
            num_set.append(int(s_s))
            return

        for i in range(len(numbers)):
            if check[i]:continue
            check[i] = 1
            s_s += numbers[i]
            perm(k+1, n, s_s)
            s_s = s_s[:-1]
            check[i] = 0

    for i in range(1,len(numbers)+1):
        perm(0, i, '')

    for n in num_set:
        flag = 0
        if n < 2:
            continue
        for i in range(2,n):
            if not n%i and n!=2:
                flag = 1
                break
        if not flag:
            answer += 1

    return answer

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
