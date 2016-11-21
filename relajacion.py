#! /usr/bin/env python

"""
Descripcion del problema.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Setup
LX = 2
LY = 2
Np = 5  # numero de puntos para discretizacion
h = LX / (Np - 1)
W = 1.


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




una_iteracion(phi, phi_next, Np, h, W, q)
phi = phi_next

una_iteracion(phi, phi_next, Np, h, W, q)
