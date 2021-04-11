import numpy
import math
import pylab
import time
from sympy import *
import keyboard
import numpy.ma as ma
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

def PDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - func(x, y))/d
def PDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - func(x, y))/d

def myGradient(func, x, y): 
    return (PDX(func, x, y), PDY(func, x, y))

def dichotomy(func, a1, b1, eps):
    a = -1e3
    b = 1e3
    
    while math.fabs(b - a > eps):
        y1 = func(a1[0] + a * b1[0], a1[1] + a * b1[1])
        y2 = func(a1[0] + b * b1[0], a1[1] + b * b1[1])

        c = (a + b) / 2
        
        if y1 < y2:
            b = c
        else:
            a = c
    return (a + b) / 2

def conjugateDirection(z, x, y, e, ax, fig):
    s1 = [1, 0]
    s2 = [0, 1]

    vertex = [[]]
    vertex.append([])

    xOld = x
    yOld = y

    while myGradient(z, x, y)[0]**2 + myGradient(z, x, y)[1]**2 > e**2:
        lbm = dichotomy(z, (x, y), s2, e)
        x1 = x + lbm*s2[0]
        y1 = y + lbm*s2[1]

        lbm = dichotomy(z, (x1, y1), s1, e)

        x2 = x1 + lbm*s1[0]
        y2 = y1 + lbm*s1[1]

        lbm = dichotomy(z, (x2, y2), s2, e)

        x3 = x2 + lbm*s2[0]
        y3 = y2 + lbm*s2[1]

        s2[0] = x3 - x1
        s2[1] = y3 - y1

        x = x3
        y = y3

        vertex[0].append(xOld)
        vertex[0].append(x)

        vertex[1].append(yOld)
        vertex[1].append(y)

        xOld = x
        yOld = y
    return vertex

def makeData(z):
    x = numpy.arange(-40, 40, 0.5)
    y = numpy.arange(-40, 40, 0.5)
    xgrid, ygrid = numpy.meshgrid(x, y)

    zgrid = z([xgrid, ygrid])
    return xgrid, ygrid, zgrid

if __name__ == '__main__':
    z = lambda a: (a[0]**2)/15 + (a[1]**2)/2
    f = lambda x, y: (x**2)/15 + (y**2)/2
    x, y, z = makeData(z)

    pylab.ion()

    fig, ax = pylab.subplots()

    ax.contourf(x, y, z, levels=20)
    ax.axis([-40, 40, -40, 40])

    arr = conjugateDirection(f, -38, 20, 0.0001, ax, fig)
    ax.set_ylabel('y', fontsize = 15)
    ax.set_xlabel('x', fontsize = 15)
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()