'''
https://www.acmicpc.net/problem/2138
'''

# 첫번째 전구를 키는지 안키는지 두가지 케이스로 나눠서 풀이
# 지나간 전구는 건들지 않는다 == 불가능한것이 가능해지지 않을 뿐더러 횟수만 증가한다.
# 두번째 전구부터 이전 전구의 상태가 희망하는 상태와 같은지 확인 후 다르다면 스위치를 누르기
# ==> 이전 전구만 비교하는 이유는 다음 루프에서 다음전구를 비교하기 때문이다.
# 참조 : https://javaiyagi.tistory.com/593


n = int(input())

data = list(map(int, input())) # 주어진 전구의 상태
hope = list(map(int, input())) # 원하는 전구의 상태

# state change 함수 1 -> 0, 0 -> 1
def change_state(number):
    if number == 0:
        number += 1
    elif number == 1:
        number -= 1
    return number

def change_procedure(data, hope, cnt):
    count = cnt # 첫번째 스위치를 켰다면 cnt가 1인것을 처리 안켰다면 0이 될것임
    
    if count == 1:
        data[0] = change_state(data[0])
        data[1] = change_state(data[1])

    for i in range(1, n):
        if data[i-1] != hope[i-1]:
            for k in (i-1, i, i+1):
                if k < n:
                    data[k] = change_state(data[k])
            count +=1

    if data == hope:
        return count
    elif data != hope:
        return -1

result1 = change_procedure(data[:], hope, 0)
result2 = change_procedure(data[:], hope, 1)

if result1 >= 0 and result2 >=0:
    print(min(result1, result2))
elif result1 >=0 and result2 == -1:
    print(result1)
elif result1 == -1 and result2 >= 0:
    print(result2)
elif result1 == -1 and result2 == -1:
    print(-1)


