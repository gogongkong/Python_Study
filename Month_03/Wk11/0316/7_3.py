'''
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때, 
적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.
입력 조건
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. 
(1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)

둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 
손님은 필요한 양만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0 이다.

출력 조건
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

[입력 예시]
4 6
19 15 10 17

[출력 예시]
15

전형적인 이진 탐색 문제이자 파라메트릭 서치 유형의 문제이다.
파라메트릭 서치(Parametric Search)는 최적화 문제를 결정문제(yes or no로 답하는 문제)로 
바꾸어 해결하는 방법

적절한 높이를 찾을 때 까지 절단기의 높이H를 반복해서 조정하는것
그 후 현재 높이로 자르면 만족하는가 --> 예 아니오 로 탐색 범위를 좁혀 나갈 수 있음

Step 1
시작점은 0, 끝점을 가장 긴 떡의 길이(19)로 설정
중간점 9를 H로 정하면 (10 + 6 + 1 + 8) = 25 -> 필요한 길이보다 크기때문에 시작점을 증가

Step 2
시작점을 10으로 옮긴다. 중간점은 14 (5 + 1 + 3) = 9 --> 시작점 증가

Step 3
시작점을 15로 옮긴다. 중간점은 17 (2) --> 시작점 감소

Step 4
시작점 15(Step2의 중간점인 14를 확인했기 때문) 중간점 15 --> (4 + 2) = 6 
'''

# 떡의 갯수 N, 떡의 길이 M 입력
n, target = map(int, input().split())

arr = list(map(int,input().split()))
start = 0 
end = max(arr)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid
    if total < target:
        end = mid -1
    else:
        result = mid
        start = mid + 1  

print(result)