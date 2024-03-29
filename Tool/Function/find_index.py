'''
A.find(찾을 문자)
A.find(찾을 문자, 시작 index)
A.find(찾을 문자, 시작 index, 끝 index)

첫 번째 인자
    - 찾을 문자열 혹은 찾을 문자
두 번째 인자
    - 문자를 찾을 때 어디서부터 찾을지 시작하는 index, 생략시 0
세 번째 인자
    - 문자를 찾을 때 어디까지 찾을지 끝을 정하는 index, 생략시 마지막 index

find 메서드는 "찾을 문자" 혹은 "찾을 문자열"이 존재하는지 확인하고,
찾는 문자가 "존재한다면 해당 위치의 index를 반환하고"
찾는 문자가 "존재하지 않는다면 -1을 반환한다"

만약에 찾는 문자나 문자열이 "여러개"있다면 맨 처음 찾은 문자의 index를 반환한다.

index 또한 사용법은 동일하나 다른점이라면
"찾는 문자나 문자열이 없다면 index는 ValueError가 발생한다."

index, find 둘다 리스트, 튜플, 딕셔너리 자료형 에서는 사용이 불가능하다.
사용시 AttributeError가 발생한다.
'''

# find 함수 예제
# https://www.acmicpc.net/problem/10809
