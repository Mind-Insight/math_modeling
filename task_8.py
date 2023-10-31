import numpy as np

rows, cols = map(int, input().split())
arr = np.zeros((rows, cols))

print("Заполните массив: ")
for i in range(rows):
    for j in range(cols):
        arr[i, j] = int(input())

max_elements = np.max(arr, axis=0)
print(max_elements)
