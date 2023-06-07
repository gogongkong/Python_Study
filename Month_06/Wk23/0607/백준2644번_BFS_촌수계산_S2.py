'''
https://www.acmicpc.net/problem/2644
문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
이러한 촌수는 다음과 같은 방식으로 계산된다. 
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 
이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 
이때에는 -1을 출력해야 한다.

예제 입력 1 
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
예제 출력 1 
3
'''

# 하루 지났으니 다시 풀어보자

from collections import deque

n = int(input()) # 노드의 갯수
target1, target2 = map(int, input().split()) # 촌수(차수) 계산을 할 타겟 노드들
m = int(input()) # 간선의 갯수
data = [[] for _ in range(n+1)] # 간선의 정보를 담을 리스트
visited = [False] * (n+1) # 방문한 노드를 기록할 리스트
count = [0] * (n+1) # 차수(촌수)정보를 담을 리스트

for _ in range(m):
    a, b = map(int, input().split()) # a는 b의 부모 입력 후 양방향 연결
    data[a].append(b)
    data[b].append(a)

def bfs(target1):
    queue = deque()
    queue.append(target1)
    visited[target1] = True

    while queue: # queue가 빌 때까지 반복
        now = queue.popleft()
        for i in data[now]: # 현재 노드와 연결되어 있는 노드를 하나씩 확인
            if visited[i] == False: # 방문하지 않았다면
                visited[i] = True # 방문처리 하고
                queue.append(i) # 확인한 노드 queue에 넣고
                count[i] = count[now] + 1 # 현재 노드의 차수 + 1 ( = 현재 노드의 촌수에서 +1 해야 내 촌수가 나오기 때문)


bfs(target1)

if count[target2] == 0:
    print(-1)
else:
    print(count[target2])
            

            
