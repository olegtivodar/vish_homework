'''
Написать программу, которая создает матрицу размером n * m и заполняет ее "спиралью"

4 5 <--- input()

1   2   3   4   5  <--- output() 
14  15  16  17  6   
13  20  19  18  7   
12  11  10  9   8 
'''

n, m = map(int, input('Введите количество строк и столбцов через пробел: ').split())
matrix = []
count = 1 
x = 0
y = -1 
moves_row = 0 # Движение по рядам {-1}(Движение вверх) {0}(Находимся в том же ряду) {1}(Движение вниз)
moves_column = 1 # Движение по столбцам {-1}(Движение влево) {0}(Находимся в том же столбце) {1}(Движение вправо)

print()

# Заполнение матрицы нулями
for r in range(n):
    row = []
    for c in range(m):
        row.append(0)
    matrix.append(row)

'''
# Печатаем матрицу, заполненную нулями
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

print()
'''

# Цикл, который заполняет матрицу по спирали
while count <= n * m:
    # Условие при котором мы можем шагать, в случае если мы не вышли за пределы массива и ячейка не занята
    if (0 <= x + moves_row < n and 0 <= y + moves_column < m) and (matrix[x + moves_row][y + moves_column] == 0):
        x += moves_row
        y += moves_column
        matrix[x][y] = count
        count += 1
    else:
        if moves_column == 1: # Должны начать идти вниз
            moves_column = 0
            moves_row = 1
        elif moves_row == 1: # Должны начать идти влево
            moves_row = 0
            moves_column = -1
        elif moves_column == -1: # Должны начать идти вверх
            moves_column = 0
            moves_row = -1
        elif moves_row == -1: # Должны начать идти вправо
            moves_row = 0
            moves_column = 1

# Печатаем матрицу, заполненную по спирали
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()