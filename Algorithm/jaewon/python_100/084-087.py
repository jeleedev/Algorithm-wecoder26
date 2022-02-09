# 문제84 : 숫자뽑기
# 풀이1
from itertools import combinations
n = 1723
k = 2
l = [i for i in str(n)] # ['1', '7', '2', '3']
num_list = list(map(''.join, combinations(l,k)))
print(max(num_list))

# 풀이2
from itertools import permutations
n = 1723
k = 2
l = [i for i in str(n)] # ['1', '7', '2', '3']
num_list = list(map(''.join, permutations(l,k)))
print(max(num_list))


# 문제85 : 숫자 놀이
def rule(n):
  num_l = max(int(i) for i in n)
  count_num = [str(i)+str(str(n).count(str(i))) for i in range(1, num_l+1)]
  return "".join(count_num)
def sol(count):
  answer = "1"
  if count == 1:
    return answer
  for i in range(1, count):
    answer = rule(answer)
    # print(answer)
  return answer
# num = int(input())
num = 6
print(sol(num))


# 문제87 : 천하 제일 먹기 대회
def sol(name, point):
  res = {}
  l = [[i,j] for i,j in zip(name, point)] # [['손오공', 70], ['야모챠', 10], ['메지터', 55], ['비콜로', 40]]
  sorted_l = sorted(l, key=lambda x: x[1], reverse=True)
  for i in range(len(sorted_l)):
    res[sorted_l[i][0]] = i+1
  return res
name = "손오공 야모챠 메지터 비콜로"
point = "70 10 55 40"
name = name.split() # ['손오공', '야모챠', '메지터', '비콜로']
point = list(map(int, point.split())) # [70, 10, 55, 40]
print(sol(name, point))


# 문제88 : 지식이의 게임개발
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

width = 4
height = 5
boss = [0,0]
blocks = [[0,1], [1,1], [2,3], [1,3]]

res = makeMap(width, height, boss, blocks)
for i in res:
  print(i)