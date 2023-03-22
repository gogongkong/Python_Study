'''
동빈이는 온라인으로 컴퓨터 공학 강의를 듣고 있다. 
이 때 각 온라인 강의는 선수 강의가 있을 수 있는데, 
선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다. 
동빈이는 총 N개의 강의를 듣고자 한다. 강의는 1번부터 N번까지의 번호를 가진다. 
또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다. 
예를 들어, N = 3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고, 1번과 2번 강의는 선수 강의가 없다고 하자. 
그리고 각 강의에 대하여 강의 시간이 다음과 같다고 하자.

1번 강의: 30시간
2번 강의: 20시간
3번 강의: 40시간

이 경우, 1번 강의를 수강하기까지의 최소 시간은 30시간, 
2번 강의를 수강하기까지는 최소 20시간, 3번 강의를 수강하기까지는 최소 70시간이 필요하다. 
동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, 
N개의 강의에 대하여 수강하기까지는 걸리는 최소 시간을 출력하는 프로그램을 작성해라.

[입력조건]

첫째줄에 동빈이가 듣고자 하는 강의의 수 N(1 <= N <= 500)이 주어진다.
다음 N개의 줄에는 각 강의의 강의시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며,
 각 자연수는 공백으로 구분된다. 이 때 강의 시간은 100,000 이하의 자연수이다.
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

[출력조건]

N개의 강의에 대해 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.

[입력 예시]
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

[출력 예시]
10
20
14
18
17
'''
# 다시 풀기
from collections import deque
import copy
v = int(input())
arr = [[] for i in range(v+1)]
time = [0] * (v+1)
indegree = [0] * (v+1)

for i in range(1,v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 강의 시간 time에 저장
    for x in data[1:-1]: # data의 중간값
        indegree[i] += 1
        arr[x].append(i)

def T_sort():
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in arr[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v+1):
        print(result[i])

T_sort()


# # 풀이
# from collections import deque
# import copy

# v = int(input()) # 노드의 갯수 입력받기

# arr = [[] for i in range(v+1)] # 각 노드별 연결된 노드를 저장할 리스트 ex : 3번 노드에 1,2가 연결됨

# time = [0] * (v+1) # 강의 시간을 저장할 리스트
# indegree = [0] * (v+1) # 진입 차수를 저장할 리스트

# for i in range(1,v+1): # 노드의 수 만큼 반복
#     data = list(map(int, input().split())) # 강의시간, 선행노드, -1 입력
#     time[i] = data[0] # 입력받은 리스트의 가장 첫번째 인자는 강의시간
#     for x in data[1:-1]: # 입력받은 리스트의 가장 첫 인자(강의시간)와 끝 인자(-1) 의 사이값(연결된 노드) 만큼 반복
#         indegree[i] += 1 # 반복된 횟수는 연결된 노드의 횟수 == 진입차수 이므로 indegree +1
#         arr[x].append(i) # 연결된 노드(즉 상위 노드)의 리스트 번호에 하위 노드들을 삽입 ex 1번 노드에 2,3이 있다면 1번노드는 2,3으로 나간다.

# def T_sort():
#     q = deque() # 큐 선언
#     result = copy.deepcopy(time) # 강의 시간이 저장된 리스트를 deepcopy

#     for i in range(1, v+1): # 노드의 수만큼 반복
#         if indegree[i] == 0: # 진입차수가 0인 노드부터 진행
#             q.append(i) # 진입차수가 0인 노드는 큐에 삽입
    
#     while q: # 큐가 빌 때까지 반복
#         now = q.popleft() # 진입 차수가 0인 노드를 큐에서 now(현재노드를 의미)로 빼냄
#         for i in arr[now]: # 진입 차수가 0인 현재노드에 연결된(나가는) 노드를 i로 하면서 반복
#             result[i] = max(result[i], result[now] + time[i]) # 현재 노드에 연결된 노드의 강의 시간은 현재시간과 현재시간+상위시간중 큰것으로 변경
#             indegree[i] -= 1 # 상위노드에 대해 확인 하였으므로 진입차수 -1
#             if indegree[i] == 0: # 위로 3줄의 연산으로 진입차수가 0이 되었다면 큐에 삽입
#                 q.append(i)

#     for i in range(1, v+1): # 노드의 갯수만큼 반복
#         print(result[i]) # 변경된 시간(연결된 상위 노드의 시간들을 하위 노드 시간에 더한값들)을 하나씩 출력

# T_sort() # 함수 실행

