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

'''
생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요
5 Dongbin 
앞서 적은 원소 갯수만큼 문자열을 입력하세요, 구분은 띄어쓰기 한 칸으로 합니다.
Hanul Jonggu Dongbin San sma
3

순차 탐색은 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징이다.
따라서 데이터의 갯수가 N개일때 최대 N번의 비교연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N)이다.
'''

'''
이진 탐색 : 반으로 쪼개면서 탐색하기
이진탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
데이터가 무작위일때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있다.
이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.

이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점 그리고 중간점이다.
" 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 반복적으로 비교"해서
원하는 데이터를 찾는 게 이진 탐색 과정이다.

이진 탐색은 한번 확인할 때마다 확인하는 원소가 절반으로 줄어든다는 점에서 시간복잡도가 O(logN)이다.
절반씩 데이터를 줄어들도록 만든다는 점은 퀵정렬과 공통점이 있다.
이진 탐색을 구현하는 방법에는 2가지가 있는데 하나는 재귀함수를 이용하는 방법.
또하나는 단순하게 반복문을 이용하는 방법이다.
'''

# 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스를 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 갯수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

'''
mid = (start + end) //2 는 중간점을 의미한다.
2로 나눈 몫만 구하기 위해 몫 연산자(//)를 사용한 것이다.
'''

# 반복문으로 구현한 이진 탐색 소스코드
def binary_search_for(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] < target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 갯수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_for(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


'''
트리 자료구조
이진 탐색은 조건이 데이터 정렬이다.
예를 들어 동작하는 프로그램에서 데이터를 정렬해두는 경우가 많으므로 이진 탐색을 효과적으로 사용할 수 있다.
데이터 베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어있다.
따라서 데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, 이진 탐색과 유사한 방법을 이용해 탐색을 항상
빠르게 수행하도록 설계되어 있어서 데이터가 많아도 탐색하는 속도가 빠르다.

트리 자료구조는 노드와 노드의 연결로 표현하며 여기에서 노드는 정보의 단위로서 어떠한 정보를 가지고 있는
개체로 이해할 수 있다.
트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템 같은곳에서 많은 양의 데이터를
관리하기 위한 목적으로 사용된다.

트리 자료구조의 몇가지 주요한 특징
    - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
    - 트리의 최상단 노드를 루트 노드라고 한다.
    - 트리의 최하단 노드를 단말 노드라고 한다.
    - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
    - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

이진 탐색 트리
트리 자료구조 중에서 가장 간단한 형태가 이진 탐색트리이다.
이진 탐색 트리란 이진 탐색이 동작 할 수 있도록 고안된, 효울적인 탐색이 가능한 자료 구조다.

보톰 이진탐색트리는 다음과 같은 특징이 있다.
    - 부모 노드보다 왼쪽 자식 노드가 작다.
    - 부모 노드보다 오른쪽 자식 노드가 크다.
간단하게 표현하면 왼쪽 자식노드 < 부모 노드 < 오른쪽 자식노드 가 성립한다.

빠르게 입력받기
이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
예를 들어 데이터의 갯수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색을 의심하다.
그렇기 때문에 입력을 빠르게 받을 필요가 있고 그 코드는 아래와 같다.
'''
import sys
input_data = sys.stdin.readline().rstrip()

'''
sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip()함수를 꼭 호출해야 한다.
소스 코드에 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백문자를 제거하려면
rstrip()함수를 사용해야 한다.
'''
