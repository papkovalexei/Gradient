import numpy
import math

def PDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - func(x, y))/d
def PDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - func(x, y))/d

def myGradient(func, x, y): 
    return (PDX(func, x, y), PDY(func, x, y))

def defGradient(z, x, y, e):
    stop = False
    iter = 0
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
        
        if (x1 - x0)**2 + (y1 - y0)**2 < e**2 and math.fabs(z(x0, y0) - z(x1, y1)) < e:
            stop = True

        x0 = x1
        y0 = y1
        iter += 1

    return (x0, y0, iter)


if __name__ == '__main__':
    z = lambda a: (a[0]**2)/15 + (a[1]**2)/2
    f = lambda x, y: (x**2)/15 + (y**2)/2

    arr = defGradient(f, -38, 20, 0.01)
    print(arr)
