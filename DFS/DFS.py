# 리스트를 활용한 DFS 구현
def dfs(graph, start_node):
    # 아직 방문하지 않은 노드의 리스트와 이미 방문한 노드의 리스트 2개를 생성하는 것이 기본이다.
    need_visit, visited = list(), list()    
    need_visit.append(start_node)
    
    while need_visit:
        # 스택 구조를 활용       
        node = need_visit.pop()
        
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited


# 재귀함수를 이용한 DFS 구현
def recursive_dfs(graph, start, visited = []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            recursive_dfs(graph, node, visited)

    return visited