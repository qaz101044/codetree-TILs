from collections import deque

def bfs(x_1,y_1,x_2,y_2,board,visited,N,M) :
    ## 동/남/서/북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    ## 북/서/남/동
    dx_2 = [-1,0,1,0]
    dy_2 = [0,-1,0,1]

    damaged_turrets = []

    q = deque()
    q.append((x_1,y_1))
    cnt = -1
    visited[x_1][y_1] = 1

    while q :
        s_x, s_y = q.popleft()

        for idx in range(4) :
            nx = (s_x + dx[idx]) % N
            ny = (s_y + dy[idx]) % M

            if visited[nx][ny] == 0 and board[nx][ny] != 0 :
                visited[nx][ny] += visited[s_x][s_y] + 1
                q.append((nx,ny))
    
    ## 도착할 수 있는지 확인
    if visited[x_2][y_2] == 0 :
        return damaged_turrets

    else :

        cnt = visited[x_2][y_2]
        q_2 = deque()
        q_2.append((x_2,y_2))
        #print(visited)
        #print('---------------')

        while q_2 :
            e_x,e_y = q_2.popleft()
            
            for idxx in range(4) :
                nx_2 = (e_x + dx_2[idxx]) % N
                ny_2 = (e_y + dy_2[idxx]) % M

                if visited[nx_2][ny_2] == cnt - 1 and visited[nx_2][ny_2] != 0 :
                    q_2.append((nx_2,ny_2))
                    damaged_turrets.append((nx_2,ny_2))
                    cnt -= 1
                    #print(cnt,nx_2,ny_2)
                    break

        return damaged_turrets


    


N,M,K = map(int,input().split())

board = []
attacked = []
answer = 0
for i in range(N) :
    board.append(list(map(int,input().split())))

for i in range(N) :
    attacked.append([0]*M)

#print(attacked)

