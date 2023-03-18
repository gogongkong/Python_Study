'''
위상정렬
방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는것
전형적인 위상정렬 예시
- 선수과목을 고려한 학습 순서 설정

위상 정렬 알고리즘
    1. 진입 차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때까지 다음의 과정을 반복한다.
        i.  큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
        ii. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

모든 원소를 방문하기 전에 큐가 비어버리면 사이클이 발생한다는 뜻
하지만 기본적으로 위상정렬 문제는 사이클이 발생하지 않는다고 명시 하는경우가 많음

'''

# 위상 정렬 소스코드

from collections import deque

# 노드의 갯수와 간선의 갯수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] *(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def TS():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드들을 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        # 위상정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

TS()


'''
입력예시
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력예시
1 2 5 3 6 4 7

'''