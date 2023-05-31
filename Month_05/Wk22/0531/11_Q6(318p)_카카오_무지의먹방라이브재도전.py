'''
무지의 먹방 라이브
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42891
평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어졌고 고민 끝에 카카오TV 라이브 방송을 하기로 마음 먹었습니다.
그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 다음과 같이 독특한 방식을 생각해 냈습니다.
회전판에 먹어야 할 N개의 음식이 있습니다.
각 음식에는 1부터 N까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요됩니다.
무지는 다음과 같은 방법으로 음식을 섭취합니다.
    1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
    2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
    3. 무지는 음식하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
        다음 음식이랑, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말합니다.
    4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정합니다.
무지가 먹방을 시작한지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었습니다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 합니다.
각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개 변수로 주어질 때
몇번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성 하세요

[제한 사항]
    - food_times는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열입니다.
    - K는 방송이 중단된 시간을 나타냅니다.
    - 만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 됩니다.

[정확성 테스트 제한 사항]
    - food_times의 길이는 1이상 2000이하입니다.
    - food_times의 원소는 1이상 1000이하 자연수입니다.
    - K는 1이상 2,000,000이하의 자연수 입니다.

[효율성 테스트 제한 사항]
    - food_times의 길이는 1 이상 200,000 이하입니다.
    - food_times의 원소는 1 이상 100,000,000이하의 자연수 입니다.
    - K는 1 이상 2 x 10^13 이하의 자연수 입니다.

[입출력 예시]
food_times      K       result
[3,1,2]         5       1

[입출력 예시에 대한 설명]
0 ~ 1초 동안에 1번 음식을 섭취한다. 남은시간은 [2,1,2] 입니다.
1 ~ 2초 동안 2번 음식을 섭취한다. 남은시간은 [2,0,2] 입니다.
2 ~ 3초 동안 3번 음식을 섭취한다. 남은시간은 [2,0,1] 입니다.
3 ~ 4초 동안 1번 음식을 섭취한다. 남은시간은 [1,0,1] 입니다.
4 ~ 5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은[1,0,0]입니다.
5초에서 네트워크 장애가 발생 했습니다. 1번 음식을 섭취해야 할 때 중단되었으므로, 
장애 복구 후에 1번 음식부터 다시 먹기 시작하면 됩니다.
''' 

'''
풀이
이 문제는, 모든 음식을 시간 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을 사용해 해결할 수 있습니다.
이를 위해 우선순위 큐가 사용됩니다.
중요한 개념은 아래와 같습니다.
예를 들어, 3가지 음식의 소요 시간이 [4, 6, 8] 이라면,
첫 번째 음식을 모두 섭취하기 위해 걸리는 총 시간은,
첫 번째 음식의 소요 시간 * 남은 음식의 개수이며, 4 * 3 = 12 가 됩니다.
따라서, 시간이 가장 적게 걸리는 음식부터 순서대로 탐색하며,
[이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]과 K의 시간을 비교하며 제거를 진행하게 됩니다.
세부 구현 방식은 예제 코드에 설명 되어있습니다.
'''

import heapq

food_times = [ 8, 6, 4 ]
k = 15

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    sum_times = 0 # 지금까지 먹은 시간의 총합
    previous = 0 # 직전에 먹은 음식의 섭취 시간
    length = len(food_times) # 음식의 종류

    queue = []

    for i in range(len(food_times)):
        heapq.heappush(queue,(food_times[i], i+1)) # 음식갯수(시간), 음식 번호(index)
    
    while sum_times + (queue[0][0] - previous) * length < k:
        now = heapq.heappop(queue)[0]
        sum_times += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(queue, key=lambda x:x[1]) # 음식 번호로 정렬
    return result[(k - sum_times)%length][1]

print(solution(food_times, k))
