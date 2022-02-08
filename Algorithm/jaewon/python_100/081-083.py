# 문제81 : 지뢰찾기
# 풀이1
value = """0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0"""
value = value.replace('1', 'f')
# print(value)
l = [i.strip() for i in value.split('\n')]
# ['0 f 0 0 0', '0 0 0 0 0', '0 0 0 f 0', '0 0 f 0 0', '0 0 0 0 0']
# print(l) 
l = [i.split() for i in l]
# print(l) 
# [
#   ['0', 'f', '0', '0', '0'],
#   ['0', '0', '0', '0', '0'],
#   ['0', '0', '0', 'f', '0'],
#   ['0', '0', 'f', '0', '0'],
#   ['0', '0', '0', '0', '0']
# ]

count = 0
for i in l:
  for j in i:
    # print(i, 'j >>',j)
    if j == 'f':
      if i.index(j) > 0:
        i[i.index(j)-1] = "*"
      if i.index(j) < len(i)-1:
        i[i.index(j)+1] = "*"
      if count > 0:
        l[count-1][i.index(j)] = "*"
      if count < len(i) - 1:
        l[count+1][i.index(j)] = "*"
  count += 1
print(l)

# 풀이2
value = """0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0"""
value = value.replace('1', 'f')
l = value.split()
# print(l)
"""
[
  '0', 'f', '0', '0', '0',
  '0', '0', '0', '0', '0',
  '0', '0', '0', 'f', '0',
  '0', '0', 'f', '0', '0',
  '0', '0', '0', '0', '0'
]
"""
for i in range(len(l)):
  if l[i] == 'f':
    # print(i) # 1, 13, 17
    if i % 5 != 0:
      l[i-1] = '*'
    if i % 5 != 4:
      l[i+1] = '*'
    if i // 5 != 0:
      l[i-5] = '*'
    if i // 5 != 4:
      l[i+5] = '*'
print(l)


# 문제82 : 수학 괄호 파싱
def sol(s):
  count = 0
  for i in s:
    if i == '(':
      count += 1
    elif i == ')':
      count -= 1
  if count == 0:
    return True
  else: return False
    
while True:
  order = int(input("데이터 입력 (1), 프로그램 종료(2) :"))
  if order == 1:
    user_input = input("데이터를 입력하세요. ")
    print(sol(user_input))
  else: break


# 문제83 : 수학 괄호 파싱 2
def sol(s):
  d = {')':'(', '}':'{'}
  stack = []
  for i in s:
    if i in '({':
      stack.append(i)
    elif i in d:
      if len(stack) == 0:
        return False
      else:
        if d[i] != stack.pop():
          return False
  return len(stack) == 0
  
while True:
  order = int(input("데이터 입력 (1), 프로그램 종료(2) :"))
  if order == 1:
    user_input = input("데이터를 입력하세요. ")
    print(sol(user_input))
  else: break