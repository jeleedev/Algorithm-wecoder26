# 문제9 : sep과 end를 활용한 출력방법

# 다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.
# 출력 >> 2019/04/26 11:34:27

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# sep : 구분자에 넣을 내용을 임의로 기입하는 옵션
# end : 현재 속한 출력물을 그 다음 출력값과 이어지게 한다.