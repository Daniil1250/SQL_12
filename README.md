print("\nЗадание 7")

import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

x = -8 + 16*rng.rand(80000)
y = -8 + 16*rng.rand(80000)
z = x + 1j*y

fig, axes = plt.subplots(1, 2, figsize=(14, 8))

L1 = (np.angle(z) >= np.pi/6) & (np.abs(z) <= 2)
axes[0].plot(np.real(z[L1]), np.imag(z[L1]), '.', color='blue', markersize=2)

L2 = (-np.angle(z) >= np.pi/6) & (np.abs(z) <= 2) & (np.abs(z - 0.2 - 1j) <= 0.2)
axes[0].plot(np.real(z[L2]), np.imag(z[L2]), '.', color='red', markersize=2)

axes[0].axhline(y=0, color='k')
axes[0].axvline(x=0, color='k')
axes[0].grid(True)
axes[0].axis('equal')
axes[0].set_title('Задание 7(1)')
axes[0].set_xlabel('Re(z)')
axes[0].set_ylabel('Im(z)')

L3 = (np.angle(6j - z) >= np.pi/3) & (np.angle(6j - z) <= 2*np.pi/3)
axes[1].plot(np.real(z[L3]), np.imag(z[L3]), '.', color='green', markersize=2)

L4 = (np.abs(np.real(z)) <= 1.7) & (np.imag(z) >= 0) & (np.imag(z) <= 3)
axes[1].plot(np.real(z[L4]), np.imag(z[L4]), '.', color='orange', markersize=2)

L5 = (np.real(z) >= -1.2) & (np.real(z) <= -0.6) & (np.imag(z) >= 0) & (np.imag(z) <= 2)
axes[1].plot(np.real(z[L5]), np.imag(z[L5]), '.', color='purple', markersize=2)

L6 = (np.real(z) >= 0.7) & (np.real(z) <= 1.3) & (np.imag(z) >= 1.3) & (np.imag(z) <= 1.9)
axes[1].plot(np.real(z[L6]), np.imag(z[L6]), '.', color='brown', markersize=2)

L7 = np.abs(z - 3 - 7j) <= 0.8
axes[1].plot(np.real(z[L7]), np.imag(z[L7]), '.', color='pink', markersize=2)

L8 = (np.abs(z - 5 - 6j) <= 0.5) & (np.abs(z - 5.5 - 5.9j) >= 0.6)
axes[1].plot(np.real(z[L8]), np.imag(z[L8]), '.', color='cyan', markersize=2)

axes[1].axhline(y=0, color='k')
axes[1].axvline(x=0, color='k')
axes[1].grid(True)
axes[1].axis('equal')
axes[1].set_title('Задание 7(2)')
axes[1].set_xlabel('Re(z)')
axes[1].set_ylabel('Im(z)')

plt.show()
