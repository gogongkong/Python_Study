'''
https://www.acmicpc.net/problem/16953
'''

a, b = map(int, input().split())
result = 1

while a != b:
    if a == b:
        break
    elif ( b%10 != 1 and b%2 != 0) or b < a :
        result = -1
        break
    else:
        if b % 10 == 1:
            b =b//10
            result += 1
        elif b % 10 != 1:
            b = b // 2
            result +=1

print(result)
