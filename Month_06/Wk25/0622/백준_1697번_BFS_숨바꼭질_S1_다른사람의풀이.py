'''
https://www.acmicpc.net/problem/1697
'''

'''
수빈이의 위치 N, 동생의 위치 K 입력

걷기 = N+1 혹은 N-1, 순간이동 = 2 * N

동생을 찾는 가장 빠른 시간을 출력
'''

from collections import deque

MAX_num = 10 ** 5 # 최대값 제한으로 시간초과 방지

dist = [0] * (MAX_num + 1) # 이동 거리를 담을 변수

n, k = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        # for문의 새로운 사용법 익혀두자
        for nx in (x - 1, x + 1, x * 2): # if x == 5  --> nx = 4, 8, 10
            # nx가 최대값과 0 사이인지 그리고 dist[nx]가 False인지 ( dist는 0으로 초기화 되어있어 한번 접근하면 True임)
            if 0 <= nx <= MAX_num and not dist[nx]: 
                dist[nx] = dist[x] + 1
                queue.append(nx)

bfs()
