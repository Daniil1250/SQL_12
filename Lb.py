import matplotlib.pyplot as plt
import numpy as np

A = np.array([-2, 0])
B = np.array([1, 2])
C = np.array([1, -1])

D = A + C - B
print("Вершина D:", D)

plt.grid()
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.arrow(*A, *(B - A), width=0.03, length_includes_head=True, facecolor='Yellow')
plt.arrow(*B, *(C - B), width=0.03, length_includes_head=True, facecolor='Red')
plt.arrow(*C, *(D - C), width=0.03, length_includes_head=True, facecolor='Green')
plt.arrow(*D, *(A - D), width=0.03, length_includes_head=True, facecolor='Blue')

for name, pt in zip('ABCD', [A, B, C, D]):
    plt.text(pt[0] + 0.2, pt[1] + 0.2, name, fontsize=14)

plt.show()



import numpy as np
a = np.array([1, 2, 0])
b = np.array([2, 1, 0])
print(np.cross(a, b))


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

O = np.array([0, 0, 0])
a = np.array([1, -2, 0])
b = np.array([0, 1, 1])
c = np.array([1, 2, 2])

ax.quiver(*O, *a, color='Red', label='a')
ax.quiver(*O, *b, color='Green', label='b')
ax.quiver(*O, *c, color='Blue', label='c')

ax.quiver(0, 0, 0, 3, 0, 0, color='Black', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 3, 0, color='Black', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 3, color='Black', arrow_length_ratio=0.1)

ax.set_xlim([-3, 3]); ax.set_ylim([-3, 3]); ax.set_zlim([-3, 3])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.legend()
plt.show()

M = np.array([a, b, c])
print("Определитель:", np.linalg.det(M))



import numpy as np

A = np.array([1, 3, -1])
B = np.array([2, -1, 4])
C = np.array([5, 0, 3])

AB = B - A
AC = C - A
cross = np.cross(AB, AC)
S = np.linalg.norm(cross) / 2

print("AB =", AB)
print("AC =", AC)
print("AB x AC =", cross)
print("Площадь треугольника S =", S)


import numpy as np

AB = np.array([3, 4, 0])
AC = np.array([-3, 0, 1])
AD = np.array([0, 2, 5])

mixed = np.dot(AB, np.cross(AC, AD))
V = abs(mixed) / 6

print("Смешанное произведение:", mixed)
print("Объём пирамиды V =", V)
