'''
Q42 탑승구

아이디어의 문제..
'''

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


g = int(input())
p = int(input())
parent = [0] * (g + 1)

for i in range(len(parent)):
    parent[i] = i

result = 0
for i in range(p):
    n = int(input())    
    prnt = find_parent(parent, n)
    
    if prnt != 0:
        union(parent, prnt, prnt - 1)
        result += 1
    if prnt == 0:
        break
        
print(result)
