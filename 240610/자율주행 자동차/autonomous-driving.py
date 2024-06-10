from collections import deque

N,M = map(int,input().split())

## 4방향 정의 : 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

## 자율 주행 자동차 초기 조건
x, y, d = map(int,input().split())

board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

visited = [[0 for j in range(M)] for i in range(N)]

visited[x][y] = 1

break_point = 0
cnt = 0

while True :

    d -= 1
    if d < 0 :
        d += 4
    
    nx = x + dx[d]
    ny = y + dy[d]

    if board[nx][ny] == 0 and visited[nx][ny] == 0 :
        cnt = 0
        x = nx
        y = ny
        visited[nx][ny] = 1

    else :
        if cnt < 4 :
            cnt += 1
    
    ## 3 단계
    bx = x + dx[(d+2)%4]
    by = y + dy[(d+2)%4]

    if board[bx][by] == 0 :
        x = bx
        y = by
        cnt = 0
        visited[bx][by] = 1
    
    else :
        break

answer = 0
for i in range(N) :
    for j in range(M) :
        if visited[i][j] == 1 :
            answer += 1

print(answer)