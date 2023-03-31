'''
https://school.programmers.co.kr/learn/courses/30/lessons/60059

자물쇠와 열쇠
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다.
그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨있었고 문 앞에는 특이한 형태의 열쇠와 함께
자물쇠를 푸는 방법에 대해 다음과 같이 설명해주는 종이가 발견되었습니다.
잠겨있는 자물쇠는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는
MxM크기인 정사각 격자 형태로 되어 있습니다.
자물쇠에는 홈이 파여있고 열쇠 또한 홈과 돌기 부분이 있습니다.
열쇠는 회전과 이동이 가능하며 열쇠의 돌기부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는
구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는데 영향을 주지 않지만,
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와
자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개 변수로 주어질 때,
열쇠로 자물쇠를 열 수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성 해주세요

[제한 사항]
    - key는 M x M(3 <= M <=20, M은 자연수) 크기 2차원 배열입니다.
    - lock은 N x N(3 <= N <= 20, N은 자연수) 크기 2차원 배열입니다.
    - M은 항상 N 이하입니다.
    - key와 lock의 원소는 0 또는 1로 이루어져 있습니다. 이때 0은 홈부분, 1은 돌기 부분을 나타냅니다.

[입출력 예시]
key                         lock                        result
[[0,0,0],[1,0,0],[0,1,1]]   [[1,1,1],[1,1,0],[1,0,1]]   true

[입출력 예시에 대한 설명]
key를 시계방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히
모두 채울 수 있습니다.
key         lock
[0,0,0]     [1,1,1]
[1,0,0]     [1,1,0]
[0,1,1]     [1,0,1]
'''

# 90도 회전 함수
def rotated_90degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠의 중간부분이 모두 1인지 확인하는 함수
def check(new_lock):
    lock_length = len(new_lock) // 3 # 확인범위를 최소화 하기 위함 9*9 다하면 오래걸림
    for i in range(lock_length, lock_length*2): # 딱 정중앙을 확인하려면
        for j in range(lock_length, lock_length*2): # 3나눈거의 처음부터 딱 2배부터 그니까 3~6까
            if new_lock[i][j] != 1: # 0부터 시작하니까 3,4,5확인하는거
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0 * (n*3) for _ in range(n*3)]]
    # 새로운 자물쇠 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotated_90degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        if check(new_lock) == True:
                            return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False