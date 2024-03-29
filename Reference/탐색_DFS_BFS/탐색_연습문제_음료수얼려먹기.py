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



















n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >=m or arr[x][y] == 1:
        return False
    elif arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)




































# 정답지
# 얼음틀의 세로길이 N, 가로길이 M 입력
n, m = map(int, input().split())

arr = []
# 얼음틀 입력
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >=m:
        return False
    elif arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)