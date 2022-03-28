#숫자
print(1)
print(1.1)
#연산
print(1+1)
print(2-1)
print(2*2)
print(6/2)
#제곱
print(pow(3,2))
#랜덤
import random
print(random.random())

#String
print('Hello')
print("Hello")
# 여러줄
print('''
    Hello
    World
''')
# 문자열 길이
print(len('Hello'))
print('Hell world'.replace('Hell','Hello'))

#List
member = ['tom', 'jack', 'jimmy']
print(member[0])
# 배열 길이
print(len(member))

# 랜덤값 뽑기
import random
print(random.choice(member))

score = [100,200,300]
# List에 있는 값들 더하기
print(sum(score))