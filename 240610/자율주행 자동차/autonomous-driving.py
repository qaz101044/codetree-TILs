from collections import deque

N,M = map(int,input().split())

## 4방향 정의 : 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

## 자율 주행 자동차 초기 조건
sx, sy, d = map(int,input().split())

board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

visited = [[0 for j in range(M)] for i in range(N)]

q = deque()
q.append((sx,sy))
visited[sx][sy] = 1
cnt = 0

while q :
    x,y = q.popleft()

    for k in range(4) :
        
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[nx][ny] == 0 :
            q.append((nx,ny))
            visited[nx][ny] = 1

for i in range(N) :
    for j in range(M) :
        if visited[i][j] == 1 :
            cnt += 1

print(cnt)