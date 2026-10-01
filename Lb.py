print("Задание 1")

import numpy as np

a = (2+3j)*(3-1j)
print("1) (2+3i)(3-i) =", a)

b = (1-1j)**3 - (1+1j)**3
print("2) (1-i)^3 - (1+i)^3 =", b)

print("3) i^k, k=1..8:")
for k in range(1, 9):
    print("   i^%d = %s" % (k, 1j**k))

c = (2-3j)/(1+4j) + (4-1j)
print("4) (2-3i)/(1+4i) + (4-i) =", c)


print("\nЗадание 2")

import numpy as np

z1 = (4-5j)*(5-6j**3)
print("1) z =", z1)
print("   Re =", np.real(z1), " Im =", np.imag(z1))
print("   |z| =", np.abs(z1), " arg =", np.angle(z1), " conj =", np.conj(z1))

z2 = (1+1j)**15
print("2) z =", z2)
print("   Re =", np.real(z2), " Im =", np.imag(z2))
print("   |z| =", np.abs(z2), " arg =", np.angle(z2), " conj =", np.conj(z2))


print("\nЗадание 3")

import numpy as np
import matplotlib.pyplot as plt

z1 = 1+3j
z2 = 3+4j
z3 = z1 + z2
z4 = z1 - z2
print("z1 =", z1, " z2 =", z2)
print("z3 = z1+z2 =", z3)
print("z4 = z1-z2 =", z4)

plt.figure(figsize=(7, 7))
vals = np.array([z1, z2, z3, z4])
colors = ['red', 'green', 'blue', 'orange']
for i in range(4):
    plt.quiver(0, 0, np.real(vals[i]), np.imag(vals[i]),
               angles='xy', scale_units='xy', scale=1, color=colors[i])
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True)
plt.axis('equal')
plt.title('z1, z2, z1+z2, z1-z2')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()


print("\nЗадание 4")

import numpy as np
import matplotlib.pyplot as plt

z = 2 - 2j
r = np.abs(z)
phi = np.angle(z)
n = 8
k = np.arange(n)
zroot = r**(1/n) * (np.cos((phi + 2*np.pi*k)/n) + 1j*np.sin((phi + 2*np.pi*k)/n))
print("Корни:", zroot)

R = r**(1/n)
t = np.linspace(0, 2*np.pi, 200)

plt.figure(figsize=(7, 7))
plt.plot(np.real(zroot), np.imag(zroot), 'og')
plt.plot(R*np.cos(t), R*np.sin(t), 'b--')
poly = np.append(zroot, zroot[0])
plt.plot(np.real(poly), np.imag(poly), 'r-.')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axis('equal')
plt.grid(True)
plt.title('Корни 8-й степени из 2-2i')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()


print("\nЗадание 5")

import numpy as np

z = 2 - 2j
r = np.abs(z)
phi = np.angle(z)
n = 8
k = np.arange(n)
zroot = r**(1/n) * (np.cos((phi + 2*np.pi*k)/n) + 1j*np.sin((phi + 2*np.pi*k)/n))

left = np.real(zroot) < 0
print("Корни в левой полуплоскости:")
print(zroot[left])

big_arg = np.angle(zroot) > np.pi/3
print("Корни с arg > pi/3:")
print(zroot[big_arg])


print("\nЗадание 6")

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, angle, name in zip(axes, [np.pi/4, 5*np.pi/6], ['pi/4', '5pi/6']):
    t = np.linspace(0, 5, 100)
    zz = t * (np.cos(angle) + 1j*np.sin(angle))
    ax.plot(np.real(zz), np.imag(zz), color='red', linewidth=2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True)
    ax.axis('equal')
    ax.set_title('Arg(z) = ' + name)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
plt.show()


print("\nЗадание 7")

import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

x = -3 + 6*rng.rand(20000)
y = -3 + 6*rng.rand(20000)
z = x + 1j*y

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

L1 = (np.angle(z) >= np.pi/6) & (np.abs(z) <= 2)
axes[0].plot(np.real(z[L1]), np.imag(z[L1]), '.', color='blue')
L2 = (-np.angle(z) >= np.pi/6) & (np.abs(z) <= 2) & (np.abs(z - 0.2 - 1j) <= 0.2)
axes[0].plot(np.real(z[L2]), np.imag(z[L2]), '.', color='red')
axes[0].axhline(y=0, color='k')
axes[0].axvline(x=0, color='k')
axes[0].grid(True)
axes[0].axis('equal')
axes[0].set_title('Arg(z) >= pi/6 и -Arg(z) >= pi/6')
axes[0].set_xlabel('Re(z)')
axes[0].set_ylabel('Im(z)')

L3 = (np.angle(6j - z) >= np.pi/3) & (np.angle(6j - z) <= 2*np.pi/3)
axes[1].plot(np.real(z[L3]), np.imag(z[L3]), '.', color='green')

L4 = (np.abs(np.real(z)) <= 1.7) & (np.imag(z) >= 0) & (np.imag(z) <= 3)
axes[1].plot(np.real(z[L4]), np.imag(z[L4]), '.', color='orange')

L5 = (np.real(z) >= -1.2) & (np.real(z) <= -0.6) & (np.imag(z) >= 0) & (np.imag(z) <= 2)
axes[1].plot(np.real(z[L5]), np.imag(z[L5]), '.', color='purple')

L6 = (np.real(z) >= 0.7) & (np.real(z) <= 1.3) & (np.imag(z) >= 1.3) & (np.imag(z) <= 1.9)
axes[1].plot(np.real(z[L6]), np.imag(z[L6]), '.', color='brown')

L7 = np.abs(z - 3 - 7j) <= 0.8
axes[1].plot(np.real(z[L7]), np.imag(z[L7]), '.', color='pink')

L8 = (np.abs(z - 5 - 6j) <= 0.5) & (np.abs(z - 5.5 - 5.9j) >= 0.6)
axes[1].plot(np.real(z[L8]), np.imag(z[L8]), '.', color='cyan')

axes[1].axhline(y=0, color='k')
axes[1].axvline(x=0, color='k')
axes[1].grid(True)
axes[1].axis('equal')
axes[1].set_title('Задание 7(2)')
axes[1].set_xlabel('Re(z)')
axes[1].set_ylabel('Im(z)')

plt.show()
