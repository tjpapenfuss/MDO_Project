import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import time as t

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
    return (d**2 - (d-(2*t))**2)

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
    return ((P*(l**3)) / (1000*0.009*E_m*I_s)) - 1 


# Pure penalty function
# objective function + p1(max_bending_fn^2 + max_tip_fn^2)
# Non-smooth penalty function
# objective function + p2(max(0, max_bending)^2 + max(0, max_tip)^2 )
def penalty_fn(guess, *params):
    p2 = 1000000000 # Penalty parameter
    d, t = guess
    #print(params[1])
    rho_material, yield_stress, e_material, shape = params
    if(shape == 0):
        area_material = area_square(guess)
        max_displacement = max_displacement_square(guess)
        inertia = inertia_square(guess)
    elif(shape == 1):
        area_material = area_circle(guess)
        max_displacement = max_displacement_circle(guess)
        inertia = inertia_circle(guess)
    elif(shape == 2):
        area_material = area_triangle(guess)
        max_displacement = max_displacement_triangle(guess)
        inertia = inertia_triangle(guess)
    else:
        area_material = area_beam(guess)
        max_displacement = max_displacement_beam(guess)
        inertia = inertia_beam(guess)
    objective_function_tuple = (rho_material, area_material)
    bending_tuple = (max_displacement, inertia, yield_stress)
    tip_tuple = (e_material, inertia)
    # if(t > d/2):
    #     print(d/2 -t)
    if(shape == 2):
        return objective_function(objective_function_tuple) + \
                p2*(max(0,max_bending_stress(bending_tuple)) + \
                    max(0,max_tip_deflection(tip_tuple)) + \
                    max(0, 0.002 - d)**2 + \
                    max(0, d-0.3)**2 + \
                    max(0, ((d/(np.sqrt(3)*2))-(t))**2) +\
                    max(0, 0.001 - t)**2)
    else:
        return objective_function(objective_function_tuple) + \
                p2*(max(0,max_bending_stress(bending_tuple)) + \
                    max(0,max_tip_deflection(tip_tuple)) + \
                    max(0, 0.002 - d)**2 + \
                    max(0, d-0.3)**2 + \
                    max(0, (d/2-(t))**2) +\
                    max(0, 0.001 - t)**2)
    
E_material = (200,75,120)
yield_stress_material = (300,200,800)
rho_material = (7600,2700,4400)

# Define bounds
bound_d = (0.002,0.3)
bound_t = (0.001,0.15)

bnds = (bound_d, bound_t)

cons = ({'type': 'ineq', 'fun': lambda x:  x[0] / (x[1]*0.5)})

# Minimize objective function
# result = minimize(obj_fun, experiment_tuple, method='SLSQP', bounds=bnds)#, constraints=cons)
# print(result)

x0 = np.array([0.3, 0.15])     # Initial guess.

df = pd.read_csv("output.csv")
#df = pd.DataFrame

# Using a timer to check algo run time
starttime = t.time()
lasttime = starttime
lapnum = 1

# Material: Steel, Shape: Square
params = (rho_material[0], yield_stress_material[0], E_material[0], 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'Square','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: Square
params = (rho_material[1], yield_stress_material[1], E_material[1], 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'Square','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: Square
params = (rho_material[2], yield_stress_material[2], E_material[2], 0)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'Square','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# ------- Circle ------ #

# Material: Steel, Shape: circle
params = (rho_material[0], yield_stress_material[0], E_material[0], 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'circle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: circle
params = (rho_material[1], yield_stress_material[1], E_material[1], 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'circle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: circle
params = (rho_material[2], yield_stress_material[2], E_material[2], 1)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'circle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# ------- Triangle ------ #

# Material: Steel, Shape: Triangle
params = (rho_material[0], yield_stress_material[0], E_material[0], 2)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'triangle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: triangle
params = (rho_material[1], yield_stress_material[1], E_material[1], 2)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'triangle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: triangle
params = (rho_material[2], yield_stress_material[2], E_material[2], 2)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'triangle','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# ------- I - beam ------ #

# Material: Steel, Shape: beam
params = (rho_material[0], yield_stress_material[0], E_material[0], 3)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Steel','shape':'beam','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Aluminum, Shape: beam
params = (rho_material[1], yield_stress_material[1], E_material[1], 3)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Aluminum','shape':'beam','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

# Material: Titanium, Shape: beam
params = (rho_material[2], yield_stress_material[2], E_material[2], 3)
np.random.seed(555)   # Seeded to allow replication.
res = optimize.dual_annealing(penalty_fn, x0=x0, args=params, bounds=bnds)

new_row = {'Material':'Titanium','shape':'beam','minimum':res["fun"],'location':res['x']}
df.loc[len(df)] = new_row
print(res)

df.to_csv("final_output.csv")
final_time = round((t.time() - lasttime), 2)
print(final_time)