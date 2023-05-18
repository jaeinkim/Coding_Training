import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
graph = {}
discovered = []
max_lst = {}

for _ in range(len(lst)-1):
    k, v = map(int, input().split())
    graph[k] = graph.get(k, []) + [v]

def recursive_dfs(v, level):
    for w in graph.get(v, []):
        recursive_dfs(w, level+1)
    lst[v-1] += max_lst.get(level+1, 0)
    max_lst[level+1] = 0
    if max_lst.get(level, 0) < lst[v-1]:
        max_lst[level] = lst[v-1]

recursive_dfs(1, 0)
print(f'{lst[0]}')

