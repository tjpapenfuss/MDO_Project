##############################################################################################
# This module will perform calculations for pipelines.
# Inputs: mass_dot, press_source, p_d, p_l, n_pc (all units are SI (ft, lbsf, lbsm, PSI))
# Intermediate variables: Reynolds number, fanning factor, velocity (of CO2 in pipe), pressure delta (in Pa), viscosity in cP
# Outputs: press_i (kPa), vel_i (m/s), temp_i (K), cost_pipe ($)
##############################################################################################

import math
import variables

# function definition
def pipes_out(mass_dot, press_source, p_d, p_l):#, n_pc):

    #kg per mol
    mol_mass_co2 = variables.M_co2 / 1000

    #pressure to pascals 
    press = press_source * 6894.76

    #temp at source​
    temp = variables.temp_source

    #rho_new is in kg/m3
    rho_new = mol_mass_co2 * press / (8.3145 * temp)
    
    #this converts rho_new to lb/ft3
    #rho_new = rho_new / 16.018

    #rho_new = rho_new * 144

    ##This section defines the inputs to be used by the pipeline calculations
    ##These values need to come from the optimizer or initial design vector

    ##This section defines the parameters that will be used
    #gravity m/s^2
    g = 9.81

    #fanning friction factor​, will be calculated later
    fanning = 0

    #density imported (lb/ft^3)​
#    rho = variables.rho_CO2sc

#    rho = 1.1664
    #density used (kg/m^3)
    #rho = rho_import * 16.018463

    #This section will calculate the viscosity of the fluid based on pressure and temperature.
    mu_o = variables.mu_o
    sutherland = variables.sutherland_c
    t_o = variables.temp_o_c02

    #viscosity of C02 in centipoise
    mu_C02 = mu_o * ((0.555 * t_o + sutherland) / (0.555 * (temp * 1.8)+sutherland)) * (temp * 1.8 / t_o) ** (3/2)

    #Convert pipe dimensions to meters.  (p_d is converted to feet in main.py before calling pipelines.py)
    p_d = p_d / 3.281
    p_l = p_l / 3.281 


    #absolute roughness imported (in)​
    k = (variables.rel_rough / 39.37)
    

    #price per foot​
    cost_per_foot = variables.cost_per_foot
    #cost_per_meter = cost_per_foot * .3048

    #cost for each connection​
    cost_per_pc = variables.cost_per_pc

    ##This section performs calculations based on parameters and inputs
    #This will compute velocity in m/s
    vel = (mass_dot) / (rho_new * math.pi * ((p_d / (2)) ** 2)) 

    #reynolds_number = 1488*rho_new*vel*(p_d) / mu_C02
    reynolds_number = rho_new*vel*(p_d) / (mu_C02/100)

    fanning = (1/(-4*math.log10   (0.2698*(k/p_d)-5.0452/      \
                reynolds_number*math.log10(.3539*(k/p_d)       \
                **1.1098+5.8506/(reynolds_number)**0.8981)    )))**2
    
    #fanning = (.0055*(1+(2*10**4*k/p_d+10**6/reynolds_number)**(1/3)))
    
    #this is technically: press_delta = 2*fanning*rho*vel_avg*pipe_length / (g*pipe_diameter)
    #however, where do we average the velocities?
    press_delta = 2*fanning*rho_new*vel**2*p_l / (g*p_d)
    
    press_i = (press - press_delta) / 1000

    vel_i = vel #assumes no velocity lost or added

    temp_i = temp  #this assumes no heat gained or lost in the system

    cost_pipe = p_l * cost_per_foot + cost_per_pc

    return press_i, vel_i, temp_i




pipes_out(250, 1500, .666667, 55000)