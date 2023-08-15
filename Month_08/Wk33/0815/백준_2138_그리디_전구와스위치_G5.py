'''
https://www.acmicpc.net/problem/2138
'''

# 첫번째 전구를 키는지 안키는지 두가지 케이스로 나눠서 풀이
# 지나간 전구는 건들지 않는다 == 불가능한것이 가능해지지 않을 뿐더러 횟수만 증가한다.
# 두번째 전구부터 이전 전구의 상태가 희망하는 상태와 같은지 확인 후 다르다면 스위치를 누르기
# ==> 이전 전구만 비교하는 이유는 다음 루프에서 다음전구를 비교하기 때문이다.
# 참조 : https://javaiyagi.tistory.com/593

n = int(input())

data = list(map(int, input()))
result = list(map(int, input()))

def change(number):
    if number == 0:
        number = 1
    else:
        number = 0
    return number

def switch(data, cnt):
    count = cnt
    if count == 1:
        data[0] = change(data[0])
        data[1] = change(data[1])
    for i in range(1, n):
        if data[i-1] != result[i-1]:
            count +=1
            data[i-1] = change(data[i-1])
            data[i] = change(data[i])
            if i != n-1:
                data[i+1] = change(data[i+1])
    if data == result:
        return count
    else:
        return -1

result1 = switch(data[:], 0)
result2 = switch(data[:], 1)

if result1 >= 0 and result2 >= 0:
    print(min(result1, result2))

elif result1 >=0 and result2 <0:
    print(result1)

elif result1 <0 and result2 >= 0:
    print(result2)

else:
    print(-1)
