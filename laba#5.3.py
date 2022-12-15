'''
Напишите программу, которая меняет местами столбцы в матрице.

3 4 <--- input()
11 12 13 14
21 22 23 24
31 32 33 34
0 1

11  12  13  14  <--- output()
21  22  23  24  
31  32  33  34  

12  11  13  14  
22  21  23  24  
32  31  33  34 
'''

n, m = map(int, input("Введите количество строк и столбцов через пробел: ").split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

j1, j2 = map(int, input("Введите столбцы, которые следует поменять местами через пробел: ").split())

print()

# Печатаем первоначальную матрицу
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

print()

# Меняем столбцы местами
for i in range(n):
    matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]

# Печатаем измененную матрицу
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()