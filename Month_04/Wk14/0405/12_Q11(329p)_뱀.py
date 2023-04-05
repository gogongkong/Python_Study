'''
뱀
'Dummy'라는 도스 게임이 있습니다.
이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어납니다.
뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝납니다.
게임은 N x N  정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있습니다.
보드의 상하좌우 끝에는 벽이 있습니다. 
게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1입니다.

뱀은 처음에 오른쪽을 향합니다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따릅니다.
    - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킵니다.
    - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
    - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다.
    즉, 몸길이는 변하지 않습니다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇초에 끝나는지 계산하세요.

[입력 조건]
    - 첫째 줄에 보드의 크기 N 이 주어집니다.(2 <= N <= 100)
    다음 줄에 사과의 갯수 K가 주어집니다.( 0 <= K <= 100)
    - 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행,
    두 번째 정수는 열 위치를 의미합니다. 단, 사과의 위치는 모두 다르며
    맨 위 맨 좌측(1행1열)에는 사과가 없습니다.
    - 다음 줄에는 뱀의 방향 변환 횟수 L이 주어집니다. (1 <= L <= 100)
    - 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수X와 문자 C로 이루어져 있으며,
    게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로
    90도 방향을 회전시킨다는 뜻입니다. X는 10,000이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로
    주어집니다.


[출력 조건]
    - 첫째 줄에 게임이 몇초에 끝나는지 출력합니다.

[입력 예시1]
6
3
3 4
2 5
5 3D
3
3 D
15 L
17 D

[출력 예시1]
9

[입력 예시2]
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

[출력 예시2]
21

[입력 예시3]
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

[출력 예시3]
13
'''

n = int(input()) # 보드의 크기 N
k = int(input()) # 사과의 갯수 K

data = [[0] * (n+1) for _ in range(n+1)] # 보드 입력
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

info = [] # 뱀의 방향 변환 정보를 입력 받을 리스트 info
l = int(input()) # 뱀의 방향 변환 횟수 L
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 초기 위치는 오른쪽(동쪽)을 바라 보고 있으므로 방향 전환 순서는 동 남 서 북 으로 결정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c): # 방향 변환 함수
    if c == "L":
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4
    return direction

def simulation(): # 입력된 정보로 뱀을 이동시키는 함수 작성
    direction = 0
    time = 0
    index = 0
    x, y = 1, 1
    data[x][y] = 1
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 뱀이 벽 안에 있고 몸통안에 있지 않다면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and data[nx][ny] != 2:
            # 이동할 위치에 사과가 없다면 머리 이동 후 꼬리 자르기
            if data[nx][ny] != 1:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
            
        else: # 이동이 불가능 할 때
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1

        # 방향을 바꿀 시간이 왔을 때
        if time == info[index][0] and index < l:
            direction = turn(direction, info[index][1])
            index += 1
    return time
print(simulation())































# n = int(input()) # 보드의 크기 N
# k = int(input()) # 사과의 갯수 K

# data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
# info = [] # 방향 회전 정보

# # 사과 위치 입력
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1

# # 방향 회전 정보 입력
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x),c))

# # 초기에 오른쪽(동)을 바라보고 있으므로 동, 남, 서, 북으로 설정
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]        

# def turn(direction, c):
#     if c == "L":
#         direction = (direction -1) % 4
#     else:
#         direction = (direction +1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1 # 초기 위치 설정
#     data[x][y] = 2 # 뱀의 머리 위치는 2로 설정
#     direction = 0 # 처음에는 동쪽을 바라봄
#     time = 0
#     index = 0 # 다음 회전 정보
#     q = [(x,y)]
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#         if 1 <= nx and nx <= n and 1<= y and ny <= n and data[nx][ny] != 2:
#             # 사과가 없다면 이동 후 꼬리 제거
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             # 사과가 있다면 이동 후 꼬리는 그대로 두기
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         # 벽이나 뱀의 몸통과 부딪히면
#         else:
#             time += 1
#             break
#         x, y = nx, ny # 다음 위치로 머리 이동
#         time += 1
#         if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time

# print(simulate())
