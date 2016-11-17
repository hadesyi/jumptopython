# 04-1 함수
'''
파이썬 함수의 구조
def 한수명(입력 인수):
    <수행할 문장1>
    <수행할 문장2>
    ...
'''


def sum(a, b):
    return a + b


a = 3
b = 4
c = sum(a, b)
print(c)

# 입력값과 결과값에 따른 함수의 형태

# 일반적인 함수
'''
def 함수이름(입력인수):
    <수행할 문장>
    ...
    return 결과값
'''


def sum(a, b):
    result = a + b
    return result


a = sum(3, 4)
print(a)