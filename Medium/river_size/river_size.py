def river_size_calculate(matrix, height, width, n, m):
    size = 0
    if n < height and n >= 0 and m < width and m >= 0:
        if matrix[n][m] == 1:
            matrix[n][m] = 0
            size += river_size_calculate(matrix, height, width, n, m+1)
            size += river_size_calculate(matrix, height, width, n, m-1)
            size += river_size_calculate(matrix, height, width, n+1, m)
            size += river_size_calculate(matrix, height, width, n-1, m)
            size += 1
            return size
        else:
            return 0
    return size

def river_size(matrix):
    height = len(matrix)
    width = len(matrix[0])
    size = 0
    rivers = []
    
    for i in range(height):
        for j in range(width):
            size = river_size_calculate(matrix,height, width, i, j)
            rivers.append(size) if size > 0 else ''
    return rivers
