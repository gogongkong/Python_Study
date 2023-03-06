'''
첫째 줄에 N (2 ≤ N ≤ 1000), M (1 ≤ M ≤ 10000), K(1 ≤ K ≤ 10000)의 자연수가 주어지며, 
각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 
단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다

[입력 예시]
5 8 3
2 4 5 4 6
[출력 예시]
46
'''

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

first = arr[0]
sec = arr[1]

count = 0
while True:
   
    for i in range(k):
        count += first
        m -= 1

    count += sec
    m-= 1

    if m == 0:
        break

print(count)