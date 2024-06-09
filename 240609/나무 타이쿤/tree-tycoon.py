N,M = map(int,input().split())

board = []
for i in range(N) : 
    board.append(list(map(int,input().split())))

move_year = []
for i in range(M) :
    move_year.append(tuple(map(int,input().split())))

## 8방향 : 동 동북 북 북서 서 서남 남 남동
dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

dx_2 = [-1,-1,1,1]
dy_2 = [-1,1,-1,1]

## 특수 영양제
nut = []
### 초기 특수 영양제는 좌하단 4개의 칸에 주어집니다.
nut.append((N-1,0))
nut.append((N-1,1))
nut.append((N-2,0))
nut.append((N-2,1))

## 1단계 : 특수 영양제를 이동 규칙에 따라 이동시킵니다.

for direction,distance in move_year :

    ## 특수 영양제 이동
    new_nut = []
    next_nut = []
    for x_n,y_n in nut :
        s_x = ( x_n + (dx[direction-1] * distance) ) % N
        s_y = ( y_n + (dy[direction-1] * distance) ) % N

        new_nut.append((s_x,s_y))
    
    ## 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
    for x_grow,y_grow in new_nut :
        board[x_grow][y_grow] += 1
    
    ## 특수 영양제가 있는 땅의 리브로스는 "대각선"으로 인접한 높이 1이상 리브로수의 개수 만큼 높이가 증가
    for x_grow,y_grow in new_nut :
        chk = 0

        for d in range(4) :
            nx = x_grow + dx_2[d]
            ny = y_grow + dy_2[d]

            if 0 <= nx < N and 0 <= ny < N :
                if board[nx][ny] >= 1 :
                    chk += 1
        #print(x_grow,y_grow,chk)
        board[x_grow][y_grow] += chk

    for i in range(N) :
        for j in range(N) :
            if (i,j) in new_nut :
                continue
            else :
                if board[i][j] >= 2 :
                    board[i][j] -= 2
                    next_nut.append((i,j))
    nut = next_nut
    #for g in range(N) :
    #    print(board[g])
    #print('----------')

answer = 0
for q in range(N) :
    for w in range(N) :
        answer += board[q][w]

print(answer)