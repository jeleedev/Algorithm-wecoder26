# 문제31 : 파이썬 자료형의 복잡도
"""
다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?
1)  l[i] => O
2)  l.append(5) => O
3)  l[a:b] => X
4)  l.pop() => O
5)  l.clear() => O
"""

# 문제32 : 문자열 만들기
def func(data):
  return len(data.split(" "))
# data = input()
data = "안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다."
print(func(data))


# 문제33 : 거꾸로 출력하기
# l = list(map(int, input().split()))
l = ['2', '4', '6', '7', '8']
for i in range(len(l)-1, -1, -1):
  print(l[i], end=' ')
print()

# 문제34 : sort 구현하기
# l = list(map(int, input().split()))
l = ['176', '156', '155', '165', '166', '169']
sorted_l = sorted(l)
if l == sorted_l:
  print('YES')
else:
  print('NO')


# 문제35 : Factory 함수 사용하기
def one(n):
  def two(value):
    return value ** n      
  return two
a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))


# 문제36 : 구구단 출력하기
# num = int(input())
num = 2
for i in range(1,10):
  print(num * i, end=" ")
print()

# 문제37 : count 사용하기
# l = input().split() 
l = ['원범', '원범', '혜원', '혜원', '혜원', '혜원', '유진', '유진']
res = max(l)
print(f'{res}(이)가 총 {l.count(res)}표로 반장이 되었습니다.')


# 문제38 : 호준이의 아르바이트
# 풀이1
# score = list(map(int, input().split()))
score = ['97', '86', '75', '66', '55', '97', '85', '97', '97', '95']
score = sorted(score, reverse=True)
print(score)
rank = 0
res = 0
for i in range(len(score)-1):
  if score[i] != score[i+1]:
    res += score.count(score[i])
    rank += 1
  if rank >= 3: break
print(res)

# 풀이2
score = ['97', '86', '75', '66', '55', '97', '85', '97', '97', '95']
res = 0
for i in range(3):
  top = max(score)
  res += score.count(top)
  for _ in range(score.count(top)):
    score.remove(top)
print(res)


# 문제39 : 오타 수정하기
# user_input = input()
user_input = 'hqllo my namq is hyqwon'
print(user_input.replace('q', 'e'))


# 문제40 : 놀이동산에 가자
limit_weight = int(input())
n = int(input())
l = [int(input()) for _ in range(n)]
i = 0
total_weight = 0
while True:
  total_weight += l[i]
  if total_weight > limit_weight: break
  i += 1
print(i)