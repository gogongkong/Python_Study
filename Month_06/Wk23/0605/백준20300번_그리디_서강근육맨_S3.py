'''
https://www.acmicpc.net/problem/20300

PT 한번에 최대 2개의 운동기구 선택 가능

PT를 받을 때마다 이전에 사용하지 않았던 기구 사용하기로

되도록 2개의 운동기구 사용

예를 들어 10개의 운동기구가 있을 때 5회의 PT로 모든 기구 사용 가능
9개의 운동기구의 경우 PT 5회를 받지만 마지막 PT에는 1개의 기구만 사용함

단 기구별 근손실이 다르기 때문에 각 PT당 근손실 M을 넘지 않도록 해야 함
PT당 근손실 정도는 두 운동기구의 근손실 정도의 합

1 <= N <= 10000 
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()
result = []

if n % 2 == 1:
    result.append(max(data))
    data.remove(max(data))
    n-=1

for i in range(len(data) // 2):
    result.append(data[i] + data[-i-1])

print(max(result))