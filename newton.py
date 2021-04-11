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

def PPDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - 2*func(x, y) + func(x - d, y))/(d**2)
def PPDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - 2*func(x, y) + func(x, y - d))/(d**2)

def newton(z, x, y, e, ax, fig):
    stop = False
    x0 = x
    y0 = y

    x1 = 0
    y1 = 0

    vertex = [[]]
    vertex.append([])

    while stop == False:
        x1 = x0 - PDX()
        y1 = y0 - z(x0, y0)/PDY(z, x0, y0)
        print (x1, y1)
        vertex[0].append(x0)
        vertex[0].append(x1)

        vertex[1].append(y0)
        vertex[1].append(y1)

      
        ax.scatter(x0, y0, c='red')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if math.fabs((x0 - x1)**2 + (y0 - y1)**2) < e**2:
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
    z = lambda a: 10*a[0]**2 + a[1]**2
    f = lambda x, y: 10*x**2+y**2
    x, y, z = makeData(z)

    pylab.ion()

    fig, ax = pylab.subplots()

    ax.contourf(x, y, z)
    ax.axis([-40, 40, -40, 40])

    arr = newton(f, 1, 1, 0.01, ax, fig)

    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()