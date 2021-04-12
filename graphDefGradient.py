import numpy
import math
import pylab
import time
from sympy import *
import keyboard
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

def defGradient(z, x, y, e, ax, fig):
    stop = False
    lbm = 0.01
    x0 = x
    y0 = y

    x1 = 0
    y1 = 0

    vertex = [[]]
    vertex.append([])
    
    while stop == False:
        x1 = x0 - myGradient(z, x0, y0)[0] * lbm
        y1 = y0 - myGradient(z, x0, y0)[1] * lbm
        
        vertex[0].append(x0)
        vertex[0].append(x1)

        vertex[1].append(y0)
        vertex[1].append(y1)
        if (x1 - x0)**2 + (y1 - y0)**2 < e**2 and math.fabs(z(x0, y0) - z(x1, y1)) < e:
            stop = True

        x0 = x1
        y0 = y1

    return vertex
    

def makeData(z):
    x = numpy.arange(-40, 40, 0.5)
    y = numpy.arange(-40, 40, 0.5)
    xgrid, ygrid = numpy.meshgrid(x, y)

    zgrid = z([xgrid, ygrid])
    return xgrid, ygrid, zgrid


if __name__ == '__main__':
    z = lambda a: (a[0]**4) + (a[1]**4)
    f = lambda x, y: (x**4) + (y**4)
    x, y, z = makeData(z)

    pylab.ion()

    fig, ax = pylab.subplots()

    ax.contourf(x, y, z)
    ax.axis([-40, 40, -40, 40])

    arr = defGradient(f, 5, 5, 0.01, ax, fig)

    ax.plot(arr[0], arr[1], c='red')
    ax.set_ylabel('y', fontsize = 15)
    ax.set_xlabel('x', fontsize = 15)
    pylab.ioff()
    pylab.show()