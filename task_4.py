from math import sin

import numpy as np


n, m = map(int, input().split())
arr = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        res = sin((i + 1) * n + (j + 1) * m)
        if res < 0:
            res = 0
        arr[i][j] = res


if __name__ == "__main__":
    print(arr)
