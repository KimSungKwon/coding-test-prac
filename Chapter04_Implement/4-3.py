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

# 또 다른 풀이
# 방향 벡터 dx, dy 이용
def solution(S):
    x = (ord(S[0]) - ord('a') + 1)
    y = int(S[1])
    count = 0
    #(y, x)
    directX = [-1, 1, 2, 2, 1, -1, -2, -2]
    directY = [-2, -2, -1, 1, 2, 2, 1, -1]
     
    for i in range(len(directX)):
        dx = x + directX[i]
        dy = y + directY[i]
        if dx < 1 or dx > 8 or dy < 1 or dy > 8:
            continue
        count += 1
        
    return count

print(solution( 'a1'  ))  # print 2
