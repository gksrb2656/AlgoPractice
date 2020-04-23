def solution(s):
    tuples = []
    li = []
    flag1 = 0
    flag2 = 0
    nums = ''
    answer = []
    for i in s:
        if i == '{' and not flag1:
                flag1 = 1
        elif i == '{':
            flag2 = 1
        elif i == ',':
            if flag2:
                li.append(int(nums))
                nums = ''
        elif i == '}':
            if flag2:
                if nums !='':
                    li.append(int(nums))
                    nums = ''
                flag2 = 0
                tuples.append(list(li[:]))
                li = []
        else:
            nums += i
    N = len(tuples)
    for i in range(N):
        for j in tuples:
            if len(j) == i+1:
                for jj in j:
                    if jj in answer:continue
                    answer.append(jj)
    return answer
