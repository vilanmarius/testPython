#Maze runner game

class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    def get_matrix(self, n, m):
        num = 1
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)
#matrix test to display

mazeMatrix=[
    [1, 0, 1,0],
    [1, 0, 1,0],
    [1, 0, 1,0],
    [1, 0, 1,0]
]
m1 = Matrix(2, 3)
print(m1)
