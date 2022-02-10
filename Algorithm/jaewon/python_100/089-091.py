# 문제89 : 지식이의 게임개발2
def makeMap(width, height, boss, blocks):
  map = [[0]*(width+2) for i in range(height+2)]
  for i in range(len(map)):
    for j in range(len(map[0])):
      if i == 0 or i == len(map)-1 or j == 0 or j == len(map[0])-1:
        map[i][j] = 2
  map[boss[0]+1][boss[1]+1] = 1
  for block in blocks:
    if map[block[0]+1][block[1]+1] != "1":
      map[block[0]+1][block[1]+1] = 2
    else:
      map[block[0]+1][block[1]+1] = 1
  return map

def move(map, m):
  x,y = 0,0
  for i,j in enumerate(map):
    if 1 in j:
      x,y = j.index(1), i
  map[y][x] = 0
  for i in m:
    # print(i)
    if i == 1 and map[y-1][x] != 2: # 상
      y -= 1
    if i == 2 and map[y+1][x] != 2: # 하
      y += 1
    if i == 3 and map[y][x-1] != 2: # 좌
      x -= 1
    if i == 4 and map[y][x+1] != 2: # 우
      x += 1
  print(x,y)
  map[y][x] = 1
  return map

width = 4
height = 5
boss = [0,0]
blocks = [[0,1], [1,1], [2,3], [1,3]]

res = makeMap(width, height, boss, blocks)
m = [2,2,2,4,4,4] # 1:상, 2:하, 3:좌, 4:우
move_res = move(res, m)
for i in move_res:
  print(i)


# 문제90 : 같은 의약성분을 찾아라!
import random
l = [chr(i) for i in range(65,91)] # A-Z
total_medicine = [] # 중복이 없는, 약품 데이터 100개
res = []
for i in range(100):
  total_medicine.append(random.sample(l, 8))

# user_input = input().split()
user_input = ['ABCDEFGH', '4']

for i in total_medicine:
  if len(set(i) & set(user_input[0])) == int(user_input[1]):
    res.append(i)
print(len(res))


# 문제91 : 반평균 등수
import random
import numpy

total_score = []
for i in range(7):
  class_score = []
  for j in range(30):
    student_score = []
    for k in range(5):
      student_score.append(random.randint(1,100))
    class_score.append(student_score)
  total_score.append(class_score)
# print(total_score)
# print(len(total_score)) # 7
a = numpy.array(total_score)
b = numpy.sum(a, axis=2)
c = b/5
d = numpy.sum(c, axis=1)
print(d/30) # 반평균
# print(a)
# print(a.shape) # (7, 30, 5)
# print(a.size) # 1050