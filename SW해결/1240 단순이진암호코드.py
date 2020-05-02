P = {'0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9}

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    D = [input() for _ in range(N)]

    def scancode():
        # 암호코드의 첫번째 행의 끝위치를 찾아간다.
        for i in range(N):
            for j in range(M -1, -1, -1):
                if D[i][j] == '0':continue
                code = []
                for k in range(j - 56+1,j,7):# 각 패턴의 시작위치
                    code.append(P[D[i][k:k+7]])
                #암호코드 검증
                a = code[0]+ code[2] + code[4] + code[6]
                b = code[1]+ code[3] + code[5] + code[7]
                if (a*3 + b)%10: return 0
                return a+ b
    print('#{} {}'.format(t, scancode()))