'''
신장트리
"하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프"를 의미
단, 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않아야함

크루스칼 알고리즘
    - 모든 노드를 연결할 때 최소한의 비용으로 연결하려면?
    - 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘을 "최소 신장 알고리즘"이라고 한다.
    - 크루스칼 알고리즘은 대표적인 최소 신장 알고리즘
    - 가장 적은 비용으로 모든 노드를 연결할 수 있음
    - 그리디 알고리즘으로 분류
    - 모든 간선에 대해 정렬을 수행한 뒤 가장 거리가 짧은 간선 부터 집합에 포함 시키면 된다.
        1. 간선데이터를 비용에 따라 오름차순으로 정렬 한다.
        2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
            i. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함 시킨다.
            ii. 사이클이 발생하는 경우 최소 신장 트리에 포함 시키지 않는다.
        3. 모든 간선에 대하여 2번의 과정을 반복한다.

크루스칼 알고리즘은 트리 자료구조를 이용한다.
'''

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수와 간선(union 연산)의 갯수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을  변수
edges = []
result = 0

# 부모 테이블상에서, 부모 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬 하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함시킴
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

'''
[입력예시]
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

[출력예시]
159
'''

