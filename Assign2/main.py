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

