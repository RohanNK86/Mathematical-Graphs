import sympy as sp

x = sp.Symbol('x')
f = sp.sympify(input("Enter the Function : "))
dfx = sp.diff(f, x)
print(f"The Differentiation of f is : {dfx}")

x0 = float(input("Enter the Initial Guess : "))
xn = x0

i = 0

while(i < 20):
    fxn = f.subs(x,  xn)
    dfxn = dfx.subs(x, xn)
    if(dfxn == 0.0):
        print("NR-Method will not Work")
        break
    X_new = xn - (fxn/dfxn)
    print(f"Iteration {i+1}")
    print(f"x = : {X_new}")

    if abs(X_new - xn) < 0.00001:
        print(f"Converge after {i+1} iterations")
        print(f"Estimated root : {X_new}")
        break
    else:
        xn = X_new
        i += 1   
    
