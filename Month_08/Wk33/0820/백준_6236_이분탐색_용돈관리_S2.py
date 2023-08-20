'''
https://www.acmicpc.net/problem/6236
'''

n,m = map(int, input().split())

coins = [int(input()) for _ in range(n)]

start, end = min(coins), sum(coins)

while start <= end:
    mid = (start + end) // 2
    count = 1 # 첫번째는 무조건 인출
    money = mid
    for coin in coins:
        if money < coin:
            money = mid
            count +=1
        money -= coin
    
    if count > m or mid < max(coins):
        start = mid +1
    else:
        end = mid -1
        result = mid
        
print(result)