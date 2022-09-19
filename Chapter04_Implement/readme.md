# 구현

## 구현에 쓰이는 기술들
### **좌표 이동**
	시계 방향 이동 (U, R, D, L)
	
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    nx = x + dx[i],  ny = y + dy[i]

### **방향 회전**
	
    turn_left(): 
	    global direction
	    direction -= 1
	    if direction == -1: 
		    direction = 3
	       ...
	nx = x + dx[direction] ...
