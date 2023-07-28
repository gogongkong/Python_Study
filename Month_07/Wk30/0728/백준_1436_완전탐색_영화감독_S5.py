'''
https://www.acmicpc.net/problem/1436
'''

n = int(input())

num = 1
check = 0
while 1:
    if check == n:
        print(num-1)
        break
    if "666" in str(num):
        check += 1

    num += 1
