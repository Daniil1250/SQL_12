import matplotlib.pyplot as plt
import numpy as np

A = np.array([-2, 0])
B = np.array([1, 2])
C = np.array([1, -1])

D = A + C - B
print("Вершина D:", D)

plt.figure(figsize=(6, 6))
plt.grid()
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.arrow(*A, *(B - A), width=0.03, length_includes_head=True, facecolor='Yellow')
plt.arrow(*B, *(C - B), width=0.03, length_includes_head=True, facecolor='Red')
plt.arrow(*C, *(D - C), width=0.03, length_includes_head=True, facecolor='Green')
plt.arrow(*D, *(A - D), width=0.03, length_includes_head=True, facecolor='Blue')

for name, pt in zip('ABCD', [A, B, C, D]):
    plt.text(pt[0] + 0.2, pt[1] + 0.2, name, fontsize=14)

plt.title("Параллелограмм ABCD")
plt.show()





import matplotlib.pyplot as plt
import numpy as np

a = np.array([0, 5, -1])
b = np.array([-4, 9, 3])

dot = np.dot(a, b)
cos_angle = dot / np.linalg.norm(a) / np.linalg.norm(b)
angle = np.arccos(cos_angle)

print('Скалярное произведение a·b:', dot)
print('Косинус угла:', cos_angle)
print('Угол (рад):', angle)
print('Угол (град):', np.degrees(angle))

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

O = np.array([0, 0, 0])
ax.quiver(*O, *a, color='Blue', label='a', arrow_length_ratio=0.1)
ax.quiver(*O, *b, color='Green', label='b', arrow_length_ratio=0.1)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 10])
ax.set_zlim([-5, 5])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title(f"Угол между a и b = {np.degrees(angle):.2f}°")
plt.legend()
plt.show()




import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

O = np.array([0, 0, 0])
a = np.array([1, 2, 0])
b = np.array([2, 1, 0])
c = np.cross(a, b)

print("a x b =", c)

ax.quiver(*O, *a, color='Blue', label='a', arrow_length_ratio=0.1)
ax.quiver(*O, *b, color='Green', label='b', arrow_length_ratio=0.1)
ax.quiver(*O, *c, color='Red', label='a x b', arrow_length_ratio=0.1)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-4, 2])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title("Векторное произведение a × b")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

O = np.array([0, 0, 0])
a = np.array([1, -2, 0])
b = np.array([0, 1, 1])
c = np.array([1, 2, 2])

ax.quiver(*O, *a, color='Red', label='a', arrow_length_ratio=0.1)
ax.quiver(*O, *b, color='Green', label='b', arrow_length_ratio=0.1)
ax.quiver(*O, *c, color='Blue', label='c', arrow_length_ratio=0.1)

ax.quiver(0, 0, 0, 3, 0, 0, color='Black', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 3, 0, color='Black', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 3, color='Black', arrow_length_ratio=0.1)

ax.set_xlim([-3, 3]); ax.set_ylim([-3, 3]); ax.set_zlim([-3, 3])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title("Базис: a, b, c")

M = np.array([a, b, c])
print("Определитель:", np.linalg.det(M))

plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

A = np.array([1, 3, -1])
B = np.array([2, -1, 4])
C = np.array([5, 0, 3])

AB = B - A
AC = C - A
cross = np.cross(AB, AC)
S = np.linalg.norm(cross) / 2

print("AB x AC =", cross)
print("Площадь S =", S)

ax.quiver(*A, *AB, color='Blue', label='AB', arrow_length_ratio=0.1)
ax.quiver(*A, *AC, color='Green', label='AC', arrow_length_ratio=0.1)
ax.quiver(*A, *cross, color='Red', label='AB x AC', arrow_length_ratio=0.1)

pts = np.array([A, B, C, A])
ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], color='Purple', linewidth=2)

for name, pt in zip('ABC', [A, B, C]):
    ax.text(pt[0], pt[1], pt[2], name, fontsize=14)

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title(f"Треугольник ABC, S = {S:.3f}")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

A = np.array([0, 0, 0])
AB = np.array([3, 4, 0])
AC = np.array([-3, 0, 1])
AD = np.array([0, 2, 5])

B = A + AB
C = A + AC
D = A + AD

mixed = np.dot(AB, np.cross(AC, AD))
V = abs(mixed) / 6
print("Смешанное произведение:", mixed)
print("Объём V =", V)

ax.quiver(*A, *AB, color='Blue', label='AB', arrow_length_ratio=0.1)
ax.quiver(*A, *AC, color='Green', label='AC', arrow_length_ratio=0.1)
ax.quiver(*A, *AD, color='Red', label='AD', arrow_length_ratio=0.1)

edges = [(A, B), (A, C), (A, D), (B, C), (B, D), (C, D)]
for p, q in edges:
    ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], color='Purple', linewidth=1.5)

for name, pt in zip('ABCD', [A, B, C, D]):
    ax.text(pt[0], pt[1], pt[2], name, fontsize=14)

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title(f"Пирамида ABCD, V = {V}")
plt.legend()
plt.show()




