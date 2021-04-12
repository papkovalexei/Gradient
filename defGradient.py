import numpy
import math
import pylab
import time
from random import randint
from sympy import *
import keyboard
from decimal import Decimal
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

def c(x):
    return Decimal(str(x)) 

def PD(f, args, i):
    d = c(0.00000001)
    args_local = args.copy()
    args_local[i] += d
    return (f(args_local) - f(args)).quantize(c(1)/(10**c(30)))/d

def cond(f, args):
    pd = c(0)
    s = c(0)

    i = 0
    while i < len(args):
        pd += c(math.fabs(PD(f, args, i)))
        s += c(math.fabs(args[i]))
        i += 1
    return (pd*s)/(f(args))

def defGradient(f, args0, e):
    iter = 0
    lbm = c(0.01)
    stop = False
    args1 = args0.copy()
    args2 = args0.copy()
    while not stop:
        i = 0
        while i < len(args2):
            args2[i] = args1[i] - PD(f, args1, i) * lbm
            i += 1
        i = 0
        delta = 0
        while i < len(args2):
            delta += (args1[i] - args2[i])**2
            i += 1
            
        if delta < e**2 and math.fabs(f(args1) - f(args2)) < e:
            stop = True
        args1 = args2.copy()
        iter += 1
    return iter
def getFunc(n, k):
    k1 = k
    k1 /= n
    z_str = 'f = lambda a: '

    for i in range(n):
        z_str += '(a[' + str(i) + ']**c('+ str(k1) +'))'

        if i != n - 1:
            z_str += ' + '
    return z_str

def T(f, n, k):
    args = numpy.array([c(5)])
    i = 1
    while i < n:
        args = numpy.append(args, c(5))
        i += 1
    return defGradient(f, args, 0.1)

if __name__ == '__main__':
    n = 3
    k = 4
    fig, ax = pylab.subplots()

    n = 1
    k = 4
    vertex = [[]]
    vertex.append([])
    while k < 5:
        while n < 1000:
            k = 4*n
            exec(getFunc(n, k)) in globals()
            try:
                vertex[1].append(T(f, n, k))
            except:
                break
            vertex[0].append(n)
            n += 1
            print("Process: ", n)
        k += 1
    ax.plot(vertex[0], vertex[1])
    ax.set_xlabel("n")
    ax.set_ylabel("Количество итераций")
    pylab.show()

