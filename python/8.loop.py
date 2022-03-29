# 1차원 배열 (배열 안에 문자열)
members = ['egoing','duru']
for member in members:
    print('member', member)

# 2차원 배열 (배열 안에 배열, 그 배열 안에 문자열)
members2 = [
    ['egoing', 'seoul', 'programmer'],
    ['duru', 'daegu', 'dba']
]
print(members2[0][0])
for member in members2:
    print(member)

#딕셔너리
egoing1 = ['egoing', 'seoul', 'programmer']
egoing2 = {'name':'egoing', 'city':'seoul', 'job':'programmer'}
print(egoing2)
print(egoing2['name'])
#딕셔너리 for문 사용
for name in egoing2:
    print(name)
    print(egoing2[name])

# member의 바람직한 코드
members3 = [
    {'name':'egoing', 'city':'seoul', 'job':'programmer'},
    {'name':'duru', 'city':'deagu', 'job':'dba'}
]
for member in members3:
    print(member['name'])
    