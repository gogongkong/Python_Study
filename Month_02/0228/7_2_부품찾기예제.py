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

# 재귀함수를 이용하여 풀이
n = int(input())
arr_a = list(map(int, input().split()))
arr_a.sort()
m = int(input())
arr_b = list(map(int, input().split()))
arr_b.sort()

def search(arr, target, start, end):
    if start > end:
        return print("no", end=' ')
    mid = (start + end) // 2
    if arr[mid] == target:
        return print("yes", end= ' ')
    elif arr[mid] > target:
        search(arr, target, start, mid-1)
    else:
        search(arr, target, mid+1, end)

for target in arr_b:
    result = search(arr_a, target, arr_a, arr_a[n-1])

# 반복문을 이용한 풀이
n = int(input())
arr_a = list(map(int, input().split()))
arr_a.sort()
m = int(input())
arr_b = list(map(int, input().split()))
arr_b.sort()

def search(arr, target, start, end):
    while start <= end:
        mid = ( start + end ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in arr_b:
    result = search(arr_a, i, 0, n-1)
    if result != None:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')


# 계수정렬을 이용한 풀이
n = int(input())
arr = [0] * 1000001

for i in input().split():
    arr[int(i)] = 1

m = int(input())
arr_c = list(map(int, input().split()))

for i in arr_c:
    if arr[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end= ' ')