# Даны две матрицы A и B. Написать программу, которая будет менять местами максимальные элементы этих матриц.
'''
Пример работы программы:

3 6 7
2 4 8
-----  <--- input()
1 2 9
3 6 4


3 6 7
2 4 9
-----  <--- output()
1 2 8
3 6 4
'''

from random import randint

def maxArray(array): # фунцкия нахождения максимального элемента матрицы
    max_element = array[0][0]
    for i in range(len(array)):
        if max(array[i]) > max_element:
            max_element = max(array[i])
    return max_element

def printArray(A, B): # фунцкия, которая печатает матрицы
    for i in A:
        print(*i)
    print('*'*15)
    for i in B:
        print(*i)
    print()

linesA = int(input('Введите количество строк матрицы A: '))
amountA = int(input('Введите количество элементов матрицы A: '))
linesB = int(input('Введите количество строк матрицы B: '))
amountB = int(input('Введите количество элементов матрицы B: '))

A = [[randint(1, 50) for i in range(amountA)] for j in range(linesA)]
B = [[randint(51, 100) for i in range(amountB)] for j in range(linesB)]

printArray(A, B)

max_element_A = maxArray(A)
max_element_B = maxArray(B)

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = max_element_B if A[i][j] == max_element_A else A[i][j] # использование тернарного оператора
for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = max_element_A if B[i][j] == max_element_B else B[i][j] # использование тернарного оператора

printArray(A, B)




