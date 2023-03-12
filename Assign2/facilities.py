## This Facility design assumes an 7-stage compression w/ 7 condensors to deliver CO2 from X-conditions in the pipeline.py to the supercritical point for injection. This section of code will calcuate the energy required at each stage, the emissions generated at each stage, and the anticipated cost at each stage.

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##import all needed modules##
import variables as v
import numpy as np
import pandas as pd

print ("import complete")
print()

##compressor function ------------------------------------------------------------------------------------#

def work_comp(p_in,p_out,m_dot,T_in):
    m = m_dot*3600*24*1 #convert to total mass on daily basis at 100% runtime
    mtot = m*365
    print ("annual co2 entering plant ", mtot, " kg CO2 per year")
    n_mole = v.n_mole
    M_co2 = v.M_co2/1000
    n = v.n_poly
    R = v.CO2_IDEAL_GAS_CONST
    Ti = T_in #convert to Kelvin
    pi = p_in
    po = p_out
    
    print()
    
    # density of CO2 at 1; m3/kg
    rho_in = n_mole*p_in*M_co2/(R*Ti) 
    print ("rhoin ", rho_in)
    
    #volumetric flowrate at inlet of compressor, m^3/s
    vi_dot = m_dot / rho_in 
    print ("vi_dot ", vi_dot)
    
    #volumetric flowrate at outlet of compressor, m^3/s
    vo_dot = (pi*vi_dot**n/po)**(1/n) 
    print ("vo_dot ", vo_dot)
    
    #Temperature at the outlet of the compressor, K
    To = (po/pi)**((n-1)/n)*Ti   
    #print ("Temp at outlet of W12 is ", To," K")
    
    ##Work done flux by compressor, in kW
    Wd = -1*(pi*vi_dot**n*(vo_dot**(1-n)-vi_dot**(1-n))/(1-n)) 
    #print ("Wd done flux by compressor is", Wd, " kW")
    
    # Emissions ----------------------- #
    CO2_emit_coeff = v.CO2_emit/293.07*0.453 #convert to kg/kWh
    CO2_emit_d = CO2_emit_coeff*Wd*24*365 #total annual kg emissions in kg
    #print ("Wd emits approximately", CO2_emit_d, " kg CO2 per year")
    
    # Capital Costs ---------------------- #
    #assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table
    comp_capex = v.comp_capex #$/(kW)
    comp_capex_d = Wd*comp_capex
    #print ("Wd capital costs approximately $", comp_capex_d)
    
    # Operating Costs (Fuel Costs) for now -------------- #
    NG_price = v.NG_price/293.07 #$/(kW)
    comp_om_cost = v.comp_om_cost
    comp_om_d = Wd*24*365*comp_om_cost #annual non-fuel o&m costs
    comp_opex_d = Wd*NG_price*365 + comp_om_d
    #print ("Wd O&M and fuel costs approximately $", comp_opex_d, " per year")
    print()
    
    ##The outputs of this module are:

    #press_out
    #temp_out
    #Wd
    #co2_emit
    #comp_capex
    #comp_opex
    
    return po, To, Wd, CO2_emit_d, comp_capex_d, comp_om_d, comp_opex_d, m_dot, mtot


##heat exchanger function ------------------------------------------------------------------------------------#

