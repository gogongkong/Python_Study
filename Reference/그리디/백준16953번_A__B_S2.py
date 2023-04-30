'''
https://www.acmicpc.net/problem/16953

문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
2 162
예제 출력 1 
5
2 → 4 → 8 → 81 → 162

예제 입력 2 
4 42
예제 출력 2 
-1
예제 입력 3 
100 40021
예제 출력 3 
5
100 → 200 → 2001 → 4002 → 40021
'''

a, b = map(int, input().split())

count = 1

while a != b:
    if b == a:
        break
    elif (b%10 != 1 and b % 2 != 0) or b < a:
        count = -1
        break
    else:
        if b % 10 == 1:
            b = b//10
            count += 1
        else:
            b = b//2
            count += 1
print(count)