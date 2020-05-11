def solution(numbers, hand):
    answer = ''
    L_point = (3,0)
    R_point = (3,2)
    for i in numbers:
        if i in (1,4,7):
            answer += 'L'
            L_point = ((i-1)//3,(i-1)%3)
        elif i in (3,6,9):
            answer += 'R'
            R_point = ((i-1)//3,(i-1)%3)
        elif i in (2,5,8):
            r, c = (i - 1) // 3, (i - 1) % 3
            lr, lc = L_point
            rr, rc = R_point
            if abs(lr-r)+abs(lc-c) == abs(rr-r)+abs(rc-c):
                if hand == 'right':
                    answer += 'R'
                    R_point = (r,c)
                else:
                    answer += 'L'
                    L_point = (r,c)
            elif abs(lr-r)+abs(lc-c) < abs(rr-r)+abs(rc-c):
                answer += 'L'
                L_point = (r,c)
            else:
                answer += 'R'
                R_point = (r,c)
        else:
            r, c = (3,1)
            lr, lc = L_point
            rr, rc = R_point
            if abs(lr-r)+abs(lc-c) == abs(rr-r)+abs(rc-c):
                if hand == 'right':
                    answer += 'R'
                    R_point = (r,c)
                else:
                    answer += 'L'
                    L_point = (r,c)
            elif abs(lr-r)+abs(lc-c) < abs(rr-r)+abs(rc-c):
                answer += 'L'
                L_point = (r,c)
            else:
                answer += 'R'
                R_point = (r,c)
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left'))