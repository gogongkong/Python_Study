'''
https://www.acmicpc.net/problem/1436
'''

n = int(input())
result = 0
count = 0

while 1:
    if result == n:
        print(count-1)
        break
    if "666" in str(count):
        result += 1
    
    count += 1

