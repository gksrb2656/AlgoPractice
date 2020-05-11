from itertools import permutations
def solution(expression):
    answer = 0
    numbers = []
    cal = set()
    num =''
    for i in expression:
        if i.isnumeric():
            num+= i
        else:
            numbers.append(int(num))
            numbers.append(i)
            cal.add(i)
            num =''
    numbers.append(int(num))
    cal = list(cal)
    cal_per = list(permutations(cal,len(cal)))
    for c in cal_per:
        num_c = numbers[:]
        for cc in c:
            flag = 0
            while not flag:
                for k in range(len(num_c)):
                    if cc == num_c[k]:
                        if cc == '+':
                            num_c[k+1] = num_c[k-1] + num_c[k+1]
                            num_c = num_c[:k-1]+num_c[k+1:]
                            flag = 1
                            break
                        elif cc == '*':
                            num_c[k+1] = num_c[k-1] * num_c[k+1]
                            num_c = num_c[:k-1]+num_c[k+1:]
                            flag = 1
                            break
                        elif cc == '-':
                            num_c[k+1] = num_c[k-1] - num_c[k+1]
                            num_c = num_c[:k-1]+num_c[k+1:]
                            flag = 1
                            break
                if flag:
                    flag = 0
                else:
                    flag = 1
        answer = max(answer,abs(sum(num_c)))
    return answer

solution("100-200*300-500+20")