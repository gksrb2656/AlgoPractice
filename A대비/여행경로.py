from collections import deque
def solution(tickets):
    answer = []
    check = [0]*len(tickets)
    def DFS(v,route,n,k):
        if n==k:
            answer.append(route[:])
        for t in range(len(tickets)):
            if tickets[t][0] == v:
                if check[t]:continue
                check[t] = 1
                route.append(tickets[t][1])
                DFS(route[-1],route,n,k+1)
                route.pop()
                check[t] = 0
    DFS('ICN',['ICN'],len(tickets),0)
    answer.sort()
    return answer[0]
solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])