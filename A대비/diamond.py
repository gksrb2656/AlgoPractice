T = int(input())
for t in range(1, T+1):
    word = input()
    n = len(word)-1
    N = 5*len(word)-n
    Dia = [['.'] * N for _ in range(5)]
    for i in range(5):
        for j in range(N):
            if i == 2:
                if j%4==0:
                    Dia[i][j] = '#'
                elif j%4==2:
                    Dia[i][j] = word[j//4]
            elif i%4 ==0:
                if j%4==2:
                    Dia[i][j] = '#'
            elif i%2:
                if j%2:
                    Dia[i][j] = '#'
    for d in Dia:
        print(''.join(d))