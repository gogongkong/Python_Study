'''
https://www.acmicpc.net/problem/12852
'''

x = int(input())

d = [0] * (x+1)

result = [[1,i] for i in range(x+1)]

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3]+1)
        
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2]+1)
        
print(d[x])

result = [x]
now = x
temp = d[x] -1

for i in range(x, 0, -1):
    if d[i] == temp and (i + 1 == now or i *2 == now or i * 3 == now):
        now = i
        result.append(i)
        temp -= 1

print(*result)