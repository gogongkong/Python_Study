# 피보나치 함수 소스코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))

'''
단점
N이 커지면 커질수록 수행시간이 기하급수적으로 늘어남
N= 30이면 10억가량의 연산을 수행해야 함
원인 : N이 커질수록 반복해서 동일한 연산을 하는경우가 늘어남 (213p 그림 참고)
해결 : 다이나믹 프로그래밍 단, 항상 사용은 불가능 일정 조건을 만족해야 사용가능
    조건 1. 큰 문제를 작은 문제로 나눌 수 있다.
    조건 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다
피보나치 수열은 이러한 조건을 만족하는 대표 문제이다.
이 문제를 메모이제이션 기법을 사용해서 해결해보자.
    메모이제이션 : 다이나믹 프로그래밍을 구현하는 방법 중 한종류
                한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면
                메모한 결과를 그대로 가져오는 기법( 캐싱이라고도 함 )'''

# 메모이제이션 기법을 이용한 피보나치 수열 소스 코드( 재귀적 )

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건( 1 혹은 2일때 1을 반환 )
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

'''
정리
다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한번씩만 풀어 문제를 효율적으로
해결하는 알고리즘 기법.
퀵정렬에서도 소개된 적이 있음. ( 분할정복 알고리즘 )
다이나믹 프로그래밍과 분할정복의 차이는 다이나믹프로그래밍은 문제들이 서로 영향을 미치고 있다는점.

퀵정렬
한번 기준원소가 자리를 잡으면 그 위치는 바뀌지 않고 피벗값을 다시 처리하는부분 문제는 존재X

다이나믹 프로그래밍
한 번 해결했던 문제를 다시 해결하는것이 특징 그렇기에 한번 해결한 문제의 답을 저장하고 
이 문제는 이미 해결이 된것이니 다시 해결할 필요가 없다고 반환하는 것
시간복잡도는 O(N)이다. 이유는 한번 구한 결과는 다시 구해지지 않기 때문
'''
# 호출되는 함수 확인하는 소스코드
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end= ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)

'''
재귀함수를 이용하여 다이나믹 프로그래밍 소스 코드를 작성하는 방법을 
탑다운(Top-Down) 방식이라고 말한다.
반면에 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 호출한다고 하여
보텀업(Bottom-Up) 방식이라고 말한다.
'''
print("\n")
# 피보나치 수열 소스코드 (반복적 - 보텀업)

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

'''
문제 해결을 위한 첫 번재 단계는 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는것
특정한 문제를 완전 탐색으로 접근 했을 때 시간이 오래걸린다면 다이나믹을 적용할 수 있는지
해결하고자 하는 부분의 문제들의 중복 여부를 확인해보기
단순히 재귀함수로 비효율적으로 작성한 뒤에(탑다운) 작은 문제에서 구한 답이 큰문제에서 
그대로 사용이 가능하면, 즉 메모이제이션을 적용할 수 있으면 코드를 개선하는 방법도 좋은
아이디어임.
앞서 다룬 피보나치 수열처럼 먼저 재귀함수를 작성한 뒤 나중에 메모이제이션 기법을 적용하는것도
좋은 방법.
그러나 가능하다면 재귀함수보단 반복문을 이용한 보텀업을 사용하기
시스템상 재귀함수의 스택 크기가 한정되어 있을 수 있음.
스택크기가 한정되어 recursion depth 에러가 발생하면 재귀제한을 완화할 수 있는
sys 라이브러리의 setrecursionlimit() 함수를 호출하여 완화가 가능하다는점을 기억하자.
'''

