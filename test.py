# import sys
# input = sys.stdin.readline
#
# num = int(input())
#
# def gcd(n, m):
#     k = n%m
#     if k == 0:
#         return m
#     return gcd(m, k)
#
# for i in range(num):
#     n, m = map(int, input().split())
#     print(n*m/gcd(n,m))
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
# def recursive_dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = recursive_dfs(w, discovered)
#     print(discovered)
#     return discovered
#
# print(f'recursive_dfs result = {recursive_dfs(1)}')


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
        print(discovered)
    return discovered

print(f'iterative_dfs result = {iterative_dfs(1)}')






# 상향식 접근법 (타뷸레이션)
def fib(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i -2]
    return dp[n]


# 하향식 접근법 (메모이제이션)
def fib(n):
    if n <= 1:
        return n

    if dp[n]:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]