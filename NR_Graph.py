import matplotlib.pyplot as pt
import numpy as np
import sympy as sp

x = sp.Symbol('x')
f = sp.sympify(input("Enter the Function : "))
df = sp.diff(f, x)

lam_f = sp.lambdify(x, f, 'numpy')
lam_df = sp.lambdify(x, df, 'numpy')

x0 = float(input("Enter the Initial Guess : "))
xn = x0

x_roots = [x0]

for i in range(20):
    if lam_df(xn) == 0.0:
        print("NR-Method will not Work")
        break
    x_new = xn - (lam_f(xn)/lam_df(xn)) 
    x_roots.append(x_new)
    print(f"iterations {i+1} ,  x = {x_new}")

    if abs(x_new - xn) < 0.00001:
        print(f"Converge after {i+1} iterations")
        print(f"Estimated root : {x_new}")
        break
    else:
        xn = x_new

xV = np.linspace(x_new-10, x_new+10, 100)
pt.plot(xV, lam_f(xV), label=f"{f}")
pt.scatter(x_roots, [0]*len(x_roots), marker='o',  label='Approximation')     
pt.scatter(x_new, 0,  color='r', marker='v', label='Roots of the Equation')  
pt.axhline(0, color='k', linewidth=0.5)
pt.xlabel("X-Axis")
pt.ylabel("Y-Axis")
pt.title("Newton Raphson Method , RollNo : CI086, Name : Rohan N Karadigudd")
pt.legend()
pt.show()
