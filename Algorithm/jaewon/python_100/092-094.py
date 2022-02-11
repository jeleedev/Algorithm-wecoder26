# 문제92 : 키보드 고장
import csv
f = open('test.txt', 'r', encoding='utf-8')
r = csv.reader(f)
for line in r:
  s1, s2 = '', ''
  for i in line[1].replace(',',''):
    # print(i)
    if i == '3':
      s1 += '1'
      s2 += '2'
    elif i== '4':
      s1 += '2'
      s2 += '2'
    elif i== '6':
      s1 += '1'
      s2 += '5'
    else:
      s1 += i
      s2 += '0'
  print(line[2], int(s1), int(s2))
# 3 -> 1,2
# 4 -> 2,2
# 6 -> 1,5


# 문제93 : 페이지 교체 - 선입선출 알고리즘
"""
['B', 'C', 'B', 'A', 'E', 'B', 'C', 'E']
페이지 = [B] 1번 째 B(6초)
페이지 = [B, C] 2번 째 C(6초)
페이지 = [B, C] 3번 째 B(1초) - HIT!
페이지 = [B, C, A] 4번 째 A(6초)
페이지 = [C, A, E] 5번 째 E(6초)
페이지 = [A, E, B] 6번 째 B(6초)
페이지 = [E, B, C] 7번 째 C(6초)
페이지 = [E, B, C] 8번 째 E(1초) - HIT!
"""  
def sol(frame, page):
  runTime = 0
  temp = []

  if frame == 0:
    runTime = len(page) * 6
    return runTime
  for i in page:
    if i in temp:
      runTime += 1
    else:
      if len(temp) < frame:
        temp.append(i)
      else:
        temp = temp[1:] + [i]
      runTime += 6
      
  return runTime, temp
frame = 3
page = ['B', 'C', 'B', 'A', 'E', 'B', 'C', 'E']
print(sol(frame, page))


# 문제94 : 페이지 교체 - LRU 알고리즘
"""
['B', 'C', 'B', 'A', 'E', 'B', 'C', 'E']
페이지 = [B] 1번 째 B(6초)
페이지 = [B, C] 2번 째 C(6초)
페이지 = [C, B] 3번 째 B(1초) - HIT!
페이지 = [C, B, A] 4번 째 A(6초)
페이지 = [B, A, E] 5번 째 E(6초)
페이지 = [A, E, B] 6번 째 B(1초) - HIT!
페이지 = [E, B, C] 7번 째 C(6초)
페이지 = [B, C, E] 8번 째 E(1초) - HIT!
"""
def sol(frame, page):
  runTime = 0
  temp = []

  if frame == 0:
    runTime = len(page) * 6
    return runTime
  for i in page:
    if i in temp:
      temp.append(temp.pop(0))
      runTime += 1
    else:
      if len(temp) < frame:
        temp.append(i)
      else:
        temp = temp[1:] + [i]
      runTime += 6
      
  return runTime, temp
frame = 3
page = ['B', 'C', 'B', 'A', 'E', 'B', 'C', 'E']
print(sol(frame, page))