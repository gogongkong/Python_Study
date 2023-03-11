'''
서로소 집합 사이클 판별

무방향 그래프 내에서 사이클을 판별할 때 사용가능

union연산은 그래프에서 간선으로 표현 될 수 있고
간선을 하나씩 확인하면 두 노드가 포함된 집합을 합치는 과정을 반복하는것 만으로
사이클 판별이 가능

알고리즘
    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
        i. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
        ii. 루트 노드가 서로 같다면 사이클이 발생할 것.
    2. 그래프에 포함되어 있는 모든 간선에 대해 1.번 과정을 반복

'''

# 서로소 집합을 활용한 사이클 판별 소스코드
# 특정 원소가 속한 집합을 찾기 
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 떄 까지 재귀적으로 호출
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a <b:
        parent[b] = a
    else:
        parent[a] = b
# 노드의 갯수와 간선(union연산)의 갯수 입력
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모테이블에서 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 없음')
'''
3 3
1 2
1 3
2 3
사이클 발생
'''