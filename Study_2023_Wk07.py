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



# ''' 직접 풀어보기'''
# # 맵의 가로 세로 크기 입력받기
# n, m = map(int, input().split())
# # 공백의 맵 만들기
# d = [[0] * m for _ in range(n)]
# x, y, direction = list(map(int, input().split()))
# d[x][y] = 1 # 초기 위치 1로 찍어두기

# #북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# array = [] # 실제 맵 생성
# for i in range(n):
#     array.append(list(map(int, input().split())))

# # 캐릭터의 방향 함수
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# turn_time = 0
# count = 1

# # 시뮬레이션 시작
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1

#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
        
#         if array[nx][ny] == 1:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time =0

# print(count)

# ''' 백준 11047번 문제'''
# # 동전 종류 N 최솟값을 출력
# # N, K 입력 N(동전의 종류) K(동전의 가치 총합)
# n, k = map(int, input().split())
# count = 0
# result = 0
# coin = []
# for i in range(n):
#     coin.append(int(input()))
# coin.sort(reverse=True)

# for i in coin: 
#     count += k//i
#     k = k%i

# print(count)

# ''' 백준 11047번 문제 복습 '''

# # 동전 종류 갯수 n / 몫 k 입력받기
# n ,k = map(int, input().split())

# coins = [] #동전의 종류를 입력 받기 위한 공백의 리스트 생성
# # 동전의 종류 입력받기
# for i in range(n):
#     coins.append(int(input()))
# coins.sort(reverse= True) # 입력받은 코인을 내림차순으로 정렬

# count = 0 # 나눈 횟수를 저장하기 위한 변수
# # 나누기 시작
# for coin in coins:
#     count += k // coin # 나눈 몫은 동전의 갯수와 같다
#     k = k%coin # 나눈 몫에서 나머지는 더 낮은 동전으로 나눌 수 있는 거스름돈 = > 다시 k에 저장

# print(count)


# ''' 게임개발 문제 다시 복습 '''
# # 맵의 세로 크기 N, 가로 크기 M 입력받기
# n, m = map(int, input().split())
# #입력받은 크기로 공백의 맵 생성
# d = [[0] * m for _ in range(n)]
# # 맵에서 캐릭터의 위치 및 방향 입력받기
# x, y, direction = map(int, input().split())

# #초기 위치 방문으로 1찍어두기
# d[x][y] = 1

# # 실제 맵 입력
# array = [] # 실제 맵을 입력받을 함수
# for i in range(m):
#     array.append(list(map(int, input().split())))

# # 북 0 / 동 1 / 남 2 / 서 3 방향에 대해 입력하기
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전하는 함수
# def turn_left():
#     global direction # 함수 바깥의 direction 변수를 이용하기 위해 전역변수 선언
#     direction -= 1
#     if direction == -1: #방향은 0, 1, 2, 3  총 4가지이므로 -1이 되면 다시 3(서)로 초기화
#         direction = 3

# # 시뮬레이션 시작
# count = 1 # 처음 위치한 칸 +1
# turn_time = 0 #왼쪽으로 회전한 횟수를 저장하는 변수
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전하고 정면에 이동할 수 있는 칸이 있는 경우 
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         # x += nx 무지성으로 += 남발로 인한 에러 발생 이해하고 풀자
#         # y += ny
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전 후 정면에 이동할 수 있는 칸이 없을경우
#     else:
#         turn_time += 1 

#     if turn_time ==4: # 4방향 모두 갈곳이 없을 떄
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         #뒤로 갈 수 있다면 이동
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny

#         else: # 뒤가 바다로 막혀있을 경우
#             break
#         turn_time = 0

# print(count)

# ''' 큰수의 법칙 '''

# # 숫자의 종류 n / 더할수있는 횟수 m / 연속해서 더할 수 있는 횟수 k 입력받기
# n, m, k = map(int, input().split())

# # n개의 자연수 입력받기
# num = list(map(int, input().split()))
# # 입력받은 자연수들을 내림차순으로 정렬
# num.sort(reverse=True)
# first = num[0] # 가장 큰 수 
# sec = num[1] # 두번째로 큰 수
# result = 0 # 더한 값을 저장할 변수
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
    
#     result += sec
#     m -= 1

# print(result)





# n, m = map(int, input().split())
# d = [[0] * m for _ in range(n)]
# x, y, direction = map(int, input().split())
# d[x][y] = 1
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
    
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1

#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0

# print(count)


# ''' 15일 공부 종료 16일 공부 시작 
# 어설프게 문제풀이 하지말고 일단 책한권 돌리자!'''

# ''' 게임 개발 문제 이번엔 꼭 뿌셔보자 '''
# # 맵의 세로 N 가로 M을 입력 받기
# n, m = map(int, input().split())
# d = [[0] * m for _ in range(n)] # 가로 세로 공백의 맵 생성

