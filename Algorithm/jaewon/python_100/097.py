# 문제97 : 택배배달
def solution(workers, times):
  res = 0
  work_distance = [0] * workers
  while times:
    for i in range(workers):
      if work_distance[i] == 0 and times:
        work_distance[i] = times.pop(0)
    work_distance = list(map(lambda x: x-1, work_distance))
    res += 1
  #   print('======================')
  #   print(work_distance, res)
  # print('==========end while============')
  # print(work_distance, res)  
  res += max(work_distance)
  return res
workers = 3
times = [1,2,1,3,3,3]

print(solution(workers, times))  