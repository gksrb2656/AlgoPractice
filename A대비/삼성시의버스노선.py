T = int(input())
for t in range(1,T+1):
    N = int(input())
    node = []
    station = []
    for n in range(N):
        node.append(list(map(int, input().split())))
    station_n = int(input())
    answer = [0]*station_n
    for s in range(station_n):
        station.append(int(input()))

    for s in range(len(station)):
        for n in node:
            if n[0] <= station[s] <=n[1]:
                answer[s] += 1

    print("#{}".format(t),*answer)