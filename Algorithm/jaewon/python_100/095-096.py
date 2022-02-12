# 문제95 : 도장찍기
# 풀이1
def solution(stamp, k):
  n = len(stamp)
  l = [[0] * n for i in range(n)]
  # print(l)
  sum_matrix(l, stamp)
  for i in range(k):
    stamp = rotate(stamp)
    l = sum_matrix(l, stamp)
  return l

def rotate(stamp):
  n = len(stamp)
  rot = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(n):
      rot[j][n-i-1] = stamp[i][j]
  return rot

def sum_matrix(l, stamp):
  n = len(stamp)
  for i in range(n):
    for j in range(n):
      l[i][j] += stamp[i][j]
  return l


stamp = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]
k = 1
print(solution(stamp, k))
"""
[
  [1, 2, 3, 3],
  [2, 1, 0, 1],
  [1, 2, 1, 2],
  [0, 1, 0, 2]
]
"""

# 풀이2
import numpy
def solution(stamp, k):
  m = numpy.array(stamp)
  numpy.rot90(m, k)
  pass


n = 4
l = numpy.zeros(n*n).reshape(n,n).astype(int)
# print(l)
stamp = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]
k = 1
print(solution(stamp, k))


# 문제96 : 넓은 텃밭 만들기!
def solution(data):
  width = len(data[0])
  height = len(data)
  res = [[0] * width for i in range(len(data))]
  for i in range(0, height):
    for j in range(0, width):
      if data[i][j] == 0:
        res[i][j] = 1
      else:
        res[i][j] = 0
    
  for i in range(1, height):
    for j in range(1, width):
      if res[i][j] == 1:
        res[i][j] = min(res[i-1][j-1], min(res[i-1][j], res[i][j-1])) + 1

  maxValue = 0
  x = 0
  y = 0
  for i in range(0, height):
    for j in range(0, width):
      if maxValue < res[i][j]:
        maxValue = res[i][j]
        x = i
        y = j
                
  # print(maxValue, x, y)
  # print(maxValue, 'X', maxValue)
    
  for i in range(x - (maxValue - 1), x + 1):
    for j in range(y - (maxValue - 1), y + 1):
      data[i][j] = '#'

  return data

data = [
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
]   
print(solution(data))