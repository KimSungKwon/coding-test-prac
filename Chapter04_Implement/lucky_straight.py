'''
Q 07 럭키스트레이트 
'''
n = list(input())

length = len(n)
mid = int(length / 2)

left = 0
right = 0
for i in range(mid):
    left += int(n[i])

for i in range(mid, length):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
