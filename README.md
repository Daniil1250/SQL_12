# Занятия для группы 12

import numpy as np

a = np.array([0, 5, -1])
b = np.array([-4, 9, 3])

print('Вектор a:', a)
print('Вектор b:', b)

dot = np.dot(a, b)
print('Скалярное произведение a·b:', dot)

cos_angle = dot / np.linalg.norm(a) / np.linalg.norm(b)
print('Косинус угла между a и b:', cos_angle)
print('Сам угол (рад):', np.arccos(cos_angle))
print('Сам угол (град):', np.degrees(np.arccos(cos_angle)))
