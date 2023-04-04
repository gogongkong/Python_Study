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