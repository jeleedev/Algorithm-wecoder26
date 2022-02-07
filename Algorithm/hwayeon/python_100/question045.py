# time함수 사용하기

# python의 모듈 중 하나인 time 모듈은 1970년 1월 1일 0시 0분 0초 이후로부터 지금까지 흐른 시간을 초단위로 반환합니다

# 이를 이용하여 현재 연도(2022)를 출력해보세요

# 답안
import time

n = time.gmtime()
print(n.tm_year)

# 답안
import time
t = time.time()
t = int(t//(3600*24*365))+1970
print(t)

# gmtime() : 주어진 timestamp 값을 GMT 기준의 time_struct 타입의 데이터로 변환
import time

tm = time.gmtime(1575142526.500323)
print(tm) # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=30, tm_hour=19, tm_min=35, tm_sec=26, tm_wday=5, tm_yday=334, tm_isdst=0)

# 이름	         값	         비고
# tm_year	    연	        예: 1993, 2019
# tm_mon	    달	        범위: 1~12
# tm_mday	    일	        범위: 1~31
# tm_hour	    시	        범위: 0~23
# tm_min	    분	        범위: 0~59
# tm_sec	    초	        범위: 0~61
# tm_wday	    요일	     범위: 0~6 (0: 월요일)
# tm_yday	    연중         경과일	범위: 1~366
# tm_isdst	일광절약타임       적용여부	0: 미적용 1: 적용 -1: 모름

# localtime() : timestamp를 현지 시간대 기준의 time_struct 타입의 데이터로 변환
import time

tm = time.localtime(1575142526.500323)
print("year:", tm.tm_year)  # year: 2019
print("month:", tm.tm_mon)  # month: 11
print("day:", tm.tm_mday)   # day: 30
print("hour:", tm.tm_hour)  # hour: 14
print("minute:", tm.tm_min) # minute: 35
print("second:", tm.tm_sec) # second: 26