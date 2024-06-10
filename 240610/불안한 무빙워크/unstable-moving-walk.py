n,k = map(int,input().split())
board = list(map(int,input().split()))
people = [0 for j in range(2*n)]
T = 0
break_point = 0

while break_point != 1 :
    T += 1
    ## 무빙워크, 사람 한 칸씩 시계 방향으로 회전
    new_board = [0 for j in range(2*n)]
    new_board[0] = board[-1] 
    for i in range(1,len(board)) :
        new_board[i] = board[i-1]
    
    new_people = [0 for j in range(2*n)]
    new_people[0] = people[-1]
    for i in range(1,len(people)) :
        new_people[i] = people[i-1]

    ## 이동 후 무빙워크, 사람 갱신
    board = new_board
    people = new_people
    
    ## 도착한 사람은 내림
    if people[n-1] >= 1 :
        people[n-1] = 0

    ## "가장 먼저 무빙워크에 올라간 사람부터" 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
    for i in range(n-2,-1,-1) :
        if people[i] == 1 :
            if people[i+1] == 0 and board[i+1] >= 1 :
                people[i+1] = 1
                people[i] = 0
                board[i+1] -= 1
    
    ## 도착한 사람은 내림
    if people[n-1] >= 1 :
        people[n-1] = 0
    
    ## 사람 올리기 : 0번 칸에 사람이 없고 안정성이 0이 아니라면 한 명 올립니다.
    if board[0] >= 1 and people[0] == 0 :
        people[0] = 1
        board[0] -= 1
    
    cnt = 0
    for i in board :
        if i == 0 :
            cnt += 1
    
    if cnt >= k :
        break_point = 1
    
print(T)