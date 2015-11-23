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
def funcion_modelo2(parametro2,D):
    '''otra forma de escrbir la ecuacion'''
    H = parametro2 
    return v/D
