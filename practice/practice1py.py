# 최저임금을 이용한 간단한 임금계산기
print('<임금 계산기>')
최저임금 = 9160
한달근무시간 = int(input('주휴시간을 포함한  한달근무시간은? '))
월급 = 최저임금 * 한달근무시간
print(f'한달 임금은 {월급}원입니다.')
