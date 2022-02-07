# 요일 구하기(datetime 모듈 사용)

# 2020년 1월 1일은 수요일입니다. 2020년 a월 b일은 무슨 요일일까요?
# 두 수 a, b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.

# 예를 들어 a = 5, b = 24라면 5월 24일은 일요일이므로 문자열 "SUN"를 반환하세요.

# 제한 조건

# 2020년은 윤년입니다.
# 2020년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일 같은 날짜는 주어지지 않습니다.)
# datetime 모듈을 사용하세요.

# 답안
import datetime

def week(a, b):
  day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
  return day[datetime.date(2020, a, b).weekday()]

print(week(2,15))

# datetime 모듈 내 date 클래스
# : 연, 월, 일 데이터를 인자로 받아 날짜를 표현하는 클래스로 시간에 대한 정보를 담지 않는다.
datetime.date(2022, 2, 7) # 2022-02-07

# 오늘 날짜를 얻고 싶은 경우 date클래스의 today() 메서드 사용
datetime.date.today()

# YYYY-MM-DD 형태의 문자열로 변환하고 싶은 경우 isoformat() 메서드 사용
# YYYY-MM-DD 형태의 문자열을 date객체로 변환하고 싶은 경우 fromisoformat() 사용
datetime.date.today.isoformat()
datetime.date.today.fromisoformat()

# 해당 날짜의 요일을 파악하고 싶은 경우 weekday(), isoweekday() 메서드 사용
datetime.date.today.weekday() # 월요일이 0으로 시작 {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}
datetime.date.today.isoweekday() # 월요일이 1로 시작

