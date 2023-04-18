'''
https://www.acmicpc.net/problem/2606

문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 
그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1 
4
'''

from collections import deque

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크의 수

com = [[] for _ in range(n+1)] # 연결을 저장할 리스트
result = [False] *(n+1) # 감염 여부 확인 리스트 

for _ in range(m): # 네트워크의 수 만큼 반복
    a, b = map(int, input().split()) # 네트워크 입력
    com[a].append(b) # 양방향 연결
    com[b].append(a)

# BFS 시작
def bfs(start):
    queue = deque([start]) # 큐에 시작 노드 삽입
    count = 0 # 횟수 저장 변수
    result[start] = True # 시작노드 감염처리
    
    while queue: # 큐가 빌 때까지 반복
        now = queue.popleft() # 시작노드 및 현재 노드 pop
        for next in com[now]: # 현재 노드와 연결된 노드를 next 라는 변수로 반복
            if not result[next]: # 다음 노드를 방문하지 않았을 경우 == if result[next] == False:
                result[next] = True # 다음 노드 감염처리
                queue.append(next) # 다음 노드 큐에 삽입
                count += 1 # 감염횟수 1 증가
    return count # 함수 동작이 완료 된 후 감염 횟수 return

print(bfs(1))
