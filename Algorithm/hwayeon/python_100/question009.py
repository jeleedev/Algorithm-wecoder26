# sep과 end를 활용한 출력방법

# 다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, )
print(hour, minute, second, )

# 출력
# 2019/04/26 11:34:27

# 답안
print(year, month, day, sep='/', end='')
print(hour, minute, second, sep=':')

# sep
# : 구분자라는 뜻의 separator에서 왔으며 값 사이에 공백이 아닌 문자를 넣고 싶을 때 사용한다.

# end
# : python의 print는 기본적으로 출력하는 값 끝에 \n을 붙이기 때문에 print를 여러번 사용하면 값이 여러줄에 걸쳐 출력된다.
#   그렇기 떄문에 여러 번 사용하더라도 한 줄에 여러 개의 값을 출력하고 싶을 때 end를 사용한다.