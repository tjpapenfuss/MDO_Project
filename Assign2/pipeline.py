##############################################################################################
# This module 

##############################################################################################

import math
import variables



# function definition
def pipes_out(mass_dot, press_source, p_d, p_l, n_pc):


    ##This section defines the inputs to be used by the pipeline calculations
    ##These values need to come from the optimizer or initial design vector

    ##This section defines the parameters that will be used
    #gravity (lbm * ft)/(lbf *s^2)​

    g = 32.174

    #fanning friction factor​, will be calculated later
    fanning = 0

    #density (lb/ft^3)​
    rho = variables.rho_CO2sc

    #viscosity (lb/(ft*s))​
    u_w = variables.visc_CO2SC

    #absolute roughness (in)​
    k = variables.abs_rough

    #price per foot​
    cost_per_foot = variables.cost_per_foot

    #cost for each connection​
    cost_per_pc = variables.cost_per_pc

    #temp at source​
    temp_source = variables.temp_source

    ##This section performs calculations based on parameters and inputs
    vel = mass_dot / (rho * math.pi * ((p_d / 2) ** 2))

    reynolds_number = 1488*rho*vel*p_d / u_w

    fanning = 1/((-4*math.log10(0.2698*(k/p_d)-5.0452/         \
                reynolds_number*math.log10(.3539*(k/p_d)       \
                **1.1098+5.8506/(reynolds_number)**0.8981)))**2)

    #this is technically: press_delta = 2*fanning*rho*vel_avg*pipe_length / (g*pipe_diameter)
    #however, where do we average the velocities?
    press_delta = 2*fanning*rho*vel*p_l / (g*p_d)

    press_i = press_source - press_delta

    vel_i = vel #assumes no velocity lost or added

    temp_i = temp_source  #this assumes no heat gained or lost in the system

    cost_pipe = p_l * cost_per_foot + cost_per_pc * n_pc

    ##The outputs of this module are:

    #press_i​
    #variables.press_source = press_i

    #temp_i​  
    #variables.temp_source = temp_i

    #vel_i​
    #variables.vel_ = vel_i

    #cost_pipe
    #variables.cost = cost_pipe

    return press_i, vel_i, temp_i, cost_pipe
