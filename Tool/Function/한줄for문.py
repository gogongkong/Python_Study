temp = [i for i in range(7)]
print(temp) # [0, 1, 2, 3, 4, 5, 6]
'''
기본형태는 '[결과 for 반복문]'으로 한줄에 가능하다.
위와같은 '결과 for 반복문'을 리스트 안에 중첩하여 다중 for문이 가능하다.
'''

temp = [i * j for i in range(1, 3) for j in range(1, 4)]
print(temp) # [1, 2, 3, 2, 4, 6]

'''
먼저 나올수록 상위 for문이다.

for문을 한줄에 쓰면서 if 조건문을 같이 적용할 수 있다.
'''

# i가 홀수 일 때 i * j 아니면 'pass'
temp = [i * j if i % 2 == 1 else 'pass' for i in range(1, 5) for j in range(1, 4)]
print(temp) # [1, 2, 3, 'pass', 'pass', 'pass', 3, 6, 9, 'pass', 'pass', 'pass']

'''
위 형태는 고정으로 else가 필수이다. 만약 else가 필요 없다면 if 조건문을 마지막에 써준다.
'''

temp = [i for i in range(0, 10) if i % 2 == 1]
print(temp)
