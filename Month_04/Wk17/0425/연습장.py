m, n, k =  map(int, input().split()) #가로 세로 위치
arr = [[0]* (n) for _ in range(m)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1
print(arr)
