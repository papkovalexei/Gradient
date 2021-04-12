import numpy
import math

def PD(f, args, i):
    d = 0.000001
    args_local = args.copy()
    args_local[i] += d
    return (f(args_local) - f(args))/d

def myGradient(func, args): 
    argsPD = args.copy()

    i = 0
    while i < len(argsPD):
        argsPD[i] = PD(f, argsPD, i)
        i += 1
    return argsPD

def goldenSlice(func, argsL1, argsR1, eps):
    iter = 0
    t1 = 0.381966
    t2 = 1 - t1

    argsL = argsL1.copy()
    argsR = argsR1.copy()

    x1 = argsL + (argsR - argsL) * t1
    x2 = argsL + (argsR - argsL) * t2
    
    f1 = func(x1 - eps)
    f2 = func(x2 + eps)

    i = 0
    delta = 0
    while i < len(argsR):
        delta += (argsL[i] - argsR[i])**2
        i += 1

    while delta > eps**2:
        if f1 < f2:
            argsR = x2
            x2 = x1
            f2 = f1
            x1 = argsL + (argsR - argsL) * t1
            f1 = func(x1)
        else:
            argsL = x1
            x1 = x2
            f1 = f2
            x2 = argsL + (argsR - argsL) * t2
            f2 = func(x2)
        i = 0
        delta = 0
        while i < len(argsR):
            delta += (argsL[i] - argsR[i])**2
            i += 1
    return (argsL + argsR) / 2

def steepestDespect(f, args, e):
    iter = 0
    stop = False
    
    args0 = args.copy()
    args1 = args0.copy()

    while not stop:
        args1 = goldenSlice(f, args0, -myGradient(f, args0), e)

        i = 0
        delta = 0
        while i < len(args0):
            delta += (args1[i] - args0[i])**2
            i += 1
            
        if delta < e**2 and math.fabs(f(args1) - f(args0)) < e:
            stop = True
        args0 = args1.copy()
    print(args0)
    return iter

f = lambda a: a[0]**2 + a[1]**2 + a[2]**2
steepestDespect(f, numpy.array([10, 10, 13]), 0.1)