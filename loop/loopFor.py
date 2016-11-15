# 03-3 for문

# for문의 기본 구조

'''

for 변수 in 리스트(또는 튜플, 문자열)
    수행할 문장1
    수행할 문장2
'''

# 1.전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 2.다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
