#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyplot
from scipy.optimize import (leastsq, curve_fit)

''' calcular la cte de hubble con un intervalor de confianza de 95%'''

def funcion_modelo(parametro,D):
    '''funcionar que minimizaremos'''
    H = parametro
    return H*D


def funcion_modelo2(parametro2,v):
    '''otra forma de escrbir la ecuacion'''
    H = parametro2
    return v/D


def funcion_min(D,H):
    ''' minimizacion de la funcion '''
    parametro = H
    return funcion_modelo(parametro, D)


def funcion_min2(D, v):
    paramtro2 = H
    return funcion_modelo2(parametro2, v)

datos=np.loadtxt('hubble_original.dat')
parametro =  datos[:,0]
parametro2 = datos[:,1]

resultado = leastsq(func_min, parametro, args=(x_muestra, y_muestra, y_scales))
resultado2 = leastsq(func_min2, parametro2, args=(x_muestra, y_muestra, y_scales))
