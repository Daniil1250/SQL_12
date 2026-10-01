# Занятия для группы 12

print("\nЗадание 6")

import numpy as np
import matplotlib.pyplot as plt

def arg_set(angle):
    t = np.linspace(0, 5, 200)
    return t * (np.cos(angle) + 1j*np.sin(angle))

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

angles = [np.pi/4, 5*np.pi/6]
names = ['pi/4', '5pi/6']

for ax, angle, name in zip(axes, angles, names):
    zz = arg_set(angle)
    ax.plot(np.real(zz), np.imag(zz), color='red', linewidth=2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True)
    ax.axis('equal')
    ax.set_title('Arg(z) = ' + name)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')

plt.show()
