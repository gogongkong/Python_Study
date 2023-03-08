'''
7-2 실전문제 부품찾기
문제
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 
어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

N=5
[8, 3, 7, 9, 2]
손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

M=3
[5, 7, 9]
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 
없으면 no를 출력한다. 구분은 공백으로 한다.

입력
첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 
이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 
이때 정수는 1보다 크고 10억 이하이다.
출력
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
[입력 예시]
5
8 3 7 9 2
3
5 7 9

[출력 예시]
no yes yes
'''
# 이진탐색 풀이
def search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if arr[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 가게의 부품 갯수 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분 하여 입력
arr = map(int, input().split())
arr.sort() # 오름차순 정렬
# 손님 요청 부품 갯수 입력
m = int(input())
# 부품 종류 입력
arr_c = map(int, input().split())
for i in arr_c:
    # 해당 부품이 존재하는지 확인
    result = search(arr, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# INF = int(1e9) # 무한을 정의
# # 매장의 부품 갯수 입력
# n = int(input())

# arr = [0] * 100001
# for i in input().split():
#     arr[int(i)] = INF

# m = int(input())
# arr_b = list(map(int, input().split()))

# for i in arr_b:
#     if arr[i] == INF:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


