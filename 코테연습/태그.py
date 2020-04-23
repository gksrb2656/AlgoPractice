def solution(dataSource, tags):
    datas = {}
    for i in range(len(dataSource)):
        datas[dataSource[i][0]] = 0
        for j in range(1,len(dataSource[i])):
            if dataSource[i][j] in tags:
                datas[dataSource[i][0]] += 1
        if not datas[dataSource[i][0]]:
            datas.popitem()
    datas = sorted(datas.items(), key=lambda x: x[1], reverse=True)
    so_rt = []
    # for i in range(len(datas)-1):
    #     if datas[i][1] == datas[i+1][1]:
    #         if not so_rt:
    #             st = i
    #         so_rt.append(datas[i])
    #     else:
    #         if so_rt:
    #             so_rt.sort()
    #             datas = datas[:st] + so_rt + datas[i+1:]
    #             st = []
    answer = dict(datas).keys()
    return answer

solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "ta6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"])