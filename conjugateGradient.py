import numpy
import math
import numpy.ma as ma

def PDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - func(x, y))/d
def PDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - func(x, y))/d

def myGradient(func, x, y): 
    return (PDX(func, x, y), PDY(func, x, y))

def goldenSlice(func, a1, b1, eps):
    a = 0
    b = 1e5
    x0 = a + 0.5 * (3 - math.sqrt(5)) * (b - a)
    x1 = b - x0 + a

    while math.fabs(b - a) > eps:
        xL = a1[0] + x0 * b1[0]
        yL = a1[1] + x0 * b1[1]

        xR = a1[0] + x1 * b1[0]
        yR = a1[1] + x1 * b1[1]

        if  func(xL, yL) < func(xR, yR):
            b = x1
        else:
            a = x0
        x1 = x0
        x0 = b + a - x1
    return (a + b)/2

def conjugateGradient(z, x, y, e):
    stop = False
    iter = 0
    p = []
    p.append(-myGradient(z, x, y)[0])
    p.append(-myGradient(z, x, y)[1])

    grad = p

    while stop == False:
        iter += 1

        alpha = goldenSlice(z, (x, y), p, e)

        x = x + alpha * p[0]
        y = y + alpha * p[1]

        grad1 = []
        grad1.append(-myGradient(z, x, y)[0])
        grad1.append(-myGradient(z, x, y)[1])

        if iter % 2 == 0:
            beta = 0    
        else:
            beta = ma.innerproduct(grad1, grad1) / ma.innerproduct(grad, grad)

        p[0] = grad1[0] + beta * p[0]
        p[1] = grad1[1] + beta * p[1]
        
        grad = grad1

        if ma.innerproduct(grad, grad) <= e:
            stop = True
    return (x, y, iter)

if __name__ == '__main__':
    z = lambda a: (a[0]**2)/15 + (a[1]**2)/2
    f = lambda x, y: (x**2)/15 + (y**2)/2

    arr = conjugateGradient(f, -38, 20, 0.0001)

    print(arr)