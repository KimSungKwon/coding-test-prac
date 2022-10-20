"""
Q41 여행계획

여행 계획이 가능하다 == 여행지가 다 같은 그룹에 속해있다. 
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
graph = []
trip = []
answer = True

for i in range(1, n + 1):
    parent[i] = i

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, (i + 1), (j + 1))

trip = list(map(int, input().split()))

for i in trip[1:]:
    if find_parent(parent, trip[0]) != find_parent(parent, i):
        answer = False

if answer:
    print("YES")
else:
    print("NO")
