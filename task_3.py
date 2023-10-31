import numpy as np

from task_1 import GRAVITY as g


x0, y0, v0, angle = 0, 0, 5, 30
angle_rad = np.radians(angle)

v0x = v0 * np.cos(angle_rad)
v0y = v0 * np.sin(angle_rad)
t = np.arange(0, 6, 1)
x = x0 + v0x * t
y = y0 + v0y * t - (g * t**2) / 2
print(np.column_stack((t, x, y)))
