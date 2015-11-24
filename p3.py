#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt("data/DR9Q.dat", usecols=(80,81,82,83))

flujo_i = datos[:,0]
error_i = datos[:,1]
flujo_z = datos[:,2]
error_z = datos[:,3]

''' defino funcion montecarlo para calcular intervalor de confianza
en donde debemos calcular el ajuste lineal osea y = ax + b'''
Nmc = 10000
a = np.zeros(Nmc)
b = np.zeros(Nmc)
    for i in range(Nmc):
        r = np.random.normal(0, 1, size=len(flujo_i))
        muestra_i = flujo_i + error_i * r
        muestra_z = flujo_z + error_z * r
        a[i], b[i] = np.polyfit(muestra_i, muestra_z,1)


        a = np.sort(a)
        b = np.sort(b)
        limite_bajo = a[int(Nmc* 0.025)]
        limite_alto = a[int(Nmc * 0.975)]
        limite_bajo_2 = b[int(Nmc* 0.025)]
        limite_alto_2 = b[int(Nmc * 0.975)]
        print "El intervalo de confianza al 95% es: [{}:{}]".format(limite_bajo, limite_alto)
        print "El intervalo de confianza al 95% es: [{}:{}]".format(limite_bajo_2, limite_alto_2)
