import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulated_annealing import simulated_annealing

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
    return (P*l*y_s) / (0.9 * I_s * S_m)

def max_tip_deflection(experiment_tuple):
    E_m = experiment_tuple[0] # Material Young's modulus
    I_s = experiment_tuple[1] # Moment of inertia
    P = 1   #Units kN
    l = 0.3 #Units m
    return (P*(l**3)) / (0.9*E_m*I_s) # THIS IS FUNKY!!

E_material = (200,75,120)
yield_stress_material = (300,200,800)
rho_material = (7600,2700,4400)

inital_guess = (0.3, 0.15)

output = objective_function((rho_material[0],area_square(inital_guess)))
print(output, max_displacement_square(inital_guess), area_square(inital_guess), inertia_beam(inital_guess))

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
