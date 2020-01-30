T = int(input())
for i in range(1, T+1):
    P, A, B = map(int, input().split())
    l_a=l_b = 1
    r_a=r_b = P
    c_a =c_b= int((1+P)/2)
    a_cnt = 1
    b_cnt = 1
    while c_a != A:
        if A in range(l_a,c_a):
            r_a = c_a
            a_cnt += 1
            c_a = int((l_a+r_a)/2)
        else:
            l_a = c_a
            a_cnt += 1
            c_a = int((l_a+r_a)/2)
    while c_b != B:
        if B in range(l_b,c_b):
            r_b = c_b
            b_cnt += 1
            c_b = int((l_b+r_b)/2)
        else:
            l_b = c_b
            b_cnt += 1
            c_b = int((l_b+r_b)/2)
    if a_cnt == b_cnt:
        print('#{0} 0'.format(i))
    elif a_cnt > b_cnt:
        print('#{0} B'.format(i))
    else:
        print('#{0} A'.format(i))