from itertools import combinations

# 0 = 빈칸, 1 = 사람, 2 = 병원
N,M = map(int,input().split())

board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

h = []
p = []

for i in range(N) :
    for j in range(N) :

        if board[i][j] == 2 :
            h.append((i,j))

        elif board[i][j] == 1 :
            p.append((i,j))

answer = 987654321
for i in combinations(h,M) :
    total = 0

    for px,py in p :
        distance_min = 987654321

        for x,y in h :
            d = abs(x-px) + abs(y-py)
            distance_min = min(distance_min,d)
        total += distance_min
    
    answer = min(total,answer)
print(answer)