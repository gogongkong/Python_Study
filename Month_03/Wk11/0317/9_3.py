'''
문제
어떤 나라에는 N개의 도시가 있다.
그리고 각 도시는 보내고자 하는 메시지가 있는 경우,
다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 
도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다.
또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며
도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

입력 조건
첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
(1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다.
(1 <= X, Y <= N, 1 <= Z <= 1,000)

출력 조건
첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.

[입력 예시]
3 2 1
1 2 4
1 3 2

[출력 예시]
2 4
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드갯수 n, 간선갯수 m, 시작노드 start
n,m, start = map(int, input().split())

arr = [[] for _ in range(n+1)]

# a에서 b로가는 비용은 c
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))

distance = [INF] * (n+1)

# 다익스트라 알고리즘
def dijkstra(start):
    q = [] 
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드인지 확인
        if dist > distance[now]:
            continue
        # 현재 노드와 인접한 노드들을 확인
        for array in arr[now]:
            cost = dist + array[1]
            # 더 짧은 경우
            if cost < distance[array[0]]:
                distance[array[0]] = cost
                heapq.heappush(q,(cost, array[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
                






































# import heapq
# import sys
# INF = int(1e9)
# input = sys.stdin.readline

# # 도시(노드)의 갯수 n / 통로(간선)의 갯수 m / 시작도시 start 입력
# n, m, start = map(int, input().split())
# arr = [[] for i in range(n+1)]
# distance = [INF] * (n+1)

# for i in range(1, m+1):
#     a, b, c = map(int, input().split())
#     arr[a].append((b,c))

# def dik(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     while q:
#         dist, now = heapq.heappop(q)
#         distance[now] = 0
#         if dist > distance[now]:
#             continue
#         for arrs in arr[now]:
#             cost = dist + arrs[1]
#             if cost < distance[arrs[0]]:
#                 distance[arrs[0]] = cost
#                 heapq.heappush(q,(cost,arrs[0]))

# dik(start)

# count = 0 

# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance, d)

# print(count - 1, max_distance)
        































# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m, start = map(int, input().split())

# arr = [[] for i in range(n+1)]

# for i in range(m):
#     a, b, c = map(int, input().split())
#     arr[a].append((b,c))

# distance = [INF] * (n+1)

# def da(start):
#     q =[]
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue
#         for arrr in arr[now]:
#             cost = dist + arrr[1]
#             if cost < distance[arrr[0]]:
#                 distance[arrr[0]] = cost
#                 heapq.heappush(q,(cost,arrr[0]))
# da(start)

# count = 0
# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance, d)


# print( count -1 , max_distance)