# K 횟수만큼 반복
for t in range(K) :

    break_point = 0
    chk_remain = 0
    tower_MIN = 987654321
    tower_MAX = -987654321
    temp = []
    att_x = -1
    att_y = -1

    ## 공격자 선정 및 부숴지지 않은 포탑 개수 확인

    for i in range(N) :
        
        for j in range(M) :
            if board[i][j] != 0 :
                chk_remain += 1

                ## 가장 약한 포탑 찾기
                if board[i][j] < tower_MIN :
                    tower_MIN = board[i][j]
                    temp = []
                    temp.append((i,j)) ## 이후 x좌표 + 1 , y좌표 + 1해서 공격력 계산해야함
                
                elif board[i][j] == tower_MIN :
                    temp.append((i,j)) ## 이후 x좌표 + 1 , y좌표 + 1해서 공격력 계산해야함

                ## 가장 강한 포탑 찾기
                if board[i][j] > tower_MAX :
                    tower_MAX = board[i][j]
                    strong_1 = []
                    strong_1.append((i,j))
                
                elif board[i][j] == tower_MAX :
                    strong_1.append((i,j))

    
    ## 부서지지 않은 포탑이 1개 이하면 중지
    if chk_remain <= 1 :
        break

    ## 공격자 선정 2단계
    if len(temp) == 1 :
        att_x = temp[0][0]
        att_y = temp[0][1]
    
    ### 공격력이 가장 낮은 포탑이 2개 이상인 경우
        ### 가장 최근에 공격한 포탑 선정
    attacked_min = 987654321
    temp_2 = []
    for x,y in temp :
        if attacked[x][y] < attacked_min :
            attacked_min = attacked[x][y]
            temp_2 = []
            temp_2.append((x,y))
        elif attacked[x][y] == attacked_min :
            temp_2.append((x,y))

    if len(temp_2) == 1 :
        att_x = temp_2[0][0]
        att_y = temp_2[0][1]
        
        ### 행과 열의 합이 가장 작은 포탑 선정
    else :
        sum_min = 987654321
        temp_3 = []

        for x_2,y_2 in temp_2 :
            if x_2 + y_2 < sum_min :
                sum_min = x_2 + y_2
                temp_3 = []
                temp_3.append((x_2,y_2))
            elif x_2 + y_2 == sum_min :
                temp_3.append((x_2,y_2))

        if len(temp_3) == 1 :
            att_x = temp_3[0][0]
            att_y = temp_3[0][1]
            
            ### 열 값이 가장 작은 포탑
        else :
            y_min = 987654321
            temp_4 = []

            for x_3,y_3 in temp_3 :
                if y_3 < y_min :
                    y_min = y_3
                    temp_4 = []
                    temp_4.append((x_3,y_3))
                
            att_x = temp_4[0][0]
            att_y = temp_4[0][1]
    
    ## 공격 대상 선정
    if len(strong_1) == 1 :
        target_x = strong_1[0][0]
        target_y = strong_1[0][1]
    
    ### 공격력이 가장 높은 포탑이 2개 이상인 경우
    else :
        attacked_min_2 = 987654321
        strong_2 = []
        for a_1,b_1 in strong_1 :
            if attacked[a_1][b_1] < attacked_min_2 :
                attacked_min_2 = attacked[a_1][b_1]
                strong_2 = []
                strong_2.append((a_1,b_1))
            elif attacked[a_1][b_1] == attacked_min_2 :
                strong_2.append((a_1,b_1))
        
        if len(strong_2) == 1 :
            target_x = strong_2[0][0]
            target_y = strong_2[0][1]

        ### 행과 열의 합이 가장 작은 포탑 선정    
        else :
            sum_min_2 = 987654321
            strong_3 = []

            for a_2,b_2 in strong_2 :
                if a_2 + b_2 < sum_min_2 :
                    sum_min_2 = a_2 + b_2
                    strong_3 = []
                    strong_3.append((a_2,b_2))
                elif a_2 + b_2 == sum_min_2 :
                    strong_3.append((a_2,b_2))
            
            if len(strong_3) == 1 :
                target_x = strong_3[0][0]
                target_y = strong_3[0][1]

            else :
                y_min_2 = 987654321
                strong_4 = []

                for a_3,b_3 in strong_3 :
                    if b_3 < y_min_2 :
                        y_min_2 = b_3
                        strong_4 = []
                        strong_4.append((a_3,b_3))
                
                target_x = strong_4[0][0]
                target_y = strong_4[0][1]
    
    ## 공격자 공격력 상승
    board[att_x][att_y] += (N+M)

    ## 전체 공격 시간 1초 증가 (관련자는 이후 0초로 초기화)
    for idx1 in range(N) :
        for idj1 in range(M) :
            attacked[idx1][idj1] += 1 

    ## 공격자 공격시간 차감
    attacked[att_x][att_y] = 0

    ## 레이저 공격 // 우선순위 : 동/남/서/북
    visited = []
    for w in range(N) :
        visited.append([0]*M)

    damaged_list = bfs(att_x,att_y,target_x,target_y,board,visited,N,M)
    #print(len(damaged_list))

    
    ### 레이저 공격 가능
    if len(damaged_list) != 0 :

        ### 공격 대상자 포탑은 공격자 공격력만큼의 공격을 받습니다.
        board[target_x][target_y] -= board[att_x][att_y]
        if board[target_x][target_y] <= 0 :
            board[target_x][target_y] = 0
        attacked[target_x][target_y] = 0
        ### 레이저 경로에 있는 포탑들은 공격자 공격력의 절반 만큼의 공격을 받습니다.
        for l_x,l_y in damaged_list :
            if l_x == att_x and l_y == att_y :
                continue
            else :
                board[l_x][l_y] -= (board[att_x][att_y] // 2)
                if board[l_x][l_y] <= 0 :
                    board[l_x][l_y] = 0
                attacked[l_x][l_y] = 0
    
    ## 포탄 공격
    else :
        ### 공격 대상자 포탄 피격
        board[target_x][target_y] -= board[att_x][att_y]
        if board[target_x][target_y] <= 0 :
            board[target_x][target_y] = 0
        attacked[target_x][target_y] = 0
        ### 경계무시 8방향 공격
        for zx in range(-1,2) :
            for zy in range(-1,2) :
                x_t = (target_x + zx) % N
                y_t = (target_y + zy) % M

                if board[x_t][y_t] != 0 :
                    board[x_t][y_t] -= (board[att_x][att_y] //2)
                    if board[x_t][y_t] <= 0 :
                        board[x_t][y_t] = 0
                    attacked[x_t][y_t] = 0
    
    #print(attacked)
    #print(board)

    ## 포탑 정비
    for idn in range(N) :
        for idj in range(M) :
            if attacked[idn][idj] != 0 and board[idn][idj] != 0 :
                board[idn][idj] += 1


answer_MAX = -987654321
for i in range(N) :
    for j in range(M) :
        if board[i][j] != 0 and board[i][j] > answer_MAX :
            answer_MAX = board[i][j]

print(answer_MAX)