'''
https://www.acmicpc.net/problem/11047
'''

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0

while k != 0:
    for coin in coins:
        if k >= coin:
            count += k//coin
            k -= (k//coin) * coin

print(count)

