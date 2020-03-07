# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# cards.sort()
# sub = M
# sum_cards = 0
# for i in range(N):
#     for j in range(i+1,N):
#         if cards[i] + cards[j] >= M:
#             continue
#         for k in range(j+1,N):
#             if M - cards[i] - cards[j] - cards[k] >= 0:
#                 if M - cards[i] - cards[j] - cards[k] <= sub:
#                     sub = M - cards[i] - cards[j] - cards[k]
#                     sum_cards = cards[i] + cards[j] + cards[k]
# print(sum_cards)

def blackjack(k,n,SUM):
    global Max
    if k==3:
        if SUM<=M:
            if SUM>Max:
                Max=SUM
        return
    for i in range(n,N):
        SUM += card[i]
        blackjack(k+1,i+1,SUM)
        SUM -= card[i]

N,M=map(int,input().split())
card=list(map(int,input().split()))
Max=0
blackjack(0,0,0)
print(Max)