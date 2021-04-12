from decimal import Decimal
import math
import numpy
def c(x):
    return Decimal(str(x)) 
def PDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - func(x, y))/d
def PDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - func(x, y))/d
def PPDX(func, x, y):
    d = c(0.000000001)
    return (c(func(x + d, y)) - 2*c(func(x, y)) + c(func(x - d, y)))/c((d**2))
def PPDY(func, x, y):
    d = c(0.000000001)
    return (func(c(x), c(y) + c(d)) - 2*func(c(x), c(y)) + func(c(x), c(y) - c(d)))/(c(d)**2)
def myGradient(func, x, y): 
    return (PDX(func, x, y), PDY(func, x, y))
def sqGradient(func, x, y):
    return math.sqrt(myGradient(func, x, y)[0]**2 + myGradient(func, x, y)[1]**2)
def cond(func, x, y):
    return (math.fabs(PDX(fx, x, y)) + math.fabs(PDY(fx, x, y)))/(math.fabs(fx(x, y))/(math.fabs(x) + math.fabs(y)))
def c(x):
    return Decimal(str(x)) 

def PD(f, args, i):
    d = c(0.00000001)
    args_local = args.copy()
    args_local[i] += d

    return (f(args_local) - f(args))/d

def cond(f, args):
    pd = c(0)
    s = c(0)

    i = 0
    while i < len(args):
        pd += c(math.fabs(PD(f, args, i)))
        s += c(math.fabs(args[i]))
        print(s, pd)
        i += 1
    return (pd*s)/(f(args))
    
def T(n, k):
    z_str = ''

    for i in range(n):
        z_str += '(a[' + str(i) + ']**c(2))'

        if i != n - 1:
            z_str += ' + '
    print(z_str) 
array = numpy.array([1, 2])
array += 2
print(-array)