from sympy import *
import numexpr as ne


def deriv(f, x):
    der = str(diff(f))
    der = der.replace("x", x)
    return float(ne.evaluate(der))


print("%.14f"%(deriv('x**3', '5')))
