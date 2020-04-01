def solution(board, moves):
    doll = []
    answer = 0
    N = len(board)
    for i in moves:
        for r in range(N):
            if board[r][i-1]:
                if doll:
                    if doll[-1] == board[r][i-1]:
                        doll.pop()
                        answer += 2
                    else:
                        doll.append(board[r][i - 1])
                else:
                    doll.append(board[r][i-1])
                board[r][i-1] = 0
                break
    return answer