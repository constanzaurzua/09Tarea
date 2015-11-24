#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import (leastsq, curve_fit)

''' calcular la cte de hubble con un intervalor de confianza de 95%'''

def funcion_modelo(parametro,D):
    '''funcionar que minimizaremos'''
    H = parametro
    return H*D


def funcion_modelo2(parametro,v):
    '''otra forma de escrbir la ecuacion'''
    H = parametro
    return v/H


def funcion_min(D,H):
    ''' minimizacion de la funcion '''
    parametro = H
    return funcion_modelo(parametro, D)


def funcion_min2(v,H):
    '''minimiza la funcion 2'''
    parametro = H
    return funcion_modelo2(parametro, v)


def bootstrap(datos):
    '''funcion que calculara errores'''

    N ,N1= datos.shape
    Nboot = 10000
    mean_values = np.zeros(Nboot)

    for i in range(Nboot):
        s = np.random.randint(low=0, high=N, size=N)
        datos_f = datos[s][s]
        distancia = datos_f[:,0]
        velocidad = datos_f[:,1]
        a_optimo, a_covarianza = curve_fit(funcion_min, distancia, velocidad, a_0)
        a_optimo2, a_covarianza2 = curve_fit(funcion_min2, velocidad, distancia, a_0)
        a_promedio = (a_optimo + a_optimo2) / 2
        mean_values[i] = a_promedio
    fig2, ax2 = plt.subplots()
    plt.hist(mean_values, bins=30)
    plt.axvline(valor_promedio, color='r')
    ax2.set_title("Simulacion de bootstrap")
    ax2.set_xlabel("H [Km/s /Mpc]")
    ax2.set_ylabel("frecuencia")

    mean_values = np.sort(mean_values)
    limite_bajo = mean_values[int(Nboot * 0.025)]
    limite_alto = mean_values[int(Nboot * 0.975)]
    print "El intervalo de confianza al 95% es: [{}:{}]".format(limite_bajo, limite_alto)



# main

np.random.seed(5000)

datos = np.loadtxt("SNIa.dat",usecols=(1,2))
distancia =  datos[:,0]
velocidad = datos[:,1]
a_0 = 2
a_optimo, a_covarianza = curve_fit(funcion_min, distancia, velocidad, a_0)
a_optimo2, a_covarianza_2 = curve_fit(funcion_min2, velocidad, distancia, a_0)

a_promedio = (a_optimo + a_optimo2) / 2
valor_promedio = a_promedio
print valor_promedio


#plot

fig = plt.figure()
fig.clf()
ax1 = fig.add_subplot(111)

ax1.plot(distancia, velocidad, '*', label="Datos experimentales")
ax1.plot(distancia, valor_promedio * distancia, label="Ajuste")

#ax1.set_xlim([-5, 5])
ax1.set_xlabel("Distancia $[Mpc]$")
ax1.set_ylabel("Velocidad $[km/s]$")
ax1.set_title("Grafico de distancia $[Mpc]$ versus velocidad $[km/s]$")

plt.legend(loc='upper left')
plt.draw()
plt.show()

# Intervalo de confianza
interv_confianza = bootstrap(datos)
