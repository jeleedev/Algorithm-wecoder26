# 문제41 : 소수판별
def is_prime(n):
  prime = True
  for i in range(2, n):
    if n % i == 0:
      prime = False
      break
  if prime == True:
    return 'YES'
  else: return 'NO'
# num = int(input())  
num = 7  
print(is_prime(num))


# 문제42 : 2022년(datetime 모듈 사용)
import datetime
def func(m, d):
  day_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
  return day_list[datetime.date(2022, m, d).weekday()]
# m, d = map(int, input().split())
m, d = (1, 28)
print(func(m, d))


# 문제43 : 10진수를 2진수로
# 풀이1
def func(num):
  res = ''
  while num:
    res += str(num % 2)
    num = num // 2
  return res[::-1]
# num = int(input())
num = 13
print(func(num))

# 풀이2
def func(num):
  res = []
  while num:
    res.append(str(num % 2))
    num = num // 2
  res.reverse()
  return int("".join(res))
num = 13  
print(func(num))


# 문제44 : 각 자리수의 합
def func(n):
    data = str(n)
    res = [int(i) for i in data]
    return sum(res)
# user_input = int(input())
user_input = 12345
print(func(user_input))


# 문제45 : time함수 사용하기
import time
now = time.time()
# print(now)
print(int(now//(3600*24*365)+1970))


# 문제46 : str 자료형의 응용
# 풀이1
def func(num1, num2):
  s = 0
  for i in range(num1, num2+1):
    for j in str(i):
      s += int(j)
  return s
# start_num = int(input())
# last_num = int(input())
num1 = 10
num2 = 15
print(func(num1, num2))

# 풀이2
def func(num1, num2):
  res = [int(j) for i in range(num1, num2+1) for j in str(i)]
  return sum(res)
# start_num = int(input())
# last_num = int(input())
num1 = 10
num2 = 15
print(func(num1, num2))


# 문제47 : set 자료형의 응용
people = [
         ('이호준', '01050442903'),
         ('이호상', '01051442904'),
         ('이준호', '01050342904'),
         ('이호준', '01050442903'),
         ('이준', '01050412904'),
         ('이호', '01050443904'),
         ('이호준', '01050442903'),
         ]
print(len(set(people)))


# 문제48 : 대소문자 바꿔서 출력하기
def func(data):
  res = []
  for i in data:
    if i.isupper():
      res.append(i.lower())
    else:
      res.append(i.upper())
  return "".join(res)

data = 'AAABBBcccddd'
print(func(data))


# 문제49 : 최댓값 구하기
def func(data):
  return max(data)
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(func(data))


# 문제50 : 버블정렬 구현하기
import random
def bubble_sort(l):
  for i in range(len(l)-1):
    swap = False
    for j in range(len(l)-1-i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]
        swap = True
    if swap == False: break
  return l

data = random.sample(range(50), 10)
print(bubble_sort(data))