def heat_hx(pi,T_in,T_out,m_dot):
    Ti = T_in 
    To = T_out
    cp = v.cp_CO2 #kJ/(kgK)
    po = pi
    
    print()
    #change in enthalpy across Hx (kJ/kg)
    h_io = cp*(To-Ti)
    
    # Heat required
    Qio = m_dot*(h_io) #in kJ/s or kW
    Q_cool = -Qio #the amount of heat gained by the cooling fluid
    #print ("Q done onto HX is", Qio, " kW")
    
    # Emissions ----------------------- #
    unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW/s)
    TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

    Elec_HX = unit_ann_elec*Q_cool #total elec used by HX in kWh

    CO2_emit_hx = Elec_HX*TX_grid/1000*24*365 #total emissions from HX annually, kg
    #print ("HX emits approximately", CO2_emit_hx, " kg CO2 per year")
    
    # Capital Costs ------------------- #
    #assumes an example chiller from paper
    #note 1TR = 3.51865kW

    hx_capex = v.hx_capex
    hx_capex_d = hx_capex*Q_cool #$ capital cost

    #print ("HX capital costs approximately $", hx_capex_d)

    # Operating Costs ------------------- #
    #Electrical costs
    hx_elec = v.hx_elec
    hx_elec_price = v.hx_elec_price
    hx_opexelec_d = hx_elec*Q_cool*hx_elec_price #elec cost in $ per year

    #Refrigerant consumed per year
    hx_refrig = v.hx_refrig
    hx_refrig_price = v.hx_refrig_price
    hx_opref_d = hx_refrig*Q_cool*hx_refrig_price #refrigcost in $ per year

    #Water costs
    hx_water = v.hx_water
    hx_water_price = v.hx_water_price
    hx_opwat_d = hx_water*Q_cool*hx_water_price

    #Total OPEX
    hx_opex_d = hx_opexelec_d+hx_opref_d+hx_opwat_d

    #print ("HX operating costs approximately $", hx_opex_d, " per year")
    print()
    
    ##The outputs of this module are:

    #press_out
    #temp_out
    #Wd
    #co2_emit
    #comp_capex
    #comp_opex
    
    return po, To, Qio, Q_cool, CO2_emit_hx, hx_capex_d, hx_opexelec_d, hx_opref_d, hx_opwat_d, hx_opex_d



##emissions generated function ------------------------------------------------------------------------------------#

def co2_gen(CO2_emit_12,CO2_emit_23,CO2_emit_34,CO2_emit_45,CO2_emit_56,CO2_emit_67,CO2_emit_78,CO2_emit_910,CO2_emit_1011,CO2_emit_1112,CO2_emit_1213,CO2_emit_1314,CO2_emit_1415):
    
    tot_co2_gen = CO2_emit_12 + CO2_emit_23 + CO2_emit_34 + CO2_emit_45 + CO2_emit_56 + CO2_emit_67 + CO2_emit_78 + CO2_emit_910 + CO2_emit_1011 + CO2_emit_1112 + CO2_emit_1213 + CO2_emit_1314 + CO2_emit_1415 #annual co2 generated with the process (kg)
    
    print("CO2 Generated ", tot_co2_gen, " kg")
    print("CO2 Generated ", tot_co2_gen/1000/1000, " Million metric T")
    
    return tot_co2_gen


##Tot CAPEX Facilities ------------------------------------------------------------------------------------#

def fac_capex(comp_capex_12,comp_capex_34,comp_capex_56,comp_capex_78,comp_capex_910,comp_capex_1112,comp_capex_1314,hx_capex_23,hx_capex_45,hx_capex_67,hx_capex_89,hx_capex_1011,hx_capex_1213,hx_capex_1415):
    cost_comp_capex = comp_capex_12 + comp_capex_34 + comp_capex_56 + comp_capex_78 + comp_capex_910 + comp_capex_1112 + comp_capex_1314 #capital cost for compressors ($
    cost_hx_capex = hx_capex_23 + hx_capex_45 + hx_capex_67 + hx_capex_89 + hx_capex_1011 + hx_capex_1213 + hx_capex_1415 #capital cost for hx ($)
    cost_fac_capex = cost_comp_capex + cost_hx_capex #Total fac cost 
    
    return cost_comp_capex, cost_hx_capex, cost_fac_capex

##Tot Opex Facilities ------------------------------------------------------------------------------------#

def fac_opex (comp_opex_12,comp_opex_34,comp_opex_56,comp_opex_78,comp_opex_910,comp_opex_1112,comp_opex_1314,hx_opex_23,hx_opex_45,hx_opex_67,hx_opex_89,hx_opex_1011,hx_opex_1213,hx_opex_1415):
    cost_comp_opex = comp_opex_12 + comp_opex_34 + comp_opex_56 + comp_opex_78 + comp_opex_910 + comp_opex_1112 + comp_opex_1314 #operating cost for compressors ($)
    cost_hx_opex = hx_opex_23 + hx_opex_45 + hx_opex_67 + hx_opex_89 + hx_opex_1011 + hx_opex_1213 + hx_opex_1415 #operating cost for hx ($)
    cost_fac_opex = cost_comp_opex + cost_hx_opex
    
    return cost_comp_opex, cost_hx_opex, cost_fac_opex
