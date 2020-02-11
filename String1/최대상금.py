T = int(input())


def get_result(num):
    if num == int(count):
        global result
        if result < int(''.join(t_c)):
            result = int(''.join(t_c))
            return
    elif num > int(count):
        pass

    else:
        for i in range(len(t_c)):
            for j in range(i, len(t_c)):
                if i == j:
                    continue

                t_c[i], t_c[j] = t_c[j], t_c[i]
                print(check)
                if [int(''.join(t_c)), num] not in check:
                    check.append([int(''.join(t_c)), num])
                    get_result(num + 1)
                t_c[i], t_c[j] = t_c[j], t_c[i]


for t in range(1, T + 1):
    t_c, count = input().split()
    t_c = list(t_c)
    check = []
    result = 0
    get_result(0)
    print(result)