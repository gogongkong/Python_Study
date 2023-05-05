'''
오늘 동빈이는 여행가는 부모님을 대신해서 떡집일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm으로 지정하면
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될것이다. 잘린 떡의 길이는 순서대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의
최댓값을 구하는 프로그램을 작성하시오. 

입력 조건
    - 첫째 줄의 떡의 갯수 N과 요청한 떡의 길이 M이 주어진다.
    - (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
    - 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을
    사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

출력 조건
    - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

입력 예시
4 6
19 15 10 17

출력 예시
15
'''

n, target = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(data, target, start, end):
    if start > end:
        return print('-1')
    mid = (start + end) // 2
    check = 0
    for i in data:
        if i - mid > 0:
            check += i - mid
    
    if check == target:
        return print(mid)
    elif check > target:
        binary_search(data, target, mid +1, end)
    else:
        binary_search(data, target, start, mid - 1)

binary_search(data, target, 0, max(data))