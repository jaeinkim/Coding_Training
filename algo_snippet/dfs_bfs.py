graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
#############
# 1. DFS    #
#############
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    print(discovered)
    return discovered

print(f'recursive_dfs result = {recursive_dfs(1)}')


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

#############
# 2. BFS    #
#############
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
        print(f'queue = {queue}')
        print(f'discovered = {discovered}')
    return discovered

print(f'iterative_bfs result = {iterative_bfs(1)}')



