'''
https://www.acmicpc.net/problem/9017
'''

'''
15
1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
'''

tc = int(input())

for _ in range(tc):
    n = int(input())
    team = list(map(int, input().split()))

    manage = {}
    for i in range(n):
        if team[i] not in manage:
            manage[team[i]] = [1, [], 0] # 팀번호, 선수별 점수, 점수 합
        else:
            manage[team[i]][0] += 1
    check = set(k for k, v in manage.items() if v[0] < 6)

    grade = 1
    for i in range(n):
        # 점수 계산에서 제외할 선수가 아니라면
        if team[i] not in check:
            manage[team[i]][1].append(grade)
            # 점수를 더하는것은 상위 4명까지
            if len(manage[team[i]][1]) <= 4:
                manage[team[i]][2] += grade
            grade += 1
    answer = []
    for k, v in manage.items():
        if len(v[1]) != 0 and v[2] != 0:
            answer.append([k,v[1][4], v[2]])
    a = sorted(answer, key=lambda x : (x[2], x[1]))
    print(a[0][0])