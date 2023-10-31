import numpy as np


N, M = 4, 3
arr1, arr2, res = [np.zeros((N, M)) for _ in range(3)]
print("Заполните первый массив размером 4х3")
for i in range(N):
    for j in range(M):
        arr1[i, j] = int(input())

print("\nЗаполните второй массив размером 4х3")
for i in range(N):
    for j in range(M):
        arr2[i, j] = int(input())

for i in range(N):
    for j in range(M):
        if arr1[i, j] > arr2[i, j]:
            res[i, j] = arr1[i, j]
        else:
            res[i, j] = arr2[i, j]
print(res)
