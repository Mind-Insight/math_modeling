from math import sqrt, pi, tan, cos

from task_1 import (
    GRAVITY as g,
    PLANCK_CONSTANT as h,
    BOLTZMANN_CONSTANT as k,
    EULER_CONSTANT as e,
)


print(
    sqrt(
        (g * 100 * tan(30) ** 2)
        / (2 * cos(pi / 3) ** 2 * (1 - tan(30) * tan(pi / 3)))
    )
)

print(
    (2 / sqrt(pi))
    * (h / ((k * 200) ** (3 / 2)))
    * (e ** (-300 / k * 200))
    * (300 ** (200 / 2))
)
