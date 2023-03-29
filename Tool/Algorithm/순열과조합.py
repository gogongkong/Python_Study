# 순열과 조합
'''
순열이란
서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것을 의미
nPr이라고 표현
--> nPr = n! / (n-r)!
다만 코딩테스트에서는 해당 경우의 수의 값만 출력하는것이 아닌 모든 경우(사건)을 출력해야 하기도 함
이럴때 사용하는 함수가 "itertools"라이브러리 이다
permutations() 함수를 호출해 나온 결과는 리스트의 형태가 아니기 때문에 list()를 사용하자
'''

# 소스코드
import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))



'''
조합이란
서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것을 의미
nCr이라고 표현
--> nCr = n! / r! * (n-r)!
조합 라이브러리의 이름은 itertools의 combinations()
'''

# 소스코드
import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')