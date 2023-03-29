'''
문자열 재정렬

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한값을 이어서 출력합니다.
예를들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

[입력 조건]
    - 첫째 줄에 하나의 문자열 S가 주어집니다.

[출력 조건]
    - 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

[입력 예시1]
K1KA5CB7

[출력 예시1]
ABCKK13

[입력 예시1]
AJKDLSI412K4JSJ9D

[출력 예시1]
ADDIJJJKKLSS20

'''



# 좋은풀이
# isalpha 라는 알파벳인지 숫자인지 확인하는 함수가 있음
data = input()
result = []
num = 0

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i)

result.sort()

if num != 0:
    result.append(str(num))

print(''.join(result))


# 내풀이
import heapq
s = list(input())
# ord(0) = 48, ord(9) = 57 ord(A) =65

data = 0 # 숫자를 더해서 저장할 변수
q= [] # 문자열을 우선순위 큐에 저장
for i in range(len(s)):
    if 48<= ord(s[i]) <= 57:
        data += int(s[i])
    elif 65<= ord(s[i]):
        heapq.heappush(q,(ord(s[i])))

while q:
    Alphabet = heapq.heappop(q)
    print(chr(Alphabet), end= '')
    if not q:
        print(data)
