#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


''' montecarlo para calcular intervalor de confianza
en donde debemos calcular el ajuste lineal osea y = ax + b'''


def montecarlo(flujo_i, error_i, flujo_z, error_z):

    Nmc = 10000
    a = np.zeros(Nmc)
    b = np.zeros(Nmc)
    for i in range(Nmc):
        r = np.random.normal(0, 1, size=len(flujo_i))
        muestra_i = flujo_i + error_i * r
        muestra_z = flujo_z + error_z * r
        a[i], b[i] = np.polyfit(muestra_i, muestra_z, 1)
    a = np.sort(a)
    b = np.sort(b)
    limite_bajo = a[int(Nmc * 0.025)]
    limite_alto = a[int(Nmc * 0.975)]
    limite_bajo_2 = b[int(Nmc * 0.025)]
    limite_alto_2 = b[int(Nmc * 0.975)]
    print "El intervalo de confianza al 95% es: [{}:{}]".format(limite_bajo,
                                                                limite_alto)
    print "El intervalo de confianza al 95% es: [{}:{}]".format(limite_bajo_2,
                                                                limite_alto_2)

# main

datos = np.loadtxt("data/DR9Q.dat", usecols=(80, 81, 82, 83))
flujo_i = datos[:, 0] * 3.631
error_i = datos[:, 1] * 3.631
flujo_z = datos[:, 2] * 3.631
error_z = datos[:, 3] * 3.631

m, n = np.polyfit(flujo_i, flujo_z, 1)
print "ecuación ajustada : y = {}x + {}".format(m, n)

# plot
x = np.linspace(0, 500, len(flujo_i))
plt.plot(x, m*x + n, color='r', label='Ajuste')
plt.errorbar(flujo_i, flujo_z, xerr=error_i, yerr=error_z, fmt='*',
             label='Datos Observacionales')
plt.xlabel("$ Flujo \ Banda_i [10^{-6} Jy]$", fontsize=15)
plt.ylabel("$ Flujo \ Banda_z [10^{-6} Jy]$", fontsize=15)
plt.title('$Flujo \ banda \ I \ vs \ banda \ Z $', fontsize=15)
plt.grid(True)

plt.savefig('p3.png')
plt.legend(loc=2)
plt.show()

# intervalo de confianza
intervalo = montecarlo(flujo_i, error_i, flujo_z, error_z)
