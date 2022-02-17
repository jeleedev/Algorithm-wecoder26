# 문제100 : 퍼즐게임
def solution(puzzle, control):
  stack = [0]
  res = 0
  while control:
    move = control.pop(0)
    for i in range(len(puzzle)):
      if puzzle[i][move-1] != 0:
        if stack[-1] == puzzle[i][move-1]:
          res += puzzle[i][move-1] * 2
          stack.pop()
        else:
          stack.append(puzzle[i][move-1])
        puzzle[i][move-1] = 0
        break
      if i == len(puzzle)-1 and puzzle[i][move-1] == 0:
        res -= 1
  return res
  

puzzle = [
  [0,0,0,0],
  [0,1,0,3],
  [2,5,0,1],
  [2,4,4,1],
  [5,1,1,1],
]
control = [1,1,1,1,3,3,3]
print(solution(puzzle, control))