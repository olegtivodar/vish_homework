'''
Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, которая выводит след заданной квадратной матрицы.

3 <--- input()
1 2 3
4 5 6
7 8 9

15 <--- output()
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

main_diagonal = [] # Пустой список, который будет заполняться числами главной диагонали
for i in range(n):
    main_diagonal.append(matrix[i][i])

md_sum_elements = sum(main_diagonal)

print(md_sum_elements)