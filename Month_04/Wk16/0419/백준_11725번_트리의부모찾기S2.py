'''
https://www.acmicpc.net/problem/11725

문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 
각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
'''




import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 반복횟수 늘리는 함수

n = int(input())

data = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(start, data, parent):
    for i in data[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, data, parent)

dfs(1, data, parent)

for i in range(2,n+1):
    print(parent[i], end=" ")


