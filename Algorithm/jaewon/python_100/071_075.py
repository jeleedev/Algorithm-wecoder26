# 문제71 : 깊이 우선 탐색
graph = dict()
graph['E'] = ['D', 'A']
graph['D'] = ['E', 'F']
graph['A'] = ['E', 'C', 'B']
graph['F'] = ['D']
graph['C'] = ['A']
graph['B'] = ['A']
# print(graph)
def dfs(graph, start_node):
  visited = list()
  need_visited = list()
  need_visited.append(start_node)
  while need_visited:
    node = need_visited.pop()
    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
  return visited
print(dfs(graph, 'E'))

# 문제72 : 너비 우선 탐색
graph = dict()
graph['E'] = ['D', 'A']
graph['D'] = ['E', 'F']
graph['A'] = ['E', 'C', 'B']
graph['F'] = ['D']
graph['C'] = ['A']
graph['B'] = ['A']
# print(graph
def bfs(graph, start_node):
  visited = list()
  need_visited = list()
  need_visited.append(start_node)
  while need_visited:
    node = need_visited.pop(0)
    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
  return visited
print(bfs(graph, 'E'))

# 문제73 : 최단 경로 찾기
graph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A', 'F']),
  'D': set(['B']),
  'E': set(['B', 'F']),
  'F': set(['C', 'E'])
}

# start, end = [i for i in input().split()] # A F
start, end = 'A', 'F'
queue = [start]
visited = [start]
def solution():
  count = -1
  while len(queue) != 0:
    count += 1
    size = len(queue)
    for i in range(size):
      node = queue.pop(0)
      if node == end:
        return count
      for next_node in graph[node]:
        if next_node not in visited:
          queue.append(next_node)
          visited.append(next_node)
print(solution()) # 2

# 문제74 : 최장 경로 찾기
graph = {1: [2, 3, 4],
				 2: [1, 3, 4, 5, 6],
				 3: [1, 2, 7],
				 4: [1, 2, 5, 6],
				 5: [2, 4, 6, 7],
				 6: [2, 4, 5, 7],
				 7: [3, 5, 6]} 

# start, end = [int(i) for i in input().split()]
start, end = 1, 7
queue = [start]
visited = []
def sol(n, visited):
	if n[-1] == end:
		return len(visited)
	if n[-1] in visited:
		return len(visited)
	visited.append(n[-1])
	length = 0
	for next_node in graph[n[-1]]:
		n.append(next_node)
		length = max(length, sol(n, visited))
		queue.pop(-1)
	return length
print(sol(queue, visited))


# 문제75 : 이상한 369
def func(n):
  l = list(str(n))
  answer = 0
  count = 1
  d = {3:1, 6:2, 9:3}
  while l:
    answer += d[int(l.pop())] * count
    count *= 3
  return answer
print(func("93"))
"""
3 = 1
6 = 2
9 = 3
33 = 4(3*1+1)
36 = 5(3*1+2)
39 = 6(3*1+3)
63 = 7(3*2+1)
66 = 8(3*2+2)
69 = 9(3*2+3)
93 = 10(3*3+1)
96 = 11(3*3+2)
99 = 12(3*3+3)
"""