def PPDX(func, x, y):
    d = 0.000000001
    return (func(x + d, y) - 2*func(x, y) + func(x - d, y))/(d**2)
def PPDY(func, x, y):
    d = 0.000000001
    return (func(x, y + d) - 2*func(x, y) + func(x, y - d))/(d**2)
f = lambda x, y: 10*x**2+y**2
print(PPDX(f, 10, 10), PPDY(f, 10, 10))