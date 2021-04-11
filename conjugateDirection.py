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

def conjugateDirection(z, x, y, e):
    s1 = [1, 0]
    s2 = [0, 1]
    iter = 0

    while myGradient(z, x, y)[0]**2 + myGradient(z, x, y)[1]**2 > e**2:
        iter += 1
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
    return (x, y, iter)


if __name__ == '__main__':
    f = lambda x, y: (x**2)/15 + (y**2)/2

    arr = conjugateDirection(f, -38, 20, 0.0001)

    print(arr)