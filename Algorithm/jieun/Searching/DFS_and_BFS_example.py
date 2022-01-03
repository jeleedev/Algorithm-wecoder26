from collections import deque

''' Depth First Search (DFS) 알고리즘 '''
def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end = ' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

''' Breadth First Search (BFS) 알고리즘 '''
def bfs(graph, start, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])  ##################?? 왜 [start] 리스트형식으로 넣어줘야하는지
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

        
''' DFS, BFS 호출하는 구간 '''
n, m, start = map(int, input().split())

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

for e in graph:
    e.sort()

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * len(graph)
dfs(graph, start, visited) # 정의된 DFS 함수 호출

print()

visited = [False] * len(graph)
bfs(graph, start, visited) # 정의된 BFS 함수 호출

'''
[Input Example 1]
8 18 1
1 2
1 3
1 8
2 1
2 7
3 1
3 4
3 5
4 3
4 5
5 3
5 4
6 7
7 2
7 6
7 8
8 1
8 7
[Output Example 1]
'''



