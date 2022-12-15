import numpy as np

arr = [23, 30, 10, 16, 29, 29, 12, 15, 19, 18, 14, 30, 11, 11, 19]
arr_2 = [16, 20, 23, 24, 28, 26, 12, 12, 19, 12, 15, 18, 24, 27, 12]
l = len(arr)

ranks = [int(i) + 1 for i in np.array(arr).argsort().argsort()]
ranks_2 = [int(i) + 1 for i in np.array(arr_2).argsort().argsort()]

n = 0
for i in range(l):
    n += (ranks[i] - ranks_2[i]) ** 2
conn_value = abs(1 - (6 * n / (l * (l ** 2 - 1))))

print(conn_value)