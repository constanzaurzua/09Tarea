#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def montecarlo():
''' defino funcion montecarlo para calcular intervalor de confianza'''
    Nmc = 10000
    mean_values = np.zeros(Nmc)
    for i in range(Nmc):
        r = np.random.normal(0, 1, size=len(medicion))
        muestra_i = flujo_i + error_i * r
        muestra_z = flujo_z + error_z * r
        mean_values[i] = np.polyfit(muestra_i,muestra_z,1)

#main
datos = np.loadtxt("data/DR9Q.dat", usecols=(80,81,82,83))

flujo_i = datos[:,0]
error_i = datos[:,1]
flujo_z = datos[:,2]
error_z = datos[:,3]
