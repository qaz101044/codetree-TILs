# N = 격자 크기
# M = 박멸이 진행되는 년 수
# K = 제초제의 확산 범위
# C = 제초제가 남아있는 년수
N,M,K,C = map(int,input().split())

board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

killer = [[-1 for j in range(N)] for i in range(N)]

## 4방향 정의 : 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

## 4대각선 정의 : 11시/01시/05시/07시
dx_2 = [-1,-1,1,1]
dy_2 = [-1,1,1,-1]

answer = 0
## 박멸이 진행되는 년수 만큼 반복
for i in range(M) :

    ### 제초제 년수 갱신
    for idx in range(N) :
        for jdx in range(N) :
            if killer[idx][jdx] != -1 :
                killer[idx][jdx] += 1
                if killer[idx][jdx] > C :
                    killer[idx][jdx] = -1

    ### 1 단계 : 나무 성장 : ok
    for idx in range(N) :
        for jdx in range(N) :
            if board[idx][jdx] >= 1 :
                cnt_growth = 0
                for k in range(4) :
                    nx = idx + dx[k]
                    ny = jdx + dy[k]

                    if 0 <= nx < N and 0 <= ny < N :
                        if board[nx][ny] >= 1 :
                            cnt_growth += 1

                board[idx][jdx] += cnt_growth

    ### 2 단계 : 나무 번식 : ok
    new_tree_board = [[0 for j in range(N)] for i in range(N)]

    for idx in range(N) :
        for jdx in range(N) :
            if board[idx][jdx] >= 1 :
                temp = []
                cnt = 0

                for k in range(4) :
                    gx = idx + dx[k]
                    gy = jdx + dy[k]

                    if 0 <= gx < N and 0 <= gy < N :
                        if board[gx][gy] == 0 and killer[gx][gy] == -1 :
                            temp.append((gx,gy))
                            cnt += 1

                if len(temp) >= 1 :
                    for t_x,t_y in temp :
                        new_tree_board[t_x][t_y] += (board[idx][jdx] // cnt)

    for idx in range(N) :
        for jdx in range(N) :
            if new_tree_board[idx][jdx] >= 1 :
                board[idx][jdx] = new_tree_board[idx][jdx]

    ### 3 단계 : 제초제 뿌리기

    #### 제초제 뿌릴 칸 선정
    kill_x = -1
    kill_y = -1
    kill_tree = -987654321
    kill_cell = []

    for idx in range(N) :
        for jdx in range(N) :

            if board[idx][jdx] >= 1 :
                temp_cell = []
                temp_value = board[idx][jdx]

                s_x = idx
                s_y = jdx

                ## 11 / 01 / 05 / 07
                chk_arr = [0,0,0,0]
                temp_cell.append((idx,jdx))

                for p in range(K) :

                    for kdx in range(4) :
                        kx = s_x + (dx_2[kdx] * (p+1))
                        ky = s_y + (dy_2[kdx] * (p+1))

                        if 0 <= kx < N and 0 <= ky < N  and chk_arr[kdx] == 0 :
                            if board[kx][ky] == 0 or board[kx][ky] == -1 :
                                chk_arr[kdx] = 1
                                temp_cell.append((kx,ky))
                            else :
                                temp_value += board[kx][ky]
                                temp_cell.append((kx,ky))

                ## 박멸 시키는 나무 수가 똑같은 경우 : 행이 작은 칸 먼저 = > 행 같으면 열이 작은 칸
                if kill_tree == temp_value :
                    if s_x < kill_x :
                        kill_x = s_x
                        kill_y = s_y
                        kill_cell = temp_cell
                    elif s_x == kill_x :
                        if s_y < kill_y :
                            kill_x = s_x
                            kill_y = s_y
                            kill_cell = temp_cell

                elif kill_tree < temp_value :
                    kill_x = s_x
                    kill_y = s_y
                    kill_tree = temp_value
                    kill_cell = temp_cell

    kill_cell.sort(key=lambda x:(x[0],x[1]))

    for x,y in kill_cell :
        killer[x][y] = 0
        if board[x][y] >= 1 :
            board[x][y] = 0

    answer += kill_tree

print(answer)