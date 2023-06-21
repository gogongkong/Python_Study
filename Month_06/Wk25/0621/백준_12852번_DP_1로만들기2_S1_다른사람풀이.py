'''
https://www.acmicpc.net/problem/12852
'''

x = int(input())

d = [i for i in range(x+1)]
d[1] = 0
result = [i for i in range(x+1)]
result[1] = 0

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    result[i] = i-1
    if i % 3 == 0 and d[i] > d[i //3] + 1:
        d[i] = d[i//3] + 1
        result[i] = i // 3
        
    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        result[i] = i // 2
        
print(d[x])
print(x, end=' ')

num = x
while result[num] != 0:
    print(result[num], end=' ')
    num = result[num]
