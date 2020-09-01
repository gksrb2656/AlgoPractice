def solution(num, cards):
    answer = 0
    dp = [10001]*(num+1)
    dp[0] = 0
    cards.sort()
    for i in range(len(cards)):
        for j in range(cards[i], num + 1):
            dp[j] = min(dp[j], dp[j - cards[i]] + 1)
    if dp[-1] == 10001:
        return -1
    return dp[-1]
print(solution(8,[1,4,6]))