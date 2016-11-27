#! /usr/bin/env python

"""
Descripcion del problema.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Setup
LX = 2
LY = 2
Np = 21  # numero de puntos para discretizacion
h = LX / (Np - 1)
W = 1.
N_max_iteraciones = 60
eps = 1e-6

phi = np.zeros((Np, Np))
phi_next = np.zeros((Np, Np))


def q(i, j, h):
    x = i * h - LX / 2
    y = j * h - LY / 2
    output = 2 * (2 - x**2 - y**2)
    return output


def una_iteracion(phi, phi_next, Np, h, w, q):
    for i in range(1, Np-1):
        for j in range(1, Np-1):
            phi_next[i, j] = ((1-w) * phi[i, j] +
                              w/4 * (phi[i+1, j] + phi_next[i-1, j] +
                                     phi_next[i, j-1] + phi[i, j+1] +
                                     h**2 * q(i, j, h)))
    pass


def no_ha_convergido(phi, phi_next, eps):
    # from ipdb import set_trace; set_trace()
    nonzero = phi_next != 0
    dif_relativa = np.fabs((phi_next - phi)[nonzero] / phi_next[nonzero])
    max_dif = np.max(dif_relativa)
    output = max_dif > eps
    return output

contador = 0
una_iteracion(phi, phi_next, Np, h, W, q)
while contador < N_max_iteraciones and no_ha_convergido(phi, phi_next, eps):
    phi = phi_next.copy()
    # from ipdb import set_trace; set_trace()
    una_iteracion(phi, phi_next, Np, h, W, q)
    contador += 1

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, Np)
y = np.linspace(-1, 1, Np)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, phi_next, rstride=1, cstride=1)

fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(111)
ax.imshow(phi_next, origin='bottom')
ax.contour(phi_next, origin='lower')

plt.show()

