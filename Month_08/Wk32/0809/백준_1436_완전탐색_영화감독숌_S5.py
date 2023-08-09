'''
https://www.acmicpc.net/problem/1436
'''

n = int(input())

count = 0
number = 0

while 1:
    if count == n:
        print(number-1)
        break    
    if "666" in str(number):
        count +=1

    number += 1



