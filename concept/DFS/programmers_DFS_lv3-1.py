# 네트워크_lv3

# 오답
def solution(n, computers):
    answer = 0
    cnt = []
    for i in range(len(computers)):
        list1 = []
        for j in computers:
            list1.append(j[i])
        if 0 not in list1:
            cnt.append(1)
        else:
            cnt.append((list1.count(0)+(list1.count(1)-1)))

    return min(cnt)


# 2차 풀이(DFS 사용)
def solution(n, computers):
    visited = [False] * n
    answer = 0

    for node in range(n):
        if visited[node] == False:
            dfs(n, computers, node, visited)
            answer += 1

    return answer

def dfs(n, computers, node, visited):
    visited[node] = True

    for i in range (n):
        if visited[i] == False and computers[node][i] == 1:
            visited = dfs(n, computers, i, visited)
    return visited

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) #1