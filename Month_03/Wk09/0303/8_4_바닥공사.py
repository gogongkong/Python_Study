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


'''
문제 해석
796796으로 나누라는것은 단순히 결과값이 커지니까 그런것
개미 전사문제(224p)와 동일하게 i-1, i-2까지만 생각한다.
왜냐하면 i-3부터는 이미 사용할 수 있는 덮개의 형태가 2x2밖에 없기 때문
i-1 까지 이미 덮어져 있다 생각한다면 가능한 경우의 수는 2x1타일 한개(1)
i-2 까지 덮어져 있다고 생각한다면 가능한 경우의 수는 2x2 한개 혹은 1x2두개를 넣는 경우가 존재(2)
이를 토대로 점화식을 유추해보면
a(i) = a(i-1) + (a(i-2) * 2) 이다.

'''

n = int(input())

d = [0] * 10001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796
print(d[n])

