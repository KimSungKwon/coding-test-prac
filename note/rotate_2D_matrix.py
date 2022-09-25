'''
Rotate 2D matrix 90' 시계방향
'''

def rotate_2D_matrix(arr):
    n = len(matrix) # column length
    m = len(arr[0]) # row length
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
      for j in range(m):
        result[j][n - i - 1] = arr[i][j]
    
    return answer
