# python은 변수 앞에 자료형을 지정하지 않아도 된다
a = 1

가격 = 10000
부가세율 = 0.1
결과 = 가격 * 부가세율
print(결과)

#print에서의 변수 사용
name = 'Tom'
print('안녕하세요, '+name+'님, ... 안녕히계세요, '+name+'님')

#중괄호를 이용하면 따옴표(')와 더하기(+) 없이 편하게 쓸 수 있다 (f-string)
print(f'안녕하세요, {name}님, ... 안녕히계세요, {name}님')