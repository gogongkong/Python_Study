# print("깃허브 외장 SSD 환경 구축 실험")

# '''118p 게임개발 문제 공부'''

# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# #방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 X좌표 Y좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1 #현재 좌표 방문 처리

# #전체 맵정보를 입력받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# #왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction =3 

# #시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     #왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀 있는경우
#         else:
#             break
#         turn_time =0
    
# #정답 출력
# print(count)



''' 직접 풀어보기'''

n,m = map(int, input().split()) # 가로 세로 공백을 구분하여 입력
# 캐릭터의 좌표(x,y) 및 방향(direction)을 입력 받기

# 공백의 행렬을 만들어 맵 초기화
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 # 처음 캐릭터의 좌표 (1,1)



# 전체 맵 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향관련 변수 만들기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#방향 전환 함수 만들기
def turn_left():
    global direction 
    direction -= 1
    if direction == -1:
        direction = 3

turn_time = 0
count = 1

# 이동 시뮬레이션 작성해보기

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 방향을 돌리고 진행방향에 바다가 없을 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0: 
        d[nx][ny] =1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전했는데 진행방향에 바다가 있을경우
    else:
        turn_time += 1
    
    # 4면 모두 갈 곳이 없을떄
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있는지
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        #뒤가 바다로 막혀 있을경우
        else:
            break
        turn_time =0

#결과 출력
print(count)
    
