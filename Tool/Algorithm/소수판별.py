# 소수 판별 함수
# 소수 : 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

# 비효율
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True # 소수임

# 동작확인
print(is_prime_number(4))
print(is_prime_number(7))

# 제곱근을 이용한 방법
# 확인을 위한 수의 가운데 약수 (ex : 16의 경우 4)까지만 나누어 떨어지는지 확인
# 다시말해 제곱근까지만 확인하면 가능
# 가운데가 없는경우 (ex : 8 --> 2.828.... 이므로 2까지만 확인)

import math

# 소수 판별함수
def is_prime_number(x):
    # 2부터 x의 제곱근 가지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))


