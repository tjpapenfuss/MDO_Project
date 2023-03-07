import math
import variables

#import nlopt
#from numpy import *

# function definition
def press_delta(mass_dot, press_source):


    ##This section defines the inputs to be used by the pipeline calculations
    ##These values need to come from the optimizer or initial design vector
    #pipe parameter​
    pipe_diameter = variables.p_d

    #length of the pipe
    pipe_length = variables.p_l

    #number of sources​
    num_pc = variables.n_pc

    #mass flow rate ​
    mass_dot = variables.m_dot

    ##This section defines the parameters that will be used
    #gravity (lbm * ft)/(lbf *s^2)​

    g = 32.174

    #fanning friction factor​, will be calculated later
    fanning = 0

    #density (lb/ft^3)​
    #where do we start as a baseline?
    rho = variables.rho_CO2sc

    #viscosity (lb/(ft*s))​
    #assuming viscosity of water or should this be CO2 gas?
    u_w = variables.visc_CO2SC

    #absolute roughness (in)​
    #what kind of material are we using and what do we assume for "roughness"
    k = variables.abs_rough

    #velocity​
    #vel = 0 

    #price per foot​
    ##ask nick
    cost_per_foot = variables.cost_per_foot

    #cost for each connection​
    ##ask nick
    cost_per_pc = variables.cost_per_pc

    #pressure at source​
    press_source = variables.press_source

    #temp at source​
    temp_source = variables.temp_source

    ##This section performs calculations based on parameters and inputs
    vel = mass_dot / (rho * math.pi * ((pipe_diameter / 2) ** 2))

    reynolds_number = 1488*rho*vel*pipe_diameter / u_w

    fanning = 1/((-4*math.log10(0.2698*(k/pipe_diameter)-5.0452/reynolds_number*math.log10(.3539*(k/pipe_diameter)**1.1098+5.8506/(reynolds_number)**0.8981)))**2)

    #this is technically: press_delta = 2*fanning*rho*vel_avg*pipe_length / (g*pipe_diameter)
    #however, what are we averaging velocities between and what is causing the velocity loss?
    press_delta = 2*fanning*rho*vel*pipe_length / (g*pipe_diameter)

    press_i = press_source - press_delta

    vel_i = vel #assumes no velocity lost or added

    temp_i = temp_source  #this assumes no heat gained or lost in the system

    cost_pipe = pipe_length * cost_per_foot + cost_per_pc * num_pc

    ##The outputs of this module are:

    #press_i​
    #variables.press_source = press_i

    #temp_i​  
    #variables.temp_source = temp_i

    #vel_i​
    #variables.vel_ = vel_i

    #cost_pipe
    #variables.cost = cost_pipe
    result = press_delta
    return result
