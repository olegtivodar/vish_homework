'''
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

3 <--- input()
1 4 5
6 7 8
1 1 6

8 <--- output()
'''

n = int(input('Введите количество строк и столбцов: '))
matrix = []

print()

# Заполняем матрицу значениями, которые вводит пользователь
for i in range(n):
    matrix.append(list(map(int, input().split())))

print()

# Печатаем заполненную матрицу
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

print()

r_zone = [] # Пустой список, который будет заполняться числами из правой области матрицы
for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j:
            r_zone.append(matrix[i][j])

l_zone = [] # Пустой список, который будет заполняться числами из левой области матрицы
for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j:
            l_zone.append(matrix[i][j])

# Нахождения максимального числа левой и правой области
r_max_element = max(r_zone)
l_max_element = max(l_zone)

# Вывод максимального числа из правой и левой области
if r_max_element > l_max_element:
    print(r_max_element)
else:
    print(l_max_element)