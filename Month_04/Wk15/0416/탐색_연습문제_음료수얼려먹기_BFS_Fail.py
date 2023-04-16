'''
문제
N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 
칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개가 생성된다

입력
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
출력
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

[입력 예시 1]
4 5
00110
00011
11111
00000

[출력 예시 1]
3

[입력 예시 2]
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

[출력 예시2]
8
'''
# 같은 문제를 BFS로 풀어보자
# 출처 : https://konghana01.tistory.com/69
from collections import deque

n, m = map(int, input().split())

arr = [map(int, input()) for _ in range(n)] # 얼음 틀 입력

def bfs(x,y):
    # 입력된 값이 0일 때, 즉 얼음을 만들 수 있는 공간일 때
    if arr[x][y] == 0:
        # 큐 생성
        queue = deque([x,y])
        # 방문 지점 표시
        arr[x][y] = 1
        # queue가 빌 때까지 반복 후 큐가 빌 때 1 리턴
        while True:
            if not queue:
                return 1
            x, y = queue.popleft()
            # 상 하 좌 우로 움직이며 이동한 장소가 0일 때 큐에 추가
            for dy, dx in ([1,0], [0,1], [-1,0], [0,-1]):
                if 0<= x+dx <= n-1 and 0<= y+dy <= m:
                    if arr[x+dx][y+dy] == 0:
                        arr.append([x+dx][y+dy])
                        arr[x+dx][y+dy] == 1
    return 0

result = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        result += bfs(x,y)

print(result)