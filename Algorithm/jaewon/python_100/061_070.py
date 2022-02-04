# 문제61 : 문자열 압축하기
# data = input()
data = 'aaabbbbcdddd'
data += ' '
res = []
for i in range(len(data)-1):
  if data[i] != data[i+1]:
    res.append(data[i])
    res.append(str(data.count(data[i])))
print("".join(res))


# 문제62 : 20190923출력하기
string='aacddddddddd'
a=string.count('a')
b=string.count('b')
c=string.count('c')
d=string.count('d')
print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(d)+str(a)+str(a+1)))


# 문제63 : 친해지고 싶어
# data = input()
data = '복잡한 세상 편하게 살자'
l = [i[0] for i in data.split()]
print("".join(l))


# 문제64 : 이상한 엘레베이터
def elevetor(n):
  res = 0
  while True:
    if n % 7 == 0:
      res += n // 7
      return res
    n -= 3
    res += 1
    if n < 0:
      return -1
# n = int(input())
n = 24
print(elevetor(n))


# 문제65 : 변형된 리스트
# 풀이1
a = [1,2,3,4]
b = ['a','b','c','d']
res = []
for i in range(len(a)):
  if i % 2 == 0:
    res.append([a[i], b[i]])
  else:
    res.append([b[i], a[i]])
print(res)

# 풀이2
a = [1,2,3,4]
b = ['a','b','c','d']
res = []
count = 0
for i,j in zip(a,b):
  if count % 2 == 0:
    res.append([i,j])
  else:
    res.append([j,i])
  count += 1
print(res)


# 문제66 : 블럭탑쌓기
def solution(blocks, rule):
  res = []
  for block in blocks:
    res.append(block_check(block, rule))
  return res

def block_check(block, rule):
  temp = rule.index(rule[0])
  for i in block:
    if i in rule:
      if temp > rule.index(i):
        return '불가능'
      temp = rule.index(i)
  return '가능'
  
blocks = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
rule = 'ABCD'
print(solution(blocks, rule))


# 문제67 : 민규의 악수
def solution(n):
  people = 0
  total = 0
  while True:
    total = people * (people - 1) / 2
    if n < total:
      break
    people += 1
  times = int(people - (total - n) - 1)
  return [times, people]
print(solution(59))

# 문제68 : 버스 시간표
def solution(times, now):
  res = []
  now = int(now[0:2])*60 + int(now[3:])
  
  for time in times:
    time = int(time[0:2])*60 + int(time[3:])
    if now >= time:
      res.append("지나갔습니다.")
    else:
      rest = time - now
      if rest >= 60:
        hour = rest // 60
        min = rest % 60
        res.append(f"{hour}시간 {min}분")
      else:
        res.append(f"0시간 {rest}분")
  return res

times = ["12:30", "13:20", "14:13"]
now = "12:40" 
print(solution(times, now))


# 문제69 : 골드바흐의 추측
import math
# n = int(input())
def prime_list(n):
  l = [True] * n
  m = int(math.sqrt(n))
  for i in range(2, m+1):
    if l[i] == True:
      for j in range(i+i, n, i):
        l[j] = False
  return [i for i in range(2, n) if l[i]==True]
# n = int(input())
n = 100
prime_bucket = prime_list(n) 
# print(prime_bucket)

res = []
for i in range(n // 2 + 1):
  if i in prime_bucket and n-i in prime_bucket:
    res.extend([[i, n-i]])
print(res)


# 문제70 : 행렬 곱하기
def sol(a, b):
  c = []
  if len(a) == len(b[0]):
    for i in range(len(a)):
      c.append([0]*len(b[0]))
    for i in range(len(c)):
      for j in range(len(c[i])):
        for k in range(len(a[i])):
          c[i][j] += a[i][k] * b[k][j]
    return c
  else:
    return -1

a = ([1, 2],
     [2, 4])
b = ([1, 0],
     [0, 3])

print(sol(a,b))