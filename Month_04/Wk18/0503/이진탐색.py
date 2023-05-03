'''
이진 탐색

- 순차 탐색
"리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법"
보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
순차 탐색은 이름처럼 순차로 데이터를 탐색한다는 의미이다.
'''
# 순차 탐색 소스코드
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환

print("생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0]) # 원소의 갯수
target = input_data[1] # 찾고자하는 문자열

print("앞서 적은 원소 갯수만큼 문자열을 입력하세요, 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
