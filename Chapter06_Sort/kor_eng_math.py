"""
Q23 국영수

튜플의 정렬 + 람다
"""

n = int(input())
data = []

for i in range(n):
    data.append(list(input().split()))

data.sort(key = lambda x: (int(-x[1]), int(x[2]), int(-x[3]), x[0]))
