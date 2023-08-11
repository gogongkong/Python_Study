# 자연수인지 확인하는 방법

data = "Aa234A"

for i in range(len(data)):
    isint = int(data[i]) == data[i]
    if isint:
        print("1")