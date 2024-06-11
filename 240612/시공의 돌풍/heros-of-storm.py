from collections import deque

N,M,T = map(int,input().split())

board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

## 4 방향 정의 : 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

## 시공의 돌풍 위치 찾기
tornado_arr = []

for i in range(N) :
    for j in range(M) :
        if board[i][j] == -1 :
            tornado_arr.append((i,j))

tornado_arr.sort(key=lambda x: x[0])

x_up = tornado_arr[0][0]
y_up = tornado_arr[0][1]

x_down = tornado_arr[1][0]
y_down = tornado_arr[1][1]

answer = 0
## T초 동안 움직임
for i in range(T) :
    temp_board = [[0 for j in range(M)] for i in range(N)]

    for idx in range(N) :
        for jdx in range(M) :

            if board[idx][jdx] == -1 :
                continue

            for d in range(4) :
                nx = idx + dx[d]
                ny = jdx + dy[d]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != -1 :
                    dust_temp = (board[idx][jdx] // 5)
                    temp_board[nx][ny] += dust_temp
                    temp_board[idx][jdx] -= dust_temp
    
    ## 모든 먼지 확산 끝난 후 연산
    for idx in range(N) :
        for jdx in range(M) :
            board[idx][jdx] += temp_board[idx][jdx]


    ## 시공의 돌풍 작동
    ### 시공의 돌풍 - 위쪽, 반시계 방향
    d_1 = 1
    q_1 = deque()
    q_1.append((x_up,y_up))
    up_board = [[-5 for j in range(M)] for i in range(N)]

    while q_1 :

        x_1,y_1 = q_1.popleft()

        nx_1 = x_1 + dx[d_1]
        ny_1 = y_1 + dy[d_1]

        if 0 <= nx_1 < N and 0 <= ny_1 < M :
            if board[nx_1][ny_1] == -1 :
                break
            else :
                if board[x_1][y_1] == -1 :
                    up_board[nx_1][ny_1] = 0
                    q_1.append((nx_1,ny_1))
                else :
                    up_board[nx_1][ny_1] = board[x_1][y_1]
                    q_1.append((nx_1,ny_1))
        else :
            d_1 -= 1
            if d_1 < 0 :
                d_1 += 4
            
            nx_1 = x_1 + dx[d_1]
            ny_1 = y_1 + dy[d_1]

            if board[nx_1][ny_1] == -1 :
                break
            else :
                up_board[nx_1][ny_1] = board[x_1][y_1]
                q_1.append((nx_1,ny_1))        
    
    for idx in range(N) :
        for jdx in range(M) :
            if up_board[idx][jdx] >= 0 :
                board[idx][jdx] = up_board[idx][jdx]
    
    ### 시공의 돌풍 - 아래쪽, 시계 방향
    d_2 = 1
    q_2 = deque()
    q_2.append((x_down,y_down))
    down_board = [[-6 for j in range(M)] for i in range(N)]
    
    while q_2 :

        x_2, y_2 = q_2.popleft()

        nx_2 = x_2 + dx[d_2]
        ny_2 = y_2 + dy[d_2]

        if 0 <= nx_2 < N and 0 <= ny_2 < M :
            if board[nx_2][ny_2] == -1 :
                break
            else :
                if board[x_2][y_2] == -1 :
                    down_board[nx_2][ny_2] = 0
                    q_2.append((nx_2,ny_2))
                else :
                    down_board[nx_2][ny_2] = board[x_2][y_2]
                    q_2.append((nx_2,ny_2))
        
        else :
            d_2 += 1
            if d_2 >= 4 :
                d_2 = d_2%4
            
            nx_2 = x_2 + dx[d_2]
            ny_2 = y_2 + dy[d_2]
            
            if board[nx_2][ny_2] == -1 :
                break
            else :
                down_board[nx_2][ny_2] = board[x_2][y_2]
                q_2.append((nx_2,ny_2))
    
    for idx in range(N) :
        for jdx in range(M) :
            if down_board[idx][jdx] >= 0 :
                board[idx][jdx] = down_board[idx][jdx]

answer = 0

for i in range(N) :
    for j in range(M) :
        if board[i][j] == -1 :
            continue
        else :
            answer += board[i][j]

print(answer)