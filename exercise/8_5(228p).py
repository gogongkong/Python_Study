'''
문제
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 
이때 각 화폐는 몇 개라도 사용할 수 있으며, 
사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

입력
첫째 줄에 N,M이 주어진다(1<= N <= 100, 1<= M <= 10,000)
이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.
출력
첫째 줄에 경우의 수 X를 출력한다.(불가능할 때는 -1을 출력한다)

[입력 예시]
2 15
2
3

[출력 예시]
5
'''




















# 풀이
# 정수 N, M 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
arr = []
for i in range(n):
    arr.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍(보텀업) 진행
d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001: # (i -k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-arr[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])