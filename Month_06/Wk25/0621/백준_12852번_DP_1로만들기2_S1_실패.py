'''
https://www.acmicpc.net/problem/12852
'''

x = int(input())

d = [0] * (x+1)

result = [[1,i] for i in range(x+1)]

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    result[i].append(i-1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3]+1)
        result[i].append(d[i//3])
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2]+1)
        result[i].append(d[i//2])
print(d[x])
#print(result)
result2 = dict.fromkeys(result[x])
result2 = list(result2)
print(result2)
result2.sort(reverse= True)

for i in result2:
    if i == 0:
        continue
    else:
        print(i, end=' ')