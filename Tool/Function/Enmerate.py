'''
enumerate
인덱스 변수를 사용하지 않고 루프를 돌리는 방식
출처 : https://www.daleseo.com/python-enumerate/
'''

# for 루프를 이용한 리스트 글자 출력 코드
print("for문 이용 \n")
for letter in ["A","B","C"]:
    print(letter)

# for를 이용하면서 인덱스도 함께 출력
print("for문 이용 및 인덱스 사용 \n")
letter = ["A","B","C"]
for i in range(len(letter)):
    print(letter[i], i)


# index와 원소를 동시에 접근하면서 루프를 돌리는 방법
# --> enumerate

print("enumerate 이용 \n")
for entry in enumerate(["A","B","C"]):
    print(entry)
print("\n\n")

# enumerate는 기본적으로 인덱스와 원소로 이루어진 튜플구조를 만듦
# 다른 변수로 할당하고 싶다면 unpacking하면 됨
for i, letter in enumerate(["A","B","C"]):
    print(i,letter)

print("\n\n")
# 시작 인덱스도 변경할 수 있다.
for i, letter in enumerate(["A","B","C"], start=1):
    print(i,letter)



# 고급 응용
print("#### 고급 응용 ####\n\n")

#2차원 리스트를 이용해보자
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

# for문을 이용한다면 아래와 같이 사용
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(i,j,matrix[i][j])

# eumerate 이용
print("\n\n")
for i, row in enumerate(matrix):
    #print(row)
    for j, letter in enumerate(row):
        print(i,j,letter)
