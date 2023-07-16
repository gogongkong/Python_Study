'''
https://www.acmicpc.net/problem/1758
'''

n = int(input())

datas = []
for _ in range(n):
    datas.append(int(input()))

datas.sort(reverse=True)

result = []
for i in range(len(datas)):
    if datas[i] -(i) >= 0:
        result.append(datas[i] -(i))

print(sum(result))