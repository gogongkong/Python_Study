'''
dictionary : {} 중괄호를 사용
- 딕셔너리 {Dictionary}는 사전형태의 자료구조이다
- Key 와 Value으로 구분되며, Key를 사용하여 값에 접근 가능하다.
- 배열이나 튜플처럼 인덱스를 활용하여 Value 에 접근할 수 없다. 
- Key 를 사용하여 값을 추가, 변경, 삭제가 가능하다. 
- 동일한 Key 자료는 존재할 수 없다. 

주목할 점은 Key를 이용하여 접근이 가능하다는점
'''
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]

data = {n:y for n,y in zip(name, yearning)}

print(data) # 출력 결과 --> {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
print(data['may']) # 출력 결과 --> 5

'''
예시 코드처럼 키값을 이용하여 접근이 가능하다

예제 : https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''

# 2023_09_03 좀더 확실히 알기 위해 공부를 해보자

# dictionary는 Key와 Value로 구분되어 있음
dic = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1118'}
# 위의 key는 name, phone, birth로 value는 pey, 010-9999-1234, 1118이 된다.

# 딕셔너리 쌍 추가, 삭제하기
a = {1 : 'a'}
print(a)
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)

# 요소 삭제하기
# 딕셔너리의 요소를 삭제하는 방법은 del 함수를 이용하면된다
del a['name']
print(a)


# 딕셔너리에서 Key를 이용해 Value를 얻는방법
grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey'])
print(grade['julliet'])

'''리스트나 튜플, 문자열은 요솟값을 얻고자 할 때 인덱싱이나 슬라이싱이 필요하지만
딕셔너리는 단 1가지 방법뿐이다 == key를 이용해서 value를 구하는 방법'''

# 딕셔너리를 만들 때 주의사항
# Key는 고유한 값이므로 중복이 되면 하나를 제외한 나머지 값은 모두 무시된다.
# 키가 2개 존재하는 경우 하나는 무시된다.

# 또하나의 주의 사항은 Key에 리스트는 쓸 수 없다.
# 하지만 튜플은 Key로 쓸 수 있다.
# Key로 쓸 수 있는지 없는지 판단은 Key값이 변할 수 있는지 불변인지에 달려있다.
# 리스트는 그 값이 변할 수 있기 때문에 쓸 수 없다.
'''a = {[1,2] : 'hi'}'''

# Key 리스트 만들기 - keys
# .keys()는 dict_keys로 반환을 한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
b = a.keys()
print(b)
# 여기서 리스트로 변환하려면
c = list(a.keys())
print(c)

# Value로 리스트를 만들기 values
c = list(a.values())
print(c)

# key와 value를 모두 지우러면 a.clear()를 하면된다
a.clear()
print(a)



# key로 value얻기 - get
# get(x) 함수는 x라는 key에 대응하는 value를 리턴한다.
# a.get('name')은 a['name']과 동일한 결과값을 리턴합니다.
# 다만 다른점은 아무것도 없는것을 get을 쓰면 None이 리턴되지만 a[]를 사용하면 오류를 발생시킨다.
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get('nokey'))

# 해당 key가 딕셔너리 안에 있는지 확인 - in
print('name' in a)
print('email' in a)

