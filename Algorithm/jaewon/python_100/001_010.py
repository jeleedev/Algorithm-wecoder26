# 문제1 : 리스트의 삭제
nums = [100, 200, 300, 400, 500]
del nums[-1]
del nums[-1]
print(nums) # [100, 200, 300]

# 문제2 : 리스트의 내장함수
l = [200, 100, 300]
l.insert(2, 10000)
print(l) # [200, 100, 10000, 300]

# 문제3 : 변수의 타입
l = [100, 200, 300]
print(type(l)) # <class 'list'>

# 문제4 : 변수의 타입2
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은?
# 3)  입력 : a = 'p',   출력 : class 'char'

# 문제5 : for문 계산
a = 10
b = 2
for i in range(1, 5, 2):
    a += i
print(a+b) # 16

# 문제6 : False
# 1)  None => False
# 2)  1 => True
# 3)  "" => False
# 4)  0 => False
# 5)  bool(0) => False

# 문제7 : 변수명
# 다음 중 변수명으로 사용할 수 없는 것 2개를 고르시오.
# 1)  age
# 2)  a
# 3)  as => as는 예약어이므로 사용할 수 없다.
# 4)  _age 
# 5)  1age => 변수명은 숫자로 시작할 수 없다.

# 문제8 : 딕셔너리 키 이름 중복
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight']) # 84

# 문제9 : sep과 end를활용한 출력방법
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':') # 2019/04/26 11:34:27

# 문제10 : 별 찍기
n = 5
for i in range(1, n+1):
    print(" " *(n-i)+"*"*(2*i-1))
"""
    *
   ***
  *****
 *******
*********
"""