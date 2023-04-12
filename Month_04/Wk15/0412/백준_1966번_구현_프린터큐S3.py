'''
https://www.acmicpc.net/problem/1966
문제
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 
즉 먼저 요청된 것을 먼저 인쇄한다. 
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 
이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 
다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

예제 입력 1 
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

예제 출력 1 
1
2
5
'''
from collections import deque

tc = int(input())

result = [] # 결과값을 저장할 변수
for _ in range(tc): # TC 갯수만큼 반복
    n, m = map(int, input().split()) # 문서 갯수 N, 타겟문서의 중요도 M 입력
    queue = deque(list(map(int, input().split()))) # 문서의 중요도 입력
    count = 0 #타겟 문서까지의 순서를 체크하기 위한 count 변수 선언
    while queue: # queue가 빌 때까지
        best = max(queue) # 가장 중요도가 높은 문서
        front = queue.popleft() # 가장 앞에 있는 문서 pop
        m -= 1 # 맨 앞의 문서 하나가 빠졌기 때문에 타겟문서의 순서도 하나 빠짐

        if front == best: # 맨 앞의 문서가 중요도가 가장 높은 문서일 때
            count += 1
            if m < 0: # 해당 문서가 타겟 문서인경우
                result.append(count)
                break
        
        else: # 맨 앞의 문서가 Best가 아닌경우
            queue.append(front) # 맨 앞 문서를 맨 뒤로 이동
            if m < 0: # 그 문서가 타겟 문서인경우 타겟문서의 순서 재정렬
                m = len(queue) - 1

for i in result:
    print(i)























# from collections import deque

# tc = int(input()) # TC 갯수
# result = []
# for i in range(tc):
#     n, m = map(int,input().split())
#     queue = deque(list(map(int, input().split())))
#     count = 0
#     while queue:
#         best = max(queue) # 큐에서 가장 큰수(우선순위가 가장 높음)를 지정
#         front = queue.popleft() # 가장 앞에 있는 문서를 pop
#         m -= 1 # target문서의 번호 -1

#         if best == front: # 최고 우선순위 문서가 가장 앞에 있다면
#             count +=1 # 인쇄하면 되므로 count + 1
#             # m이 0보다 작다는 소리는 가장 앞의 문서가 target문서이자 최고 우선순위이며 가장 앞에 있다는 의미
#             if m < 0: 
#                 result.append(count) # 더이상 확인할 사항이 없으니 count 종료
#                 break
#         else: # 가장 앞의 문서가 최고 우선순위 문서가 아니라면
#             queue.append(front) # 가장 앞의 문서를 다시 가장 뒤로 보냄
#             if m < 0: # target문서가 최고 우선순위가 아니면서 가장 앞에 있었다면
#                 m = len(queue) -1 # target의 순서를 맨 뒤로 옮김

# for i in result:
#     print(i)

