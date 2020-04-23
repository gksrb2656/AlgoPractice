for _ in range(int(input())):
    func = input()
    n_D = func.count('D')
    n_arr = int(input())
    arr = eval(input())
    if n_D>n_arr:
        print('error')
        continue
    flag = 0
    front = 0
    back = 0
    for f in func:
        if f == 'R':
            if flag:
                flag = 0
            else:
                flag = 1
        elif f == 'D':
            if flag:
                back += 1
            else:
                front += 1
    if flag:
        ans = arr[front:n_arr-back]
        ans.reverse()
        print(str(ans).replace(' ',''))
    else:
        ans = arr[front:n_arr-back]
        print(str(ans).replace(' ',''))


