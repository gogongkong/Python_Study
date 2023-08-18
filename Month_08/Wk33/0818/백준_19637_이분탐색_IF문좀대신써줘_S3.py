'''
https://www.acmicpc.net/problem/19637
'''



n, m = map(int, input().split())
status = [input().split() for _ in range(n)]
datas = [int(input()) for _ in range(m)]
answer = [] # 정답을 담을 변수

for data in datas:
    result = 0
    start, end = 0 , len(status)-1 # 시작과 끝 정의

    while start <= end:
        mid = (start + end) // 2

        if data <= int(status[mid][1]):
            end = mid - 1
            result = end
        else:
            start = mid + 1

    answer.append(result)

for i in answer:
    print(status[i+1][0])