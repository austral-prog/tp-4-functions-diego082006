# Replace the "ANSWER HERE" for your answer

import math

def roots(a, b, c):
    discriminante = b**2 - 4 * a * c
    
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2 * a)
        r2 = (-b - math.sqrt(discriminante)) / (2 * a)
        
        if r1 < r2:
            r1, r2 = r2, r1
            
        return f"({r1}, {r2})"
    
    elif discriminante == 0:
        r = (-b) / (2 * a)
        return f"({r})"
    
    else:
        return "( )"


def value_y(a, b, c, x):
    return a * x**2 + b * x + c


def to_string(a, b, c):
    resultado = "f(x) = "
    primero = True

    if a != 0:
        resultado += f"{a} * X^2"
        primero = False

    if b != 0:
        if not primero:
            resultado += " + "
        resultado += f"{b} * X"
        primero = False

    if c != 0:
        if not primero:
            resultado += " + "
        resultado += f"{c}"
        primero = False

    if primero:  
        resultado += "0"

    return resultado


def derivation(a, b, c):
    resultado = "f'(x) = "
    primero = True

    if a != 0:
        resultado += f"{2*a} * X"
        primero = False

    if b != 0:
        if not primero:
            resultado += " + "
        resultado += f"{b}"
        primero = False

    if primero:  
        resultado += "0"

    return resultado
