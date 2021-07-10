n = input()
maximum = 8   # 나이트가 갈 수 있는 모든 위치

if not ('c' <= n[0] <= 'f'): 
  maximum -= 2
if n[0] == 'a' or n[0] == 'h':
  maximum -= 1
if not (3 <= int(n[1]) <= 6):
  maximum -= 2
if int(n[1]) == 1 or int(n[1]) == 8:
  maximum -= 1

print (maximum)
