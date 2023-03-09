# ------------------------------------------------------------------------------------------------------------------ #
# 16.888 MDO; Multidisciplinary Design Optimization. 
# Project: Design and optimization of CO2 injection. 
# Authors: John Beilstein, Warren Anderson, Brooke DiMartino, Stephen Tainter, Tanner Papenfuss
# Team name: Terra Sparkling
# ------------------------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------------------------ #
# Import all necessary packages
# ------------------------------------------------------------------------------------------------------------------ #
from numpy import *
import variables
import pipeline as pipes
import finance as finance
import subsurface as sub

# ------------------------------------------------------------------------------------------------------------------ #
# Import the module files. EX. import subsurface as sub
# ------------------------------------------------------------------------------------------------------------------ #
import wells as wells

print("The value of CO2 ideal gas constant is: " + str(variables.CO2_IDEAL_GAS_CONST))

# Chaining together the modules below. 

# ------------------------------------------------------------------------------------------------------------------ #
# Module name: Wells
# Required inputs: FILL IN
# Outputs: FILL IN
# ------------------------------------------------------------------------------------------------------------------ #
print("Wells res depth: ", wells.res_depth)

# ------------------------------------------------------------------------------------------------------------------ #
# Module name: 
# Required inputs:
# Outputs: 
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Module name: Pipeline
# Required inputs:  m_dot, press_source, p_d, p_l, n_pc
# Outputs: p_i, t_i, v_i
# ------------------------------------------------------------------------------------------------------------------ #
pipes_press_out, pipes_vel_out, pipes_temp_out, pipes_cost_out = pipes.pipes_out(variables.m_dot, 
                                                                variables.press_source, variables.p_d, 
                                                                variables.p_l, variables.n_pc)
print("Pipes pressure output: ", pipes_press_out)
print("Pipes velocity output: ", pipes_vel_out)
print("Pipes temperature output: ", pipes_temp_out)
print("Pipes cost output: ", pipes_cost_out)


# ------------------------------------------------------------------------------------------------------------------ #
# Module name: Subsurface
# Required inputs: p_wf_t
# Outputs: q_inj
# ------------------------------------------------------------------------------------------------------------------ #
q_inj = sub.subsurface(10)
print("The Value of q_inj injection volume is: " + str(q_inj))


#Module name: Finance
#Required inputs: p_d, p_l, q_inj, n_wells
#Outputs: NPV
q_inj=50                #q_inj should be an output of a subsurface function, so delete this once it's available
revenue = finance.revenue_func(q_inj, variables.n_wells) 
CAPEX_total, CAPEX_pipeline, CAPEX_site = finance.CAPEX_func(variables.p_l, variables.p_d, variables.n_wells)
OPEX_total = finance.OPEX_func(CAPEX_pipeline, variables.n_wells)
NPV = finance.NPV_func(CAPEX_total, revenue, CAPEX_site, OPEX_total)