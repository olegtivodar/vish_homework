'''
Напишите программу, которая создает матрицу размером m * n, заполнив ее змейкой

3 5 <--- input()

1   2   3   4   5 <--- output()  
10  9   8   7   6   
11  12  13  14  15 
'''

n, m = map(int, input("Введите количество строк и столбцов через пробел: ").split())
matrix = []
count = 1

print()

# Создаем матрицу, заполненную нулями
for r in range(n):
    row = []
    for c in range(m):
        row.append(0)
    matrix.append(row)

'''
# Печатаем матрицу с нулями
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

print()
'''

# Меняем изначальную матрицу, изменяя каждый элемент на +1    
for i in range(n):
    for j in range(m):
        matrix[i][j] += count
        count += 1

# Печатаем итоговую матрицу, переворачивая строчки матрицы через одну 
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()
    else:
        matrix[i].reverse()
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()