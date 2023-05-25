'''
그래프란?
그래프란 노드(Node)와 노드 사이에 연결된 간선(Edge)의 정보를 가지고 있는 자료 구조를 의미한다.
문제에서는 "서로 다른 개체(혹은 객체)가 연결되어 있다" 라는 얘기를 들으면 곧바로 그래프 알고리즘을 떠올리자.

예를 들어 
    - "여러개의 도시가 연결되어 있다."

그래프와 트리의 구분을 잘 하자
                            그래프                            트리
방향성                  방향 그래프 혹은 무방한 그래프      방향 그래프
순환성                  순환 및 비순환                     비순환
루트 노드 존재 여부      루트 노드가 없음                   루트 노드가 존재
노드간 관계성           부모와 자식 관계 없음               부모와 자식 관계
모델의 종류             네트워크 모델                      계층 모델

또한 그래프의 구현 방법은 2가지 방식이 존재하며 아래와 같다

인접 행렬 : 2차원 배열을 사용하는 방식
인접 리스트 : 리스트를 사용하는 방식

노드의 갯수 V, 간선의 갯수 E인 그래프에서
    - 인접 행렬 = O(V^2)
    - 인접 리스트 = O(E)
두 방식은 속도, 메모리 측면에서 구별된다

노드가 적은 경우 플로이드 워셜
노드와 간선이 많으면 다익스트라 

'''
'''
서로소 집합
서로소 집합이란 공통 원소가 없는 두 집합을 의미한다.
서로소 집합 자료구조를 설명하려면 서로소 집합 개념이 필요하다.
서로소 집합 자료구조란
" 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조" 라고 할 수 있다.
서로소 집합 자료구조는 union, find 2개의 연산으로 조작할 수 있다.

union(합집합)연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이다.
find(찾기)연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다.
스택과 큐가 각각 push, pop연산으로 이루어졌던 것처럼, 서로소 집합 자료구조는 합집합과 찾기 연산으로 구성된다.
서로소 집합 자료구조는 union - find 자료구조라고 불리기도 한다.
구현할 때는 트리 자료구조를 이용하여 집합을 표현하고
서로소 집합 정보(합집합 연산)가 주어졌을 때 트리 자료구조를 이용해서 집합을 표현하는 방법은 다음과 같다.
    1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
        i. A와 B의 루트노드 A', B'를 각각 찾는다.
        ii. A'와 B'의 부모 노드로 설정한다.(B'가 A'를 가리키도록 한다.)
    2. 모든 union(합집합) 연산을 처리할 때까지 1.번 과정을 반복한다.
여기서 가리킨다는 표현은 부모노드로 설정한다는 의미이다.

그래프 관련 설명은 책 271p

'''

# 기본적인 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합 찾기 - 효울 낮음
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# 특정 원소가 속한 집합 찾기 - 개선
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
parent = [0] * (v+1) # 부모테이블 초기화

# 부모테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ",end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')

print()

# 부모 테이블 내용 출력
print("부모테이블 : ", end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')

print()

'''
입력 예시
6 4
1 4
2 3
2 4
5 6

출력 예시
각 원소가 속한 집합 : 1 1 1 1 5 5
부모테이블 : 1 1 2 1 5 5
'''
'''
서로소 집합을 활용한 사이클 판별
서로소 집합은 다양한 알고리즘에 사용될 수 있다.
특히 서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있다는 특징이 있다.
참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.

union 연산은 그래프에서 간선으로 표현될 수 있다.
따라서 간선을 하나씩 확인 하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로
사이클을 판별할 수 있고 알고리즘은 아래와 같다.

    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
        i. 루트 노드가 서로 다르다면 두 노드에 대하여 union연산을 수행한다.
        ii. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
    2. 그래프에 포함되어 있는 모든 간선에 대하여 1.번 과정을 반복한다.
'''
# 서로소 집합을 활용한 사이클 판별 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수와 간선의(union연산)의 갯수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i # 부모 테이블 초기화

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 union 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 없음")

'''
입력 예시
3 3
1 2
1 3
2 3

출력 예시
사이클 발생
'''