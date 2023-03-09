from numpy import *
import numpy as np

import variables as v

#Subsurface


#make a def subsurface here - make sure that 
def subsurface(p_wf_t):
    #variables
    p_wf_t =                2365.568 # Subsurface, wellbore injection pressure, PSI
    re =                    500 # Subsurface, Formaiton radius zone, ft
    t_res_K =               v.t_res+460
    
    #equation setup
    square_pwf = p_wf_t**2
    Re_rw = np.log(re/v.rw)
    print(Re_rw)
    res_x = (0.703*v.perm*v.h_res*((p_wf_t**2)-(v.p_res**2)))
    fluid_y = (t_res_K*v.visc_CO2SC*v.Z_CO2SC*(Re_rw-.075+v.skin))
    

    print("The Value of res_x is: " + str(res_x))
    print("The Value of fluid_y is: " + str(fluid_y))
    
    q_inj = res_x/fluid_y

    print("The Value of q_inj is: " + str(q_inj))
    return q_inj