# # 캐릭터의 좌표 x,y 방향 direction 입력 받기
# x, y, direction = map(int, input().split())

# # 맵의 정보 입력 받기
# maps = [] # 정보를 입력받을 공백의 리스트 생성
# for i in range(m):
#     maps.append(list(map(int, input().split()))) # 맵 입력받기

# # 방향은 4가지 북0 동1 남2 서3 가있음
# # 방향에 따라 입력받을 리스트 생성
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전하는 함수 만들기
# def turn_left():
#     global direction
#     direction -= 1 # 왼쪽(반시계)방향으로 회전
#     if direction == -1: # 이미 북쪽을 바라보고 있다면?
#         direction = 3 # 서쪽으로 바꿔주기

# #시뮬레이션 시작
# d[x][y] = 1 # 초기 위치 방문처리

# turn_time = 0 # 회전한 횟수
# count = 1 # 초기 위치방문처리로 인해 count 1 증가

# while True: # break로 탈출 전까진 계속 돌리기
#     turn_left() # 첫번째 조건 : 현위치에서 일단 왼쪽방향부터 갈곳이 있는지 탐색
#     # 현재 방향에 맞는 값을 dx, dy의 리스트에서 direction 의 값에 위치한 dx, dy값을 더해줌
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 이동할 곳이 있을 때
#     if d[nx][ny] == 0 and maps[nx][ny] == 0:
#         d[nx][ny] = 1 # 현위치 방문처리
#         x, y = nx, ny # 이동
#         turn_time = 0
#         count += 1
#         continue
#     else: # 이동할 곳이 없을 때 회전 횟수 1 증가
#         turn_time += 1

#     if turn_time == 4: # 4번 회전(4방향 모두 확인 했을 때)
#         nx = x - dx[direction] # 뒤로 한칸
#         ny = y - dy[direction]
#         if d[nx][ny] == 0 and maps[nx][ny] == 0: # 뒤에 갈곳이 있을 때
#             d[nx][ny] = 1 # 현위치 방문처리 
#             x, y = nx, ny
#             count += 1
#         else: # 갈곳이 없을 때
#             break

# print(count)


# ''' 2월 17일 공부 스타트'''
# # push : 데이터를 삽입
# # pop  : 데이터를 삭제

# # 스택 선입 후출 or 후입 선출 예제
# stack = []
# # 삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 삭제
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack)

# # 큐 = 선입선출
# # 예제 삽5 삽2 삽3 삽7 삭제 삽1 삽4 삭제
# from collections import deque
# que = deque()
# que.append(5)
# que.append(2)
# que.append(3)
# que.append(7)
# que.popleft()
# que.append(1)
# que.append(4)
# que.popleft()

# print(que)
# que.reverse()
# print(que)


# # 재귀 함수
# def recursive_function(i):
#     # 100번째 출력 했을 때 종료 되도록 종료 조건 명시
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출 합니다.')
#     recursive_function(i+1)
#     print(i, '번째 재귀함수를 종료합니다.')

# recursive_function(1)

# # 팩토리얼 예제
# # 반복적으로 구현한 n!
# def factorial_iterative(n):
#     result = 1
#     # 1부터 n까지의 수 차례대로 곱하기
#     for i in range(1, n+1):
#         result *= i
#     return result

# # 재귀적으로 구현한 n!
# def factorial_recursive(n):
#     if n<= 1: #n이 1 이하인경우 1을 반환
#         return 1
#     # n! = n*(n-1)! 을 그대로 코드로 작성하기
#     return n * factorial_recursive(n-1)

# print("반복적으로 구현 : ", factorial_iterative(5))
# print("재귀적으로 구현 : ", factorial_recursive(5))

# ''' 인접 행렬 방식'''
# INF = 999999999
# # 2차원 리스트를 이용해 인접 행렬 표현
# graph = [
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0]
# ]
# print(graph)

# ''' 인접 리스트 방식'''
# graph = [[] for _ in range(3)]

# #노드 0에 연결된 노드 정보 저장(노드, 거리)
# graph[0].append((1,7))
# graph[0].append((2,5))

# #노드 1에 연결된 노드 정보 저장(노드, 거리)
# graph[1].append((0,7))

# #노드 2에 연결된 노드 정보 저장(노드, 거리)
# graph[2].append((0,5))
# print( graph)

# # DFS 메서드 정리
# def dfs(graph, v, visited):
#     # 현재 노드 방문 처리
#     visited[v] = True
#     print(v, end = ' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)
'''
BFS 너비 우선 탐색 
선입선출 큐 방식을 이용하는 것이 정석
인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성 --> 가까운 노드부터 탐색을 진행
 
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
3. 2번의 과정을 더이상 수행 할 수 없을 때 까지 반복한다.
'''
# BFS 예제
from collections import deque

# BFS 메서드 정의
