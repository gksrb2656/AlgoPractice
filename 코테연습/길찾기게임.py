def solution(nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]):
    N = len(nodeinfo)
    node_back = [data[:] for data in nodeinfo]
    for i in range(N):
        nodeinfo[i][0], nodeinfo[i][1] = nodeinfo[i][1], nodeinfo[i][0]
        nodeinfo[i].append(i)
    nodeinfo.sort()
    fore = [nodeinfo[N-1][2]+1]
    idx = N-1
    stack = []
    while len(fore)<=N:
        y, x, n = nodeinfo[idx]
        if nodeinfo[idx-1][0] < y and nodeinfo[idx-1][1]>x:
            if nodeinfo[idx-1][2]+1 in fore:continue
            fore.append(nodeinfo[idx-1][2]+1)
        elif nodeinfo[idx-1][0]==y:
            if nodeinfo[idx-1][1]<x:
                if nodeinfo[idx - 1][2] + 1 in fore: continue
                stack.append(fore[-1])
                fore[-1] = nodeinfo[idx-1][2]+1
            else:
                stack.append(idx-1)
        if idx:
            idx -= 1
        else:
            for i in stack:
                fore.append(i+1)
    print(fore)
    answer = [[]]
    return answer

solution()