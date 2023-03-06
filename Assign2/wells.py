from numpy import *

#import variables as v


# wells
rw =                    0 # Wellbore Radius Inner radius of injection well tubing measured in ft
n_wells =               0 # Wells,Number of wells,Number of injection wells in system
rel_rough =             0 # Wells,Relative roughness,Relative roughness of wellbore,,,0.0006,diml
res_depth =             5500 # Wells,Well total depth,Average depth of wells to be drilled,5000,6000,5500,ft
rho_CO2sc =             37.5 # Wells,CO2 fluid density at Super Critcal, lb/ft3 
avg_vol =               6 # Wells, Average Volocity of CO2 Coming down the pipe, ft/s
Pipe_id =               0.5 # Wells, Inside Diameter of drill pipe, ft
mu_CO2sc =              0.000458304 # Wells, Viscosity of CO2 at SC, lbs/ft*s
k =                     0.000492 # Wells, Pipe Roughness, ft
g =                     32.147 # Wells, Gravitaional Constant, ft/s^2
Pwh =                   1070 # Wells, 

#Step 1 is to calculate the Reynolds Number Re in Centipoise
        
        
        #for the actual model we will need to call the avg_vol from the facilities module


Re = ((rho_CO2sc*avg_vol*Pipe_id)/mu_CO2sc)
#Note that the Re is diml
print("The Value of the Reynolds Number is: " + str(Re))
#print(Re)

#Step 2 is to calculate the Fanning friction factor (function of Reynolds number)
fann = 0.0055*(1+(2*10**4*(k/Pipe_id)+(10**6/Re))**(1/3))
#Note that the fann is diml
print("The Value of the Fanning Friction factor is: " + str(fann))

#Step 3 is to calculate the pressure loss due to friction effects
Delta_Pf = (((2*fann*rho_CO2sc*(avg_vol**2)*res_depth)/(g*Pipe_id))/144)
#Note that Delta_Pf units are PSIA (absolute PSI)
#Note that the equation is divided by 144 to conver to PSI
print("The Value of Delta_Pf is: " + str(Delta_Pf))

#Step 4 is to calculate the wellbore injection pressure
        #for the actual model we will need to call the Pwh from the facilities module
p_wf_t = (Pwh-Delta_Pf+((rho_CO2sc*res_depth)/144))
print("The Value of p_wf_t is: " + str(p_wf_t))

#Step 5 is to pass p_wf_t to the subsurface.py module