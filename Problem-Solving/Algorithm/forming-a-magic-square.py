
def reflect_col(m):
    matrix = [m[0][:], m[1][:], m[2][:]]
    
    for i in range(3):
        matrix[i][0] = matrix[i][0] + matrix[i][2]
        matrix[i][2] = matrix[i][0] - matrix[i][2]
        matrix[i][0] = matrix[i][0] - matrix[i][2]
    
    return matrix

def reflect_row(m):
    matrix = [m[0][:], m[1][:], m[2][:]]
    
    for i in range(3):
        matrix[0][i] = matrix[0][i] + matrix[2][i]
        matrix[2][i] = matrix[0][i] - matrix[2][i]
        matrix[0][i] = matrix[0][i] - matrix[2][i]
    return matrix

if __name__ == '__main__':
    
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    
    row1 = [8, 1, 6]
    row2 = [3, 5, 7]
    row3 = [4, 9, 2]
    matrix = [None] * 8

    matrix[0] = [row1, row2, row3]
    matrix[1] = reflect_row(matrix[0])
    matrix[2] = reflect_col(matrix[1])
    matrix[3] = reflect_col(matrix[0])
    matrix[4] = [value for value in zip(*matrix[0])]
    matrix[5] = [value for value in zip(*matrix[1])]
    matrix[6] = [value for value in zip(*matrix[2])]
    matrix[7] = [value for value in zip(*matrix[3])]

    cost = []
    for i in range(8):
        diff = 0
        for j in range(3):
            for k in range(3):
                diff += abs(matrix[i][j][k] - s[j][k])
        cost.append(diff)
    print(min(cost))