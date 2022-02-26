'''
union_find 알고리즘
'''

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 사용자로부터 n, m 입력받음
n, m = map(int, input().split())

# 부모 테이블 초기화
parents = [0] * (n+1)
for i in range(n+1):
    parents[i] = i

# 사용자로부터 union연산 또는 find연산 입력받음
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union_parent(parents, a, b)
    else:
        if find_parent(parents, a) == find_parent(parents, b):
            print("YES")
        else:
            print("NO")
