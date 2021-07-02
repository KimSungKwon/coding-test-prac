n = int(input())
route = input().split()

# 시작 좌표 (1, 1)
posX = 1
posY = 1

# L, R, U, D 에 해당하는 좌표 이동
for i in range(len(route)):
  if (route[i] == 'L'):
    if (posX == 1):
      continue
    else:
      posX -= 1
  if (route[i] == 'R'):
    if (posX == n):
      continue
    else:
      posX += 1
  if (route[i] == 'U'):
    if (posY == 1):
      continue
    else:
      posY -= 1
  if (route[i] == 'D'):
    if (posY == n):
      continue
    else:
      posY += 1

print(f"{posY} {posX}")
