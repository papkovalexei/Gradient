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

def goldenSlice(func, a, b, eps):
    t1 = 0.381966
    t2 = 1 - t1

    x1 = []
    x2 = []

    x1.append(a[0] + (b[0] - a[0]) * t1)
    x1.append(a[1] + (b[1] - a[1]) * t1)

    x2.append(a[0] + (b[0] - a[0]) * t2)
    x2.append(a[1] + (b[1] - a[1]) * t2)

    f1 = func(x1[0] - eps, x1[1] - eps)
    f2 = func(x2[0] + eps, x2[1] + eps)

    while math.sqrt((b[0]-a[0])**2 + (b[1] - a[1])**2) > eps:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1[0] = a[0] + (b[0] - a[0]) * t1
            x1[1] = a[1] + (b[1] - a[1]) * t1
            f1 = func(x1[0], x1[1])
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2[0] = a[0] + (b[0] - a[0]) * t2
            x2[1] = a[1] + (b[1] - a[1]) * t2
            f2 = func(x2[0], x2[1])
    return [(a[0] + b[0])/2, (a[1] + b[1])/2]

def fibonacci(func, a, b, eps):
    def calcFibArr(n):
        fibArr = [0, 0, 1]

        if n == 1 or n == 2:
            return  fibArr

        while len(fibArr) <= n:
            fibArr.append(fibArr[len(fibArr) - 1] + fibArr[len(fibArr) - 2])

        return fibArr

    n = math.ceil(math.sqrt((b[0]-a[0])**2 + (b[1] - a[1])**2) / eps)
    fibArr = calcFibArr(n)

    if n == 1:
        return [(a[0] + b[0])/2, (a[1] + b[1])/2]

    y = []
    z = []

    y.append((fibArr[n - 2] / fibArr[n]) * (b[0] - a[0]) + a[0])
    y.append((fibArr[n - 2] / fibArr[n]) * (b[1] - a[1]) + a[1])

    z.append((fibArr[n - 1] / fibArr[n]) * (b[0] - a[0]) + a[0])
    z.append(((fibArr[n - 1] / fibArr[n]) * (b[1] - a[1]) + a[1]))

    fa = func(y[0], y[1])
    fb = func(z[0], z[1])

    while math.sqrt((b[0]-a[0])**2 + (b[1] - a[1])**2) > eps:
        if fa < fb:
            b = z
            z = y
            fb = fa

            y[0] = (fibArr[n - 3] / fibArr[n - 1]) * (b[0] - a[0]) + a[0]
            y[1] = (fibArr[n - 3] / fibArr[n - 1]) * (b[1] - a[1]) + a[1]
            fa = func(y[0], y[1])
        else:
            a = y
            y = z
            fa = fb
            z[0] = (fibArr[n - 2] / fibArr[n - 1]) * (b[0] - a[0]) + a[0]
            z[1] = (fibArr[n - 2] / fibArr[n - 1]) * (b[1] - a[1]) + a[1]
            fb = func(z[0], z[1])
    return [(a[0] + b[0])/2, (a[1] + b[1])/2]

def steepestDespect(z, x, y, e, ax, fig):
    stop = False
    lbm = 0.3
    x0 = x
    y0 = y

    x1 = 0
    y1 = 0

    arr = [[]]
    arr.append([])
    arr.append([])
    while stop == False:

        #ax.plot((x1, y1), (x0, y0), c='orange')
        #print(x1, y1, "to ", x0, y0)
        ax.scatter(x0, y0, c='red')
        fig.canvas.draw()
        fig.canvas.flush_events()
     

        #x1 = x0 - lbm * myGradient(z, x0, y0)[0]
        #y1 = y0 - lbm * myGradient(z, x0, y0)[1]
        print(x1, y1)
        point = fibonacci(z, [x0, y0], [-myGradient(z, x0, y0)[0], -myGradient(z, x0, y0)[1]], e)
        ax.axline((x0, y0), (-myGradient(z, x0, y0)[0], -myGradient(z, x0, y0)[1]), c='yellow')
        #keyboard.read_key()
        time.sleep(0.1)
        x1 = point[0]
        y1 = point[1]

        if (x1 - x0)**2 + (y1 - y0)**2 < e**2 and math.fabs(z(x0, y0) - z(x1, y1)) < e:
            stop = True

        x0 = x1
        y0 = y1

        arr[0].append(x1)
        arr[1].append(y1)

    return arr
    

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

    ax.contourf(x, y, z)
    ax.axis([-40, 40, -40, 40])

    arr = steepestDespect(f, -38, 20, 0.01, ax, fig)

    pylab.ioff()
    pylab.show()