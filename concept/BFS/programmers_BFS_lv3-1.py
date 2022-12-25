# 네트워크_lv3
def solution(n, computers):
    visited = [False] * n
    answer = 0

    for node in range(n):
        if visited[node] == False:
            bfs(n, computers, node, visited)
            answer += 1
    return answer

def bfs(n, computers, node, visited):
    visited[node] = True
    queue = []
    queue.append(node)

    while queue:
        node = queue.pop(0)
        visited[node] = True
        for i in range(n):
            if i != node and computers[node][i] == 1:
                if visited[i] == False:
                    queue.append(i)