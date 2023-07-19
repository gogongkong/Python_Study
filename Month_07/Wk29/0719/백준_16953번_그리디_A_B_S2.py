'''
https://www.acmicpc.net/problem/16953
'''

# 풀이 접근
# a --> b가 아니라
# b --> a로 풀어보기

a, b = map(int, input().split())

count = 1

while a != b:
    if a == b:
        break
    elif (b % 10 != 1 and b % 2 != 0) or b < a:
        count = -1
        break
    else:
        if b % 10 == 1:
            b = b // 10
            count += 1
        else:
            b = b // 2
            count += 1

print(count)