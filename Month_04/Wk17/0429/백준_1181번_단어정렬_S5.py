'''
https://www.acmicpc.net/problem/1181
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.

예제 입력 1 
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
예제 출력 1 
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''































n = int(input()) # 단어의 갯수를 입력받을 변수

data = [] # 단어를 입력받을 리스트

for _ in range(n): # 단어 갯수 만큼 반복
    data.append(input()) # 단어 입력

data = list(set(data)) # 입력받은 단어를 리스트형식으로 set()

sorting = [] # data를 (단어길이, 단어) 형식으로 입력받을 리스트
for i in data:
    sorting.append((len(i), i))

sorting.sort() # 정렬

for word in sorting: # 출력
    print(word[1])