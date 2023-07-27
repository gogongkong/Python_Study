'''
https://www.acmicpc.net/problem/1018
'''

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(input())

result = []

for a in range(n-7):
    for b in range(m-7):

        first = 0
        sec = 0

        for i in range(a, a+8):
            for j in range(b, b+8):

                if (i +j) % 2 == 0:
                    if data[i][j] != "W":
                        first += 1
                    if data[i][j] != "B":
                        sec += 1
                
                else:
                    if data[i][j] != "B":
                        first += 1
                    if data[i][j] != "W":
                        sec += 1
        
        result.append(min(first, sec))

print(min(result))
