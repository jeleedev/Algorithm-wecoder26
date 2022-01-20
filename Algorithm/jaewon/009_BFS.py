# BFS 구현
## graph 표현
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
## BFS
def bfs(graph, start_node): # 그래프와 시작 Node를 넣음
    visited = list() 
    need_visit = list()
    # start_node를 맨 처음 방문 대기열에 추가
    need_visit.append(start_node)
    # 방문 대기열이 존재하지 않을 때 까지 반복
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited: 
            visited.append(node)
            need_visit.extend(graph[node])
    return visited 
# BFS TEST
print(bfs(graph, 'A')) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']