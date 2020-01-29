# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for i in range(T):
    cnt = 0
    K, N, M = map(int, input().split())
    nxt = K
    charge = list(map(int, input().split())) # 충소 리스트로 받기
    for j in range(M):
        if charge[j] == nxt: # 충전소와 최대로 갈 수 있는 거리가 동일할 때
            nxt += K    # nxt 업데이트
            cnt += 1    # 카운트 누적
        elif charge[j] > nxt: #충전소가 최대로 갈 수 있는 거리보다 멀리 있을 때
            if charge[j-1]+K < charge[j]: # 그 전 충전소에서 충전해서 다음 충전소까지 갈 수 있는지 확인
                cnt = 0                  # 갈 수 없다면 0으로 출력
                break
            else:
                nxt = charge[j-1]+K    # 갈 수 있다면 그 전 충전소에서 최대로 갈 수 있는 거리를 nxt로 업데이트
                cnt += 1 # 카운트 누적
        if j == M-1:    # for문이 마지막 충전소 일 때
            if nxt < N: # 그 전까지 충전소에서 충전한 양으로 마지막 정류소까지 도달하지 못했을 때
                if (charge[j] + K) >= N: # 마지막 충전소에서 충전하여 마지막 정류소까지 갈 수 있는 지 확인
                    cnt += 1  # 갈 수 있다면 카운트 누적
                else:
                    cnt = 0   # 갈 수 없다면 카운트 0으로 출력
    print("#{0} {1}".format(i+1, cnt))
