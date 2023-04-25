'''
https://www.acmicpc.net/problem/1260
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split()) # 정점의 갯수N, 간선의 갯수 M, 탐색을 시작할 번호 V 입력

node = [[]for _ in range(n+1)] # 노드의 정보를 입력받을 리스트
visited = [False] * (n+1) # 해당 노드를 방문 했는지 안했는지 확인하는 변수
count_dfs = [start] # 시작노드 방문처리
count_bfs = [start]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b) # 양방향 연결
    node[b].append(a)

for i in range(n+1): # 연결 정보 정렬
    node[i].sort()

def dfs(start, node, visited): # DFS 함수 작성
    visited[start] = True # 시작노드 방문처리
    for next in node[start]:
        if visited[next] == False:
            visited[next] = True
            count_dfs.append(next)
            dfs(next, node, visited)
    return count_dfs

for i in dfs(start, node, visited):
    print(i,end=' ')
print()

visited = [False] * (n+1) # visited 초기화

def bfs(start, node, visited): # BFS 함수 작성
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for next in node[now]:
            if visited[next] == False:
                visited[next] = True
                count_bfs.append(next)
                queue.append(next)
    return count_bfs

for i in bfs(start, node, visited):
    print(i,end=' ')
print()