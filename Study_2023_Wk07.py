print("깃허브 외장 SSD 환경 구축 실험")

'''118p 게임개발 문제 공부'''

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X좌표 Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

#전체 맵정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3 

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는경우
        else:
            break
        turn_time =0
    
#정답 출력
print(count)



''' 직접 풀어보기'''
# 맵의 가로 세로 크기 입력받기
n, m = map(int, input().split())
# 공백의 맵 만들기
d = [[0] * m for _ in range(n)]
x, y, direction = list(map(int, input().split()))
d[x][y] = 1 # 초기 위치 1로 찍어두기

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = [] # 실제 맵 생성
for i in range(n):
    array.append(list(map(int, input().split())))

# 캐릭터의 방향 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

turn_time = 0
count = 1

# 시뮬레이션 시작
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 1:
            x = nx
            y = ny
        else:
            break
        turn_time =0

print(count)

''' 백준 11047번 문제'''
# 동전 종류 N 최솟값을 출력
# N, K 입력 N(동전의 종류) K(동전의 가치 총합)
n, k = map(int, input().split())
count = 0
result = 0
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

for i in coin: 
    count += k//i
    k = k%i

print(count)

''' 백준 11047번 문제 복습 '''

# 동전 종류 갯수 n / 몫 k 입력받기
n ,k = map(int, input().split())

coins = [] #동전의 종류를 입력 받기 위한 공백의 리스트 생성
# 동전의 종류 입력받기
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse= True) # 입력받은 코인을 내림차순으로 정렬

count = 0 # 나눈 횟수를 저장하기 위한 변수
# 나누기 시작
for coin in coins:
    count += k // coin # 나눈 몫은 동전의 갯수와 같다
    k = k%coin # 나눈 몫에서 나머지는 더 낮은 동전으로 나눌 수 있는 거스름돈 = > 다시 k에 저장

print(count)


''' 게임개발 문제 다시 복습 '''
# 맵의 세로 크기 N, 가로 크기 M 입력받기
n, m = map(int, input().split())
#입력받은 크기로 공백의 맵 생성
d = [[0] * m for _ in range(n)]
# 맵에서 캐릭터의 위치 및 방향 입력받기
x, y, direction = map(int, input().split())

#초기 위치 방문으로 1찍어두기
d[x][y] = 1

# 실제 맵 입력
array = [] # 실제 맵을 입력받을 함수
for i in range(m):
    array.append(list(map(int, input().split())))

# 북 0 / 동 1 / 남 2 / 서 3 방향에 대해 입력하기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction # 함수 바깥의 direction 변수를 이용하기 위해 전역변수 선언
    direction -= 1
    if direction == -1: #방향은 0, 1, 2, 3  총 4가지이므로 -1이 되면 다시 3(서)로 초기화
        direction = 3

# 시뮬레이션 시작
count = 1 # 처음 위치한 칸 +1
turn_time = 0 #왼쪽으로 회전한 횟수를 저장하는 변수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전하고 정면에 이동할 수 있는 칸이 있는 경우 
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        # x += nx 무지성으로 += 남발로 인한 에러 발생 이해하고 풀자
        # y += ny
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 후 정면에 이동할 수 있는 칸이 없을경우
    else:
        turn_time += 1 

    if turn_time ==4: # 4방향 모두 갈곳이 없을 떄
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        else: # 뒤가 바다로 막혀있을 경우
            break
        turn_time = 0

print(count)