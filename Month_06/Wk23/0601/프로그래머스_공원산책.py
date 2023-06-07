'''
https://school.programmers.co.kr/learn/courses/30/lessons/172928
'''

park = ["OSO","OOO","OXO","OOO"]
route = ["E 2","S 3","W 1"]

# 지나가는길 O 장애물 X 시작지점 S
# 동서남북으로 방향을 정의 'E' 'W' 'S' 'N'
# 장애물을 만나면 --> 무시(continue)
# 공원을 벗어나면 --> 무시(continue)
# 가로 W, 세로 H

def solution(park, route):
    direction = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}

    # 시작점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
    
    for move in route:
        dx, dy = direction[move.split()[0]]
        
        ix, iy = x, y # 임시 x, y값
        check = True # 장애물이나 밖으로 나간것을 확인하기 위한 변수

        for _ in range(int(move.split()[1])):
            nx = ix + dx
            ny = iy + dy
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                check = True
                ix, iy = nx, ny
            else:
                check = False
                break
        
        if check:
            x, y = nx, ny

    return [x,y]
    

print(solution(park, route))



