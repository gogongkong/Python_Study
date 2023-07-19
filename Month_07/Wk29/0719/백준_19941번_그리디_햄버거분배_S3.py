'''
https://www.acmicpc.net/problem/19941
'''

# table의 크기 N, 선택가능한 범위 K 입력
n, k = map(int, input().split())

# table의 구성 입력
table = list(input())
# 정답을 담을 변수 count
count = 0

for i in range(n):
    if table[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0<= j < n and table[j] == 'H':
                count +=1
                table[j] = 'X'
                break
            
print(count)