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
plt.legend()
plt.show()

bc = np.cross(b, c)
mixed = np.dot(a, bc)
print("b x c =", bc)
print("Смешанное произведение a·(b×c) =", mixed)

if mixed != 0:
    print("Векторы некомпланарны → образуют базис")
else:
    print("Векторы компланарны → базис не образуют")
