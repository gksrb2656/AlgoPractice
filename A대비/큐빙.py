UD = ['F', 'R', 'B', 'L']
FB = ['L', 'U', 'R', 'D']
LR = ['U', 'F', 'D', 'B']

def right(pan):
    ret = [[0] * 3 for _ in range(3)]

    for r in range(3):
        for c in range(3):
            ret[c][2 - r] = pan[r][c]
    return ret


def left(pan):
    ret = [[0] * 3 for _ in range(3)]

    for r in range(3):
        for c in range(3):
            ret[2 - c][r] = pan[r][c]
    return ret


for t in range(int(input())):
    cube = {'U': [['w'] * 3 for _ in range(3)],
            'D': [['y'] * 3 for _ in range(3)],
            'F': [['r'] * 3 for _ in range(3)],
            'B': [['o'] * 3 for _ in range(3)],
            'L': [['g'] * 3 for _ in range(3)],
            'R': [['b'] * 3 for _ in range(3)]}
    n = int(input())
    command = list(input().split())



