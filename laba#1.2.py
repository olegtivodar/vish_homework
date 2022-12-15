#  laba №2 variant(11)
chislo_1, chislo_2, chislo_3 = map(float, input('Введите число: ').split())
counter = 0
if chislo_1 > 0:
    counter += 1
if chislo_2 > 0:
    counter += 1
if chislo_3 > 0:
    counter += 1
print('Количество положительных чисел:', counter)