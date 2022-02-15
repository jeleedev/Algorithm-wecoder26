# 문제98 : 청길이의 패션 대회
import re

def solution(s):
  res = []
  l = re.split('[0-9]번: ', s)[1:]
  for i in range(len(l)):
    l[i] = list(map(int, l[i].replace(" ", "").split(',')))
  # print(l) # [[3, 1], [4], [2, 1, 3], [2, 1, 3, 4]]
  for i in l:
    for j in i:
      if j in res:
        pass
      else:
        res.append(j)
      
  return res
s = "1번: 3,1 2번: 4 3번: 2,1,3 4번: 2,1,3,4"
print(solution(s))