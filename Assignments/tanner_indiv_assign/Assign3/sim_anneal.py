from scipy import optimize
import numpy as np

def f(d,t,s,m):
    "Objective function"
    rho_material = [7600,2700,4400]
    if(m < 1):
        rho = rho_material[0]
    elif(m < 2):
        rho = rho_material[1]
    else:
        rho = rho_material[2]
    
    if(s < 1):
        mass = rho * (d**2 - (d-2*t)**2)
    elif(s < 2):
        mass = rho * ((np.pi/4) * (d**2 - (d-2*t)**2))
    elif(s < 3):
        mass = rho * ((np.sqrt(3)/4) * (d**2 - (d-((np.sqrt(3)*2)*t))**2))
    else:
        mass = rho * (3*d*t - 2*(t**2))

    return 1 # something here

def constraint1(d,t,s,m):
    "Constraint function"
    return 0.3 - d

def main():
    "Main function"
    # Initial guess
    x0 = np.array([0.1, 0.1, 0.1, 0.1])
    # Bounds
    bnds = ((0.01, 0.3), (0.01, 0.3), (0, 3), (0, 4))
    # Run the optimization
    res = optimize.minimize(f, x0, method='SLSQP', bounds=bnds)
    # Print the results
    print(res)

if __name__ == '__main__':
    main()