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


from collections import deque
import copy


# 노드의 갯수 입력받기 
v = int(input())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
# 위상 정렬 함수
def TS():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

TS()

