가격 = input('가격? ')
# can't multiply sequence by non-int of type 'float' 에러남

# 가격 = float(input('가격? '))
# 입력받은 값을 float로 바꿔줘야 한다
부가세율 = 0.1
결과 = 가격 * 부가세율
print(결과)