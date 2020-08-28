def solution(array, commands):
    answer = []
    for c in commands:
        c_arr = array[c[0]-1:c[1]]
        c_arr.sort()
        answer.append(c_arr[c[2]-1])
    return answer