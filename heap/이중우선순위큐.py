def solution(operations):
    answer = []
    for o in operations:
        order, num = o.split()
        if order == "I":
            answer.append(int(num))
        if order == "D":
            if int(num)==1:
                if answer:
                    answer.remove(max(answer))
            else:
                if answer:
                    answer.remove(min(answer))
    if not answer:
        return [0,0]
    return [max(answer),min(answer)]

solution(["I 16","D 1"])