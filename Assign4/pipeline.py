##############################################################################################
# This module will perform calculations for pipelines.
# Inputs: mass_dot, press_source, p_d, p_l, n_pc (all units are SI (ft, lbsf, lbsm, PSI))
# Intermediate variables: Reynolds number, fanning factor, velocity (of CO2 in pipe), pressure delta (in Pa), viscosity in cP
# Outputs: press_i (kPa), vel_i (m/s), temp_i (K), CO2_emit_d, comp_capex_d, comp_opex_d
##############################################################################################

import math
import variables

# function definition
def pipes_out(mass_dot, press_source, p_d, p_l, temp_facilities):#, n_pc):

    #kg per mol
    mol_mass_co2 = variables.M_co2 / 1000

    #convert pressure to pascals 
    press = press_source * 1000
    #press = press_source * 6894.76

    #temp at source​
    temp = temp_facilities

    #rho_new is in kg/m3
    rho_new = mol_mass_co2 * press / (8.3145 * temp )
    
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
    k = (variables.rel_rough)

    ##This section performs calculations based on parameters and inputs
    #This will compute velocity in m/s
    vel = (mass_dot) / (rho_new * math.pi * ((p_d / (2)) ** 2))

    #reynolds_number = 1488*rho_new*vel*(p_d) / mu_C02
    reynolds_number = rho_new*vel*(p_d) / (mu_C02/1000)

    fanning = (1/(-4*math.log10   (0.2698*(k/p_d)-5.0452/      \
                reynolds_number*math.log10(.3539*(k/p_d)       \
                **1.1098+5.8506/(reynolds_number)**0.8981)    )))**2

    #this is technically: press_delta = 2*fanning*rho*vel_avg*pipe_length / (g*pipe_diameter)
    #however, where do we average the velocities?

    #Calculate pressure delta (pascals)
    press_delta = 2*fanning*rho_new*vel**2*p_l / (p_d)

    #compute the new facilities input pressure
    press_i = (press - press_delta) 

    if press_i < 350000:
        #if you're here then the pressure exiting the pipe is too low and requires a compressor before entering the facilities
        #equations in this section require pressures to be in kPa
        n = variables.n_poly
        Ti = temp #convert to Kelvin
       
        #pi = press / 1000
        if press_i < 0:
            pi = 1
        else:
            pi = press_i / 1000
        po = 350 
        #po = (350000-(press - press_delta)) / 1000 #figure out the work to reach the standardized output to facilities module (350 kPa)
        
        #Convert rho_new to work with kPa
        rho_new = rho_new / 1000

        #volumetric flowrate at inlet of compressor, m^3/s
        vol = mass_dot / rho_new 
        
        #volumetric flowrate at outlet of compressor, m^3/s
        vo_dot = (pi*vol**n/po)**(1/n) 

        #Temperature at the outlet of the compressor, K
        To = (po/pi)**((n-1)/n)*Ti   
        #print ("Temp at outlet of W12 is ", To," K")
        
        ##Work done flux by compressor, in kW
        Wd = -1*(pi*vol**n*(vo_dot**(1-n)-vol**(1-n))/(1-n)) 
        #print ("Wd done flux by compressor is", Wd, " kW")
        
        # Emissions ----------------------- #
        CO2_emit_coeff = variables.CO2_emit/293.07*0.453 #convert to kg/kWh
        CO2_emit_d = CO2_emit_coeff*Wd*24*365 #total annual kg emissions in kg
        #print ("Wd emits approximately", CO2_emit_d, " kg CO2 per year")
        
        # Capital Costs ---------------------- #
        #assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table
        comp_capex = variables.comp_capex #$/(kW)
        comp_capex_d = Wd*comp_capex
        #print ("Wd capital costs approximately $", comp_capex_d)
        
        # Operating Costs (Fuel Costs) for now -------------- #
        NG_price = variables.NG_price/293.07 #$/(kW)
        comp_om_cost = variables.comp_om_cost
        comp_om_d = Wd*24*365*comp_om_cost #annual non-fuel o&m costs
        comp_opex_d = Wd*NG_price*365 + comp_om_d
        #print ("Wd O&M and fuel costs approximately $", comp_opex_d, " per year")
        temp_i = To
        press_i = po
    else:
        temp_i = temp  #this assumes no heat gained or lost in the system
        CO2_emit_d = 0
        comp_capex_d = 0
        comp_opex_d = 0    
        vol = 0
        vo_dot = 0
        To = 0
        Wd = 0    
        #convert back to kPa
        press_i = press_i / 1000 
    vel_i = vel #assumes no velocity lost or added       
    #Used for testing
    # x='foo'
    return press_i, vel_i, temp_i, CO2_emit_d, comp_capex_d, comp_opex_d

#used for testing
pipes_out(15, 150, 12/12, 55000,293)