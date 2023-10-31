import numpy as np


arr = np.zeros(5)
for i in range(4):
    arr[i] = int(input())

new_el, ind = map(
    int,
    input(
        (
            "Введите значение которое хотите вставить в массив "
            "и его индекс через пробел: "
        )
    ).split(),
)
arr = np.insert(arr, ind, new_el)
print(arr)
