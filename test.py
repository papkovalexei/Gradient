from decimal import Decimal
def c(x):
    return Decimal(str(x)) 
def PPDX(func, x, y):
    d = c(0.000000001)
    return (c(func(x + d, y)) - 2*c(func(x, y)) + c(func(x - d, y)))/c((d**2))
def PPDY(func, x, y):
    d = c(0.000000001)
    return (func(c(x), c(y) + c(d)) - 2*func(c(x), c(y)) + func(c(x), c(y) - c(d)))/(c(d)**2)
f = lambda x, y: 10*c(x)**5+c(y)**5
print(PPDX(f, 105, 100), PPDY(f, 105, 100))