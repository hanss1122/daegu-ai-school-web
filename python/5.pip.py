import pandas
house = pandas.read_csv('boston.csv')
print(house)
# 상단 데이터만 보기
print(house.head())
# 첫번째 데이터만 보기
print(house.describe())