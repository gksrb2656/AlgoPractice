def DFS(depth, s):
    global ans
    if depth==10:
        ans = max(ans,s)
        return

    for i in range(4):
        flag = 0
        temp, temp_node = charic[i][0], charic[i][1]
        if charic[i][0]>20:continue
        if not charic[i][1]:
            flag = 0
            if charic[i][0] in (5,15):
                if dice[depth]>3:
                    charic[i][1], charic[i][0] = 3, dice[depth]-4
                elif charic[i][0] == 5:
                    charic[i][1], charic[i][0] = 1, dice[depth] - 1
                else:
                    charic[i][1], charic[i][0] = 4, dice[depth] - 1
            elif charic[i][0] == 10:
                if dice[depth]>2:
                    charic[i][1], charic[i][0] = 3, dice[depth]-3
                else:
                    charic[i][1], charic[i][0] = 2, dice[depth] - 1
            else:
                charic[i][0] += dice[depth]
        else:
            if charic[i][1] in (1,4):
                if 2<charic[i][0]+dice[depth]<6:
                    charic[i][1], charic[i][0] = 3, charic[i][0]+dice[depth] - 3
                elif 5<charic[i][0]+dice[depth]:
                    charic[i][1], charic[i][0] = 0, 20+charic[i][0]+dice[depth]-6
                else:
                    charic[i][0] += dice[depth]
            elif charic[i][1] == 2:
                if 1<charic[i][0]+dice[depth]<5:
                    charic[i][1], charic[i][0] = 3, charic[i][0]+dice[depth] - 2
                elif 4<charic[i][0]+dice[depth]:
                    charic[i][1], charic[i][0] = 0, 20+charic[i][0]+dice[depth]-5
                else:
                    charic[i][0] += dice[depth]
            else:
                if 2<charic[i][0] + dice[depth]:
                    charic[i][1], charic[i][0] = 0, 20 + charic[i][0] + dice[depth] - 3
                else:
                    charic[i][0] += dice[depth]

        if visit[charic[i][1]][charic[i][0]]:
            charic[i][0], charic[i][1] = temp, temp_node
            continue
        if charic[i][0]<21:
            visit[charic[i][1]][charic[i][0]] = 1
        visit[temp_node][temp] = 0
        DFS(depth+1, s+board[charic[i][1]][charic[i][0]])
        visit[temp_node][temp] = 1
        visit[charic[i][1]][charic[i][0]] = 0
        charic[i][0], charic[i][1] = temp, temp_node

dice = list(map(int, input().split()))
board = [[i for i in range(0,41,2)]+[0]*5, #normal
        [13,16,19], #10 >> index=5, node=1로
        [22,24], #20 >> index=10, node=2로
        [25,30,35], #25
        [28,27,26]] #30 >> index=15, node=4로

visit = [[0]*27,[0]*8,[0]*7,[0]*8,[0]*8]
charic = [[0,0] for _ in range(4)] # index, node
ans = 0
DFS(0,0)
print(ans)