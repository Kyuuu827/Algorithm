# 1번
# def solution(n):
#     answer = 0
#     nums = []

#     for num in str(n):
#         nums.append(num)
    
#     nums = list(set(nums))

#     for i in nums:
#         if int(i) == 0:
#             continue
#         if n % int(i) == 0:
#             answer += 1

#     return answer

# print(solution(1234)) # 2

#2번
# INC = 0
# DEC = 1

# def func_b(s):
#     global INC, DEC

#     length = len(s)
#     ret = [0 for _ in range(length)]
#     ret[0] = -1

#     for i in range(1, length):
#         if s[i] > s[i-1]:
#             ret[i] = INC
#         elif s[i] < s[i-1]:
#             ret[s] = DEC
#     return ret    

# def func_a(arr):
#     length = len(arr)
#     ret = [0 for _ in range(length)]
#     ret[0] = 1

#     for i in range(1, length):
#         if arr[i] != arr[i-1]:
#             ret[i] = ret[i-1] + 1
#         else:
#             ret[i] = 2
#     return ret

# def func_c(arr):
#     ret = max(arr)

#     if ret == 2:
#         return 0
#     return ret

# def solution(S):
#     check = func_b(S)
#     dp = func_a(check)
#     answer = func_c(dp)
#     return answer

# print(solution([1,2,3]))

#2번
# def solution(s):
#     cnt = 0
#     for i in range(1, len(s)):
#         if i % 2 == 0: #짝수
#             if s[i-1] < s[i]:
#                 cnt += 1
#         else: # 홀수
#             if s[i-1] > s[i]:
#                 cnt += 1

#     if (len(s)+cnt) % 2 == 0:
#         if s[-1] < s[-2]:
#             cnt += 1
#     else:
#         if s[-1] > s[-2]:
#             cnt +=1
    
#     return cnt

# print(solution([1,2,3]))

#3번
import heapq as hq

def solution(board, c):
    cost = 0
    loc = []
    
    # (0,4) -> (5, 4)
    for i, row in enumerate (board):
        for j, col in enumerate (row):
            if col == 2:
                sp = [i, j] # (0, 4)
            if col == 3:
                ep = [i, j] # (5, 4)
    loc = sp


    # while loc != ep:
    #     if board[loc[0]+1][loc[1]] == 1:
    #         cost += 1+c
    #         loc = [loc[0]+1, loc[1]] #(1,4)
    #         print(loc)
    #     elif board[sp[0]+1][sp[1]] == 0:
    #         cost += 1
    #         loc = [sp[0]+1, sp[1]]
    #     elif loc == ep:
    #         break

    # while loc != ep:
    #     if loc[0] + 1:
    #         if board[loc[0]+1][loc[1]] == 1:
    #             cost += 1+c
    #         else:
    #             cost += 1
    #         loc = [loc[0]+1, loc[1]]
    # return cost

    

    # return cost

#print(solution([ [0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]], 1))

#단비교육
#1번
# def solution(n, v):
#     max_profit = []
#     answer = []
#     for i, sp in enumerate(v):
#         profit = []
#         for pp in range(i+1, len(v)):
#             pp = v[pp]
#             profit.append(sp-pp)
#         answer.append(max(profit, default=float("-inf")))

#     return max(answer)

# print(solution(10, [4, 1, 7, 6, 5, 2]))

#2번
result = []
def solution(N, relation, dirname):
    answer = 0
    visited = [False] * N

    for node in range (N):
        if visited[node] == False:
            dfs(N, relation, dirname, node, visited)
            answer = result
    return sum(answer)

def dfs(N, relation, dirname, node, visited):
    visited[node] = True
    global result

    for i in range (N):
        if visited[i] == False:
            result.append(1+len(dirname[i]))
    
    return result

print(solution(7, [[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]], ["root","abcd","cs","hello","etc","hello","solution"]))
#3번


#4번
# import itertools

# from collections import deque as dq


# def solution(play_list, listen_time):
#     if sum(play_list) <= listen_time:
#         return len(play_list)

#     queue = dq()

#     for i in play_list:
#         for j in range(i):
#             queue.append(i)

#     result = []
#     num = 0
#     while num < len(queue):
#         for _ in range(listen_time):
#             queue.append(queue.popleft())
#         result.append(len(set(list(itertools.islice(queue, 0, listen_time)))))
#         queue.rotate(-1)
#         num += 1

#     return max(result)

# print(solution([1,2,3,4], 5))
    

