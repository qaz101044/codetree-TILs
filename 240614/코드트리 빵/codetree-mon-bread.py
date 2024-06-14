from collections import deque

## n = 격자의 크기, m = 사람의 수
N,M = map(int,input().split())

board = []
for _ in range(N) :
    board.append(list(map(int,input().split())))

goal = []
for _ in range(M) :
    goal_x,goal_y = map(int,input().split())
    goal.append((goal_x-1,goal_y-1))

## 4 방향 정의 : 북/서/동/남

dx = [-1,0,0,1]
dy = [0,-1,1,0]

## 목표 편의점과 가까운 베이스캠프 탐색
## 가까운 베이스캠프 여러 개인 경우에는 행이 작은 곳이 먼저 -> 열이 작은 곳이 먼저
def search_close_base_from_store(gx,gy) :
    visited_1 = [[0 for jdx in range(N)] for idx in range(N)]
    q_1 = deque()
    q_1.append((gx,gy))
    visited_1[gx][gy] = 1

    base_temp_1 = []

    while q_1 :

        sx,sy = q_1.popleft()

        for d_1 in range(4) :
            nx_1 = sx + dx[d_1]
            ny_1 = sy + dy[d_1]

            if 0 <= nx_1 < N and 0 <= ny_1 < N :
                if visited_1[nx_1][ny_1] == 0 and board[nx_1][ny_1] != -1:
                    if board[nx_1][ny_1] == 0 :
                        visited_1[nx_1][ny_1] = visited_1[sx][sy] + 1
                        q_1.append((nx_1,ny_1))
                    elif board[nx_1][ny_1] == 1 :
                        visited_1[nx_1][ny_1] = visited_1[sx][sy] + 1
                        base_temp_1.append([nx_1,ny_1,visited_1[nx_1][ny_1]])

    if len(base_temp_1) >= 1 :
        base_temp_1.sort(key=lambda x:(x[2],x[0],x[1]))
        # print(base_temp_1)
        # print(visited_1)
        return base_temp_1[0][0], base_temp_1[0][1]

    else :
        return -1,-1

def Calculate_d(px,py,goal__x,goal__y) :
    visited_cal = [[0 for jdx in range(N)] for idx in range(N)]
    q_2 = deque()
    q_2.append((px,py))
    visited_cal[px][py] = 1
    dis = 987654321

    while q_2 :

        sx_2, sy_2 = q_2.popleft()

        for d_2 in range(4) :

            nx_2 = sx_2 + dx[d_2]
            ny_2 = sy_2 + dy[d_2]

            if 0 <= nx_2 < N and 0 <= ny_2 < N :
                if visited_cal[nx_2][ny_2] == 0 and board[nx_2][ny_2] != -1 :
                    if nx_2 == goal__x and ny_2 == goal__y :
                        visited_cal[nx_2][ny_2] = visited_cal[sx_2][sy_2] + 1
                        dis = visited_cal[nx_2][ny_2]
                    else :
                        visited_cal[nx_2][ny_2] = visited_cal[sx_2][sy_2] + 1
                        q_2.append((nx_2,ny_2))

    if px == goal__x and py == goal__y :
        return 0
    else :
        return dis

## 사람 위치 정보
people = []
for _ in range(M) :
    people.append([-1,-1])

##print(goal)
##print("**************")
###################################
###############메인 함수#############
####################################

T = 0
arrival = 0
while arrival != M :
    T += 1

    ## 보드 위에 있는 사람들 이동
    for i in range(len(people)) :
        s_x = people[i][0]
        s_y = people[i][1]

        goal_x = goal[i][0]
        goal_y = goal[i][1]

        if s_x == goal_x and s_y == goal_y :
            continue

        else :

            route_temp = []

            for d in range(4) :
                nx = s_x + dx[d]
                ny = s_y + dy[d]

                if 0 <= nx < N and 0 <= ny < N :
                    if board[nx][ny] != -1 :
                        distance = Calculate_d(nx,ny,goal_x,goal_y)
                        route_temp.append([nx,ny,distance,d])

            route_temp.sort(key=lambda x:(x[2],x[3]))

            ## 사람 이동
            if len(route_temp) >= 1 :
                people[i][0] = route_temp[0][0]
                people[i][1] = route_temp[0][1]

                if people[i][0] == goal[i][0] and people[i][1] == goal[i][1] :
                    arrival += 1
    
    ## 격자 안에 있는 모든 사람이 이동한 후에 편의점에 도착한 칸은 이동할 수 없음
    for i in range(len(people)) :
        if people[i][0] == goal[i][0] and people[i][1] == goal[i][1] :
            board[goal[i][0]][goal[i][1]] = -1

    ## 현재 시간이 T분이고 T <= M을 만족한다면, T번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프로 이동
    if T <= M :
        gx, gy = goal[T-1][0], goal[T-1][1]
        base_x,base_y = search_close_base_from_store(gx,gy)
        board[base_x][base_y] = -1
        people[T-1][0] = base_x
        people[T-1][1] = base_y

        ## 오류 처리
        if base_x == -1 :
            ##print("ERROR")
            break

    ##print(people)
    ##print(arrival)

##print('ok')
print(T)