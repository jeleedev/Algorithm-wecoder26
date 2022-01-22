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
# DFS
def dfs(graph, start_node):
    visited = list() 
    need_visit = list() 
    # start_node를 맨 처음 방문 대기열에 추가
    need_visit.append(start_node)
    # 방문 대기열이 존재하지 않을 때 까지 반복   
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
# DFS TEST
print(dfs(graph, 'A')) # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']