'''
https://www.acmicpc.net/problem/6236
'''

n, m = map(int, input().split())
datas = [int(input()) for _ in range(n)] # i번째 날에 이용할 금액

start, end = min(datas), sum(datas)

while start <= end:
    mid = (start + end) // 2
    count = 1 # 처음엔 무조건 돈을 인출
    coin = mid
    for data in datas:
        if coin < data:
            coin = mid
            count +=1
        coin -= data
    
    if count > m or mid < max(datas):
        start = mid + 1
    else:
        end = mid -1
        K = mid

print(K)