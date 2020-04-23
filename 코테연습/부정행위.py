def solution(answer_sheet, sheets):
    answer = -1
    for i in range(len(sheets)):
        for i2 in range(i+1,len(sheets)):
            cnt = 0
            long_cnt = 0
            long = 0
            score = 0
            for j in range(len(answer_sheet)):
                if sheets[i][j] == sheets[i2][j] and sheets[i][j] != answer_sheet[j]:
                    cnt += 1
                    long_cnt += 1
                else:
                    long = max(long,long_cnt)
                    long_cnt = 0
            if long_cnt:
                long = max(long, long_cnt)
            score = cnt + long**2
            answer = max(answer,score)
        return answer

solution('24551', ['24553','24553'])