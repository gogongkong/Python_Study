'''
신장 트리
"하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다."
이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립조건이기도 하다

크루스칼 알고리즘
모든 노드를 연결할때 최소한의 비용으로 연결하려면 어떤 알고리즘을 써야할까?
대표적인 최소 신장 트리 알고리즘이며 그리디 알고리즘으로 분류됨
먼저 모든 간선에 대하여 정렬을 수행하고 가장 거리가 짧은 간선부터 집합에 포함시키면 된다.
구체적인 알고리즘은 다음과 같다.
    
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
        i. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
        ii. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    3. 모든 간선에 대하여 2번의 과정을 반복한다.

최소 신장트리는 일종의 트리(tree)자료구조 이므로, 최종적으로 신장트리에 포함되는 간선의 갯수가
"노드의 갯수 -1"과 같다는 특징이 있다.
크루스칼 알고리즘의 핵심 원리는 가장 거리가 짧은 간선부터 차례대로 집합에 추가하면 된다는 것이다.

'''

# 크루스칼 알고리즘 소스코드

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수와 간선의 갯수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)

'''
입력 예시
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
출력 예시
159
'''
'''
크루스칼 알고리즘의 시간 복잡도
크루스칼 알고리즘은 간선의 갯수가 E개일때
O(ElogE)의 시간 복잡도를 가진다.

'''
