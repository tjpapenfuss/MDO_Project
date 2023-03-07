from numpy import *

import variables as v

#Subsurface
p_wf_t =                2365.568 # Subsurface, wellbore injection pressure, PSI
re =                    500 # Subsurface, Formaiton radius zone, ft


#Step 1 is to calculate the daily injection rate in scf/day
q_inj = ((0.703*v.perm*v.h_res*((p_wf_t**2)-(v.p_res**2)))/(v.t_res*v.visc_CO2SC*v.Z_CO2SC(log(re/v.rw)-.075+v.skin)))

            #There is a proble with my natural log function??


print("The Value of q_inj is: " + str(q_inj))

#Do we need an extra step to include the number of wells???