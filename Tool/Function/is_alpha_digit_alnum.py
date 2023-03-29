
'''
isalpha()
문자열의 구성이 알파벳 or 한글인지 확인하는 방법 [isalpha]
isalpha()라는 내장함수 사용, 단 문자열에 공백,기호 and 숫자가 있을시 False를 리턴한다.
'''

# Example for isalpha
ex_01 = 'A'
ex_02 = 'S520'
ex_03 = "코드앵글러"
ex_04 = "Code_Angler"
ex_05 = "Code Angler"
# print result of isalpha()
print(ex_01.isalpha())
print(ex_02.isalpha()) # 숫자가 포함되여 False
print(ex_03.isalpha())
print(ex_04.isalpha()) # 기호가 포함되어 False
print(ex_05.isalpha()) # 공백이 포함되어 False

'''
isdigit()
숫자인지 확인하는 방법 [isdigit]
'''
# Example for isdigit
ex_01 = '123'
ex_02 = '010-1234-5678'
ex_03 = "전화번호010"
ex_04 = "Phone 010"
# print result of isdigit()
print(ex_01.isdigit())
print(ex_02.isdigit()) # 기호가 포함되여 False
print(ex_03.isdigit()) # 문자가 포함되어 False
print(ex_04.isdigit()) # 공백이 포함되어 False

'''
isalnum()
알파벳(한글) 또는 숫자인지 확인하는법[isalnum]
isalnum()라는 내장함수를 사용하여 확인한다.
'''
# Example for isalnum
ex_01 = '123'
ex_02 = '010-1234-5678'
ex_03 = "전화번호010"
ex_04 = "Phone 010"
# print result of isalnum()
print(ex_01.isalnum())
print(ex_02.isalnum()) # 기호가 포함되여 False
print(ex_03.isalnum()) 
print(ex_04.isalnum()) # 공백이 포함되어 False

