'''
https://www.acmicpc.net/problem/20115
'''

'''
1. 임의의 두개의 음료를 선택 A, B
2. A를 B에다가 모두 부음(B를 A도 가능) 붓는과정중 절반 손실 --> B + A/2
3. A는 버림
4. 1~3을 반복 
'''

n = int(input())

drinks = list(map(float, input().split()))

drinks.sort(reverse=True)
result = drinks[0]
for i in range(1, n):
    result = max(result, drinks[i]) + (min(result, drinks[i])/2)

print(result)