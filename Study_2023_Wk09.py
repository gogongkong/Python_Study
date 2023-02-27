
# '''
# 문제
# 하나의 수열에는 다양한 수가 존재하며, 이런 큰 수는 크기와 상관 없이 무작위로 주어진다. 이 수를 큰수 부터 작은 수까지 내림차순으로 정렬하면되는 문제다. 즉 수열을 내림차순으로 정렬하는 프로그램을 만들면된다.

# 입력
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. 이때 범위는 1 <= N <= 500
# 둘째 줄부터 N + 1 번째 줄 까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하 자연수
# 출력
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분해서 출력하면된다. 동일한 수는 순서상관없다.
# 입력 예시

# 3
# 15
# 27
# 12
# 출력 예시

# 27 25 12
# '''
# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))
# data.sort(reverse= True)

# for i in data:
#     print(i, end=' ')

# '''
# 문제
# N명의 학생의 성적 정보가 주어진다. 
# 형식은 이름 성적 으로 주어지는데 이때 이들의 성적이 낮은 순으로 학생 이름을 출력하는 문제다.

# 입력
# 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
# 두 번째 줄 부터 N+1 번째 줄 까지 학생의 이름 그리고 성적이 공백으로 주어진다. 
# 학생이름 길이는 100이하, 성적은 100이하 자연수로 주어진다.

# 출력
# 모든 학생의 이름을 성적이 낮은 순으로 출력하면된다. 동일한 성적은 자유롭게 출력하면된다.
# [입력 예시]
# 2
# 홍길동 96
# 이순신 78

# [출력 예시]
# 이순신 홍길동
# '''

# n = int(input())
# arr = []
# for i in range(n):
#     data = input().split()
#     arr.append((data[0], int(data[1])))

# arr = sorted(arr, key= lambda student: student[1])

# for student in arr:
#     print(student[0], end=' ')

# '''
# 문제
# 동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는
# 모두 자연수이다

# 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와
# 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다

# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야한다

# N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라

# 예를 들어 N = 5, K = 3이고, 배열 A와 B가 다음과 같다고 해보자

# 배열 A = [1, 2, 5, 4, 3]

# 배열 B = [5, 5, 6, 6, 5]
# 이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다

# 연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기

# 연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기

# 연산 3) 배열 A의 원소 '3'과 배열 B의 원소 '5'를 바꾸기
# 세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다

# 배열 A = [6, 6, 5, 4, 5]

# 배열 B = [3, 5, 1, 2, 5]
# 이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다

# 입력
# 첫 번째 줄: N, K 가 공백으로 구분되어 입력 (1 <= N <= 100,000, 0 <= K <= N)
# 두 번째 줄: 배열 A의 원소들이 공백으로 구분되어 입력 (원소 a < 10,000,000인 자연수)
# 세 번째 줄: 배열 B의 원소들이 공백으로 구분되어 입력 (원소 b < 10,000,000인 자연수)
# 출력
# 최대 K번 바꿔치기 연산을 수행해서 가장 최대의 합을 갖는 A의 모든 원소 값의 합을 출력

# [입력 예시]
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# [출력 예시]
# 26
# '''


# n, k = map(int, input().split())
# arr_a = list(map(int, input().split()))
# arr_b = list(map(int, input().split()))

# arr_a.sort()
# arr_b.sort(reverse=True)

# for i in range(k):
#     if arr_a[i] < arr_b[i]:
#         arr_a[i], arr_b[i] = arr_b[i], arr_b[i]
#     else:
#         break

# result = 0
# for i in arr_a:
#     result += i
# print(result)


# '''
# 순차 탐색-이진 탐색 알고리즘
# 리스트 안에있는 특정한 데이터를 찾기 위해 
# 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# '''

# # 순차 탐색 소스코드 구현
# def sequential_search(n, target, array):
#     # 각 원소를 하나씩 확인하며
#     for i in range(n):
#         # 현재의 원소가 찾고자 하는 원소와 같을 경우
#         if array[i] == target:
#             return i + 1 # 현재의 위치 반환

# print("생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()
# n = int(input_data[0]) # 원소의 갯수
# target = input_data[1] # 찾고자 하는 문자열

# print("앞서 적은 원소 갯수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()

# # 순차 탐색 수행 결과 출력
# print(sequential_search(n, target, array))
# '''
# 입력
# 5 Dongbin
# Hanul Jonggu Dongbin Taeil Sangwook
# '''

# '''
# 이진 탐색
# 내부의 데이터가 정렬 되어 있어야만 사용 할 수 있는 알고리즘
# 이미 정렬 되어 있다면 매우 빠르게 데이터를 찾을 수 있는 장점을 가지고 있음
# 탐색범위를 절반씩 좁혀가며 데이터를 탐색
# --> 3개의 변수 시작, 끝, 중간의 변수를 가짐
# '''

# # 재귀함수를 이용한 이진 탐색 소스코드
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid -1)
#     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#     else:
#         return binary_search(array, target, mid+1, end)
    
# # n(원소의 갯수)과 target(찾고자 하는 문자열)을 입력받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력받기
# array = list(map(int, input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 존재 하지 않습니다.")
# else:
#     print(result+1)



# # 반복문으로 구현한 이진 탐색 소스코드
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 반환
#         if array[mid] == target:
#             return mid
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#         elif array[mid] > target:
#             end = mid -1
#         # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#         else:
#             start = mid +1
#     return None
# # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력받기
# array = list(map(int, input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 존재 하지 않습니다.")
# else:
#     print(result+1)

# '''
# 입력
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# 출력
# 4
# '''

# '''
# sys 라이브러리를 이용한 한줄 입력받아 출력하는 소스코드
# sys 라이브러리를 사용할 때는 한줄 입력 받고나서 rstrip()함수를 꼭 호출해야만 한다.
# 소스코드에 readline()으로 입력하면 입력 후 엔터(Enter)가 줄바꿈 기호로 입력되는데,
# 이 공백문자를 제거 하려면 rstrip()함수를 사용해야 한다.
# '''
# import sys
# # 하나의 문자열 데이터 입력받기
# input_data = sys.stdin.readline().rstrip()
# # input_data = sys.stdin.readline()

# # 입력받은 문자열 그대로 출력
# print(input_data)


# '''
# 7-2 실전문제 부품찾기
# 문제
# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 
# 어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
# 예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

# N=5
# [8, 3, 7, 9, 2]
# 손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

# M=3
# [5, 7, 9]
# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 
# 없으면 no를 출력한다. 구분은 공백으로 한다.

# 입력
# 첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 
# 이때 정수는 1보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 
# 이때 정수는 1보다 크고 10억 이하이다.
# 출력
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
# [입력 예시]
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# [출력 예시]
# no yes yes
# '''

# # 풀이 (이진탐색 - 재귀함수)
# n = int(input())
# stack = list(map(int, input().split()))
# stack.sort()
# m = int(input())
# c_stack = list(map(int, input().split()))
# c_stack.sort()

# def search(array, target, start, end):
#     if start > end:
#         return print("no", end= ' ')
#     mid = (start+end) // 2
#     if array[mid] == target:
#         return print("yes", end=' ')
#     elif array[mid] > target:
#         search(array, target, start, mid-1)
#     else:
#         search(array, target, mid+1, end)
    

# for target in c_stack:
#     search(stack, target, 0, n-1)


