# 문제76 : 안전한 땅
import numpy as np

square_len = 5
detect_len = 3

mine_array = [
  [1, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0]
]

mine_array = np.array(mine_array)
# print(mine_array)
# slice_area = mine_array[i:detect_len+i, j:detect_len+j]
# print(mine_array[0:3, 0:3])
# print(mine_array[0:3, 1:4])
# print(mine_array[0:3, 2:5])
# print(mine_array[1:4, 0:3])
# print(mine_array[1:4, 1:4])
# print(mine_array[1:4, 2:5])
# print(mine_array[2:5, 0:3])
# print(mine_array[2:5, 1:4])
# print(mine_array[2:5, 2:5])

res = 0
for i in range(square_len - detect_len + 1): # 3(5-3+1)
    for j in range(detect_len): # 3
        slice_area = mine_array[i:detect_len+i, j:detect_len+j]
        if np.sum(slice_area) > res: 
            res = np.sum(slice_area)
print(res) # 3


# 문제77 : 가장 긴 공통 부분 문자열
def sol(s):
  result = []
  for i in range(1, len(s)+1):
    for j in range(i):
      result.append(s[j:j+len(s)-i+1])
  return result

# user_input = input().split()
user_input = ["ABCDEF", "BCDE"]
user_input_set_one = set(sol(user_input[0]))
user_input_set_two = set(sol(user_input[1]))
# print(user_input_set_one)
# print(user_input_set_two)
res = user_input_set_one.intersection(user_input_set_two)
# print(res)
res = max(res, key=len)
print(len(res))


# 문제78 : 원형테이블
def sol(n,k):
  l = [i for i in range(1, n+1)]
  while len(l) > 2:
    l.pop(0)
    for _ in range(k-1):
      l.append(l.pop(0))
  return l

# n, k = list(map(int, input().split()))
n, k = 6, 3
print(sol(n,k))


# 문제79 : 순회하는 리스트
def sol(l, turn):
  l_copy = l.copy()
  result = []
  for i in range(turn):
    l_copy.insert(0, l_copy.pop())
  for i,j in zip(l, l_copy):
    result.append(abs(i-j))
  index = result.index(min(result))
  return l[index], l_copy[index]
  
l = [10, 20, 25, 27, 34, 35, 39]
# turn = int(input())
turn = 2
print(sol(l, turn))


# 문제80 : 순열과 조합
from itertools import combinations

user_input = ["ㄱ","ㄴ","ㄷ","ㄹ"]
user_num = 3
print(list(combinations(user_input, user_num)))
"""
[('ㄱ', 'ㄴ', 'ㄷ'), ('ㄱ', 'ㄴ', 'ㄹ'), ('ㄱ', 'ㄷ', 'ㄹ'), ('ㄴ', 'ㄷ', 'ㄹ')]
"""
print(list(map(''.join, combinations(user_input, user_num))))
"""
['ㄱㄴㄷ', 'ㄱㄴㄹ', 'ㄱㄷㄹ', 'ㄴㄷㄹ']
"""