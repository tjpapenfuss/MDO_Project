import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
#from simulated_annealing import simulated_annealing
myopts = {
        'schedule'     : 'boltzmann',   # Non-default value.
        'maxfev'       : None,  # Default, formerly `maxeval`.
        'maxiter'      : 500,   # Non-default value.
        'maxaccept'    : None,  # Default value.
        'ftol'         : 1e-6,  # Default, formerly `feps`.
        'T0'           : None,  # Default value.
        'Tf'           : 1e-12, # Default value.
        'boltzmann'    : 1.0,   # Default value.
        'learn_rate'   : 0.5,   # Default value.
        'quench'       : 1.0,   # Default value.
        'm'            : 1.0,   # Default value.
        'n'            : 1.0,   # Default value.
        'lower'        : 0,   # Non-default value.
        'upper'        : 1,   # Non-default value.
        'dwell'        : 250,   # Non-default value.
        'disp'         : True   # Default value.
        }
# ------------------------------------------------------------------------------------------------------------------ #
# Objective function
# ------------------------------------------------------------------------------------------------------------------ #
def objective_function(experiment_tuple):
    density = experiment_tuple[0]
    area = experiment_tuple[1]
    return density * area

# ------------------------------------------------------------------------------------------------------------------ #
# Square functions
# ------------------------------------------------------------------------------------------------------------------ #
def max_displacement_square(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (d/2)

def area_square(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (d**2 - (d-2*t)**2)

def inertia_square(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return ((1/12) * (d**4 - (d-(2*t))**4))

# ------------------------------------------------------------------------------------------------------------------ #
# Circle functions
# ------------------------------------------------------------------------------------------------------------------ #
def max_displacement_circle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (d/2)

def area_circle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return ((np.pi/4) * (d**2 - (d-2*t)**2))

def inertia_circle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (((np.pi/64) * (d**4 - (d-2*t)**4)))

# ------------------------------------------------------------------------------------------------------------------ #
# Triangle functions
# ------------------------------------------------------------------------------------------------------------------ #
def max_displacement_triangle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (1-(1/(np.sqrt(3)*2))) * d
def area_triangle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return ((np.sqrt(3)/4) * (d**2 - (d-((np.sqrt(3)*2)*t))**2))

def inertia_triangle(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (((np.sqrt(3)/96) * (d**4 - (d-((np.sqrt(3)*2)*t))**4)))

# ------------------------------------------------------------------------------------------------------------------ #
# I-beam functions
# ------------------------------------------------------------------------------------------------------------------ #
def max_displacement_beam(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (d/2)

def area_beam(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (3*d*t - 2*(t**2))

def inertia_beam(experiment_tuple):
    d = experiment_tuple[0]
    t = experiment_tuple[1]
    return (t/12) * ((d-2*t)**3 + (2*d*(t**2)) + ((6*d)*(d-t)**2))


# ------------------------------------------------------------------------------------------------------------------ #
# Constraints
# ------------------------------------------------------------------------------------------------------------------ #
def max_bending_stress(experiment_tuple):
    y_s = experiment_tuple[0] # Max displacement
    I_s = experiment_tuple[1] # Moment of inertia
    S_m = experiment_tuple[2] # Material yield stress
    P = 1   #Units kN
    l = 0.3 #Units m
    return ((P*l*y_s) / (0.9 * I_s * S_m)) - 1

def max_tip_deflection(experiment_tuple):
    E_m = experiment_tuple[0] # Material Young's modulus
    I_s = experiment_tuple[1] # Moment of inertia
    P = 1   #Units kN
    l = 0.3 #Units m
    return ((P*(l**3)) / (1000*0.009*E_m*I_s)) - 1 # THIS IS FUNKY!!

# Pure penalty function
# objective function + p1(max_bending_fn^2 + max_tip_fn^2)
# Non-smooth penalty function
# objective function + p2(max(0, max_bending)^2 + max(0, max_tip)^2 )
def penalty_fn(guess, *params):
    p2 = 1000000000 # Penalty parameter
    d, t = guess
    #print(params[1])
    rho_material, area_material, bending_tuple, tip_tuple, shape = params
    objective_function_tuple = (rho_material, area_material)
    if(shape == 0):
        return objective_function(objective_function_tuple) + \
                p2*(max(0,max_bending_stress(bending_tuple))**2 + \
                    max(0,max_tip_deflection(tip_tuple))**2 + \
                    max(0, 0.002 - d)**2 + \
                    max(0, d-0.3)**2 + \
                    max(0, d/2-(t))**2 +\
                    max(0, 0.001 - t)**2)
    else:
        return objective_function(objective_function_tuple) + \
                p2*(max(0,max_bending_stress(bending_tuple))**2 + \
                    max(0,max_tip_deflection(tip_tuple))**2 + \
                    max(0, 0.002 - d)**2 + \
                    max(0, d-0.3)**2 + \
                    max(0, (d/(np.sqrt(3)*2))-(t))**2 +\
                    max(0, 0.001 - t)**2)
    
E_material = (200,75,120)
yield_stress_material = (300,200,800)
rho_material = (7600,2700,4400)

inital_guess = (0.3, 0.15)
params = (rho_material[0], area_square(inital_guess), 
            (max_displacement_square(inital_guess), inertia_square(inital_guess), yield_stress_material[0]),
            (E_material[0], inertia_square(inital_guess)))
output = objective_function((rho_material[0],area_square(inital_guess)))
#print(params[1])
#output2 = penalty_fn(inital_guess, params)

#print(output, output2, max_displacement_square(inital_guess), area_square(inital_guess), inertia_beam(inital_guess))

b_s = max_bending_stress((max_displacement_square(inital_guess), inertia_square(inital_guess), yield_stress_material[0]))
t_d = max_tip_deflection((E_material[0], inertia_square(inital_guess)))
print(b_s, t_d)

# Define bounds
bound_d = (0.002,0.3)
bound_t = (0.001,0.15)

bnds = (bound_d, bound_t)

cons = ({'type': 'ineq', 'fun': lambda x:  x[0] / (x[1]*0.5)})

# Minimize objective function
# result = minimize(obj_fun, experiment_tuple, method='SLSQP', bounds=bnds)#, constraints=cons)
# print(result)
x0 = np.array([0.3, 0.11])     # Initial guess.

df = pd.read_csv("output.csv")

# Material: Steel, Shape: Square
params = (rho_material[0], area_square(inital_guess), 
            (max_displacement_square(inital_guess), inertia_square(inital_guess), yield_stress_material[0]),
            (E_material[0], inertia_square(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'Square','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: Square
params = (rho_material[1], area_square(inital_guess), 
            (max_displacement_square(inital_guess), inertia_square(inital_guess), yield_stress_material[1]),
            (E_material[1], inertia_square(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'Square','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: Square
params = (rho_material[2], area_square(inital_guess), 
            (max_displacement_square(inital_guess), inertia_square(inital_guess), yield_stress_material[2]),
            (E_material[2], inertia_square(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'Square','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# ------- Circle ------ #

# Material: Steel, Shape: circle
params = (rho_material[0], area_circle(inital_guess), 
            (max_displacement_circle(inital_guess), inertia_circle(inital_guess), yield_stress_material[0]),
            (E_material[0], inertia_circle(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'circle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: circle
params = (rho_material[1], area_circle(inital_guess), 
            (max_displacement_circle(inital_guess), inertia_circle(inital_guess), yield_stress_material[1]),
            (E_material[1], inertia_circle(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'circle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: circle
params = (rho_material[2], area_circle(inital_guess), 
            (max_displacement_circle(inital_guess), inertia_circle(inital_guess), yield_stress_material[2]),
            (E_material[2], inertia_circle(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'circle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# ------- Triangle ------ #

# Material: Steel, Shape: Triangle
params = (rho_material[0], area_triangle(inital_guess), 
            (max_displacement_triangle(inital_guess), inertia_triangle(inital_guess), yield_stress_material[0]),
            (E_material[0], inertia_triangle(inital_guess)), 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'triangle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: triangle
params = (rho_material[1], area_triangle(inital_guess), 
            (max_displacement_triangle(inital_guess), inertia_triangle(inital_guess), yield_stress_material[1]),
            (E_material[1], inertia_triangle(inital_guess)), 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'triangle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: triangle
params = (rho_material[2], area_triangle(inital_guess), 
            (max_displacement_triangle(inital_guess), inertia_triangle(inital_guess), yield_stress_material[2]),
            (E_material[2], inertia_triangle(inital_guess)), 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'triangle','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# ------- I - beam ------ #

# Material: Steel, Shape: beam
params = (rho_material[0], area_beam(inital_guess), 
            (max_displacement_beam(inital_guess), inertia_beam(inital_guess), yield_stress_material[0]),
            (E_material[0], inertia_beam(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'beam','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: beam
params = (rho_material[1], area_beam(inital_guess), 
            (max_displacement_beam(inital_guess), inertia_beam(inital_guess), yield_stress_material[1]),
            (E_material[1], inertia_beam(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'beam','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: beam
params = (rho_material[2], area_beam(inital_guess), 
            (max_displacement_beam(inital_guess), inertia_beam(inital_guess), yield_stress_material[2]),
            (E_material[2], inertia_beam(inital_guess)), 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'beam','minimum':res["fun"]}
df.loc[len(df)] = new_row
print(res)

df.to_csv("final_output.csv")