from collections import deque

N,L,R = map(int,input().split())

## 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

board = []
for _ in range(N) :
    board.append(list(map(int,input().split())))

visited = [[0 for j in range(N)] for i in range(N)]

def bfs(x,y) :

    temp = []
    total = 0

    q = deque()
    q.append((x,y))
    temp.append((x,y))
    visited[x][y] = 1
    total += board[x][y]

    while q :
        x,y = q.popleft()
        for d in range(4) :

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and L <= abs(board[nx][ny] - board[x][y]) <= R :
                visited[nx][ny] = 1
                temp.append((nx,ny))
                total += board[nx][ny]
                q.append((nx,ny))
        
    for x_t,y_t in temp :
        board[x_t][y_t] = total // len(temp)
    
    if len(temp) > 1 :
        return True
    else :
        return False

answer = 0

while True :
    cnt = 0
    visited = [[0 for j in range(N)] for i in range(N)]

    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                bfs(i,j)
                cnt += 1
    
    if cnt == N*N :
        break
    else :
        answer += 1
    

print(answer)