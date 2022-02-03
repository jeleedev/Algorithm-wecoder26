# 문제51 : merge sort를 만들어보자
import random
data = random.sample(range(50), 10)
def merge_sort(l):
  if len(l) <= 1: return l
  mid = len(l) // 2
  left = merge_sort(l[:mid])
  right = merge_sort(l[mid:])
  res = []
  while left and right:
    if left[0] < right[0]:
      res.append(left.pop(0))
    else:
      res.append(right.pop(0))
  while left:
    res.append(left.pop(0))
  while right:
    res.append(right.pop(0))
  return res
print(f"{data} => {merge_sort(data)}")


# 문제52 : quick sort
def quick_sort(l):
  if len(l) <= 1: return l
  pivot = l[0]
  left = [i for i in l[1:] if i < pivot]
  right = [i for i in l[1:] if i >= pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)
print(f"{data} => {quick_sort(data)}")


# 문제53 : 괄호 문자열
def func(data):
  if data.count('(') != data.count(')'):
    return 'NO'
  res = []
  for i in data:
    if i == '(':
      res.append(i)
    elif i == ')':
      if len(res) == 0:
        return 'NO'
      res.pop()
  return 'YES'
# user_input = input()
user_input = '(())()(()))'
print(func(user_input))



# 문제54 : 연속되는 수
def func(l):
  l = sorted(l)
  for i in range(len(l)-1):
    if l[i] + 1 != l[i+1]:
      return 'No'
  return 'Yes'
# num_list = list(map(int, input().split()))
num_list = [1, 2, 3, 4, 5]
print(func(num_list))

# 문제55 : 하노이의 탑
res = []
def func(n, start, end, mid):
    if n == 1:
        res.append([start, end])
        return None
    func(n-1, start, mid, end)
    res.append([start, end])
    func(n-1, end, mid, start)
# n = int(input())
n = 3
func(n, 'A', 'C', 'B')
print(res, len(res))

# 문제56 : 리스트의 함수 응용
nationWidth = {
  'korea': 220877,
  'Rusia': 17098242,
  'China': 9596961,
  'France': 543965,
  'Japan': 377915,
  'England' : 242900
}
korea_area = nationWidth['korea']
del nationWidth['korea']
max_gap = max(nationWidth.values())
res = ""
for i in nationWidth.items():
  if max_gap > abs(i[1] - korea_area):
    max_gap = i[1] - korea_area
    res = i[0]
print(res, max_gap)


# 문제57 : 내장함수 응용하기
def func(n):
  num_data = str(list(range(n+1)))
  return num_data.count('1')
# n = int(input())
n = 20
print(func(n))


# 문제58 : 콤마 찍기
# 풀이1
def comma(n):
    return format(n, ",")
# n = int(input())
n = 123456789
print(comma(n))

# 풀이2
def comma(n):
  if len(n) <= 3:
    return n
  return comma(n[:len(n)-3]) + ',' + n[len(n)-3:]
# n = input()
n = '123456789'
print(comma(n))


# 문제59 : 빈칸채우기
s = 'hi'
print('{0:=^50}'.format(s))
print(format(s, '=^50'))
print('=' * ((50-len(s))//2) + s + ('=' * (50-((50-len(s))//2)-len(s))))


# 문제60 : enumerate
student = [
  '강은지',
  '김유정',
  '박현서',
  '최성훈',
  '홍유진',
  '박지호',
  '권윤일',
  '김채리',
  '한지호',
  '김진이',
  '김민호',
  '강채연'
]
student = sorted(student)
for i,v in enumerate(student, 1):
  print(f"번호: {i}, 이름: {v}")