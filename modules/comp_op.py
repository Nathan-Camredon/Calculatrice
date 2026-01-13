PI = 3.141592653589793

def percent(valor, rate):
    return valor * rate / 100

def square(x):
    return x ** 2

def square_root(x):
    pass

def rad(deg):
    return deg * PI / 180

def sin(x):
    return x - (x**3)/6 + (x**5)/120

def cos(x):
    return 1 - (x**2)/2 + (x**4)/24

def tan(x):
    c = cos(x)
    if c == 0:
        raise ValueError("Tangente non définie")
    return sin(x) / c
