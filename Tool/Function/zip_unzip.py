'''
zip()
zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 
각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다
'''
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

# (1, 'A')
# (2, 'B')
# (3, 'C')

# 3개도 가능
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e


'''
unzip()
zip() 함수로 엮어 놓은 데이터를 다시 해체(unzip)하고 싶을 때도 zip() 함수를 사용할 수 있습니다.
'''

numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)
# [(1, 'A'), (2, 'B'), (3, 'C')]

numbers, letters = zip(*pairs)
numbers
(1, 2, 3)
letters
('A', 'B', 'C')