'''
문제
문제가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.

태일이는 이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 덮개를 이용해 채우고자 한다.

이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1,000)
출력
첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최솟값을 출력한다.
첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.

[입력 예시]
3	

[출력 예시]
5
'''
n = int(input())

d = [0] * 10001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] +2*d[i-2]) % 796796

print(d[n])