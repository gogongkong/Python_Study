'''
https://www.acmicpc.net/problem/9465
'''

tc = int(input())
result = []

for _ in range(tc):
    n = int(input())

    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    for i in range(1,n):
        if i == 1:
            s1[i] += s2[0]
            s2[i] += s1[0]
        
        else:
            s1[i] = max(s2[i-1], s2[i-2]) + s1[i]
            s2[i] = max(s1[i-1], s1[i-2]) + s2[i]
    
    result.append(max(s1[-1], s2[-1]))

print(result)

