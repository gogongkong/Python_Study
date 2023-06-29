'''
https://www.acmicpc.net/problem/16953
'''

A, B = map(int, input().split())
count = 1 # 최솟값 + 1이 정답이므로 미리 1부터 시작

while B != A:
    if B == A:
        break
    elif (B % 10 != 1 and B % 2 != 0) or B < A:
        count = -1
        break
    else:
        if B % 10 == 1:
            B = B // 10
            count += 1
        else:
            B = B // 2
            count += 1

print(count)
