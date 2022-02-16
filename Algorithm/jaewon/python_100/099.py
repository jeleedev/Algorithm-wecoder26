# 문제99 : 토끼들의 행진
def solution(capability, rabbit_jumps):
  res = ["pass" for i in range(len(rabbit_jumps))]
  # print(res)
  for i in range(len(rabbit_jumps)):
    p = 0
    while p < len(capability):
      p += rabbit_jumps[i]
      # print(f'{i}번째 토끼 위치는 {p}')
      # print(f"뛰기 전 돌의 내구도 {capability}")
      capability[p-1] -= 1
      # print(f"뛴 후 돌의 내구도 {capability}")
      if capability[p-1] < 0:
        res[i] = "fail"
    # print('==============================')
  return res
capability = [1, 2, 1, 4]
rabbit_jumps = [2, 1]
print(solution(capability, rabbit_jumps))