# Дан одномерный массив
# Получить другой массив, состоящий только из четных чисел исходого массива, а также меньше числа меньшие 10
# Или сообщить, что таких чисел нет
# Массив вводит пользователь
# Пример:
'''
n = 7
8
4
2
6
29
39
145
Ответ: [2, 4, 6, 8]
'''


n = int(input('Введите количество чисел в одномерном массиве:'))
sp = []
for _ in range(n):
    num = int(input('Введит число в одномерный массив:'))
    sp.append(num)
new_sp = []
for i in range(len(sp)):
    if sp[i] % 2 == 0 and sp[i] < 10:
        new_sp.append(sp[i])
new_sp = sorted(new_sp, reverse=False)
if len(new_sp) == 0:
    print('Таких чисел нет!')
else:
    print('Полученный масив:', new_sp)
