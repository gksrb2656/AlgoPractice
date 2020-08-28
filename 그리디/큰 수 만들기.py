def solution(number, k):
    answer = ''
    stack = [number[0]]
    for i in number[1:]:
        while len(stack)>0 and stack[-1]< i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


solution("1924", 2)