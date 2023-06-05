'''
https://www.acmicpc.net/problem/19941

K가 1인 경우 인접한 햄버거만 먹을 수 있음
식탁의 길이  N
선택 가능 거리 K
햄버거를 먹을 수 있는 사람의 최대 수 를 구하기

1 <= N <= 20000
1 <= K <= 10

사람 P, 햄버거 H
'''

n, k = map(int, input().split())

data = list(input())
count = 0
for i in range(len(data)):
    if data[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0<= j <n and data[j] == 'H':
                count += 1
                data[j] = 0
                break
            
print(count)