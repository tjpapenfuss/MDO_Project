from numpy import *
import variables as v
import math as math

#Wells
def wells(mass_dot, Pwh):

        #these are the inputs that we will need from facilities when it is ready
        #avg_vel =               6 # Wells, Average Volocity of CO2 Coming down the pipe, ft/s
        # Pwh =                   1070 # Facilities, Wellhead pressure, PSI 
        #variables
        Pipe_id =               v.rw*2 # Wells, Inside Diameter of drill pipe, ft
        mu_CO2sc =              v.visc_CO2SC*0.000672 # Wells, Viscosity of CO2 at SC, lbs/ft*s
        g =                     32.147 # Wells, Gravitaional Constant, ft/s^2
        rho =                   v.density_CO2SC
        avg_vel =               mass_dot / (rho * math.pi * ((Pipe_id / 2) ** 2))

        #Step 1 is to calculate the Reynolds Number Re in Centipoise    
        Re = ((rho*avg_vel*Pipe_id)/mu_CO2sc)
        #Note that the Re is diml
        #print("The Value of the Reynolds Number is: " + str(Re))

        #Step 2 is to calculate the Fanning friction factor (function of Reynolds number)
        fann = 0.0055*(1+(2*(10**4)*(v.rel_rough/Pipe_id)+(10**6/Re))**(1/3))
        #Note that the fann is diml
        #print("The Value of the Fanning Friction factor is: " + str(fann))

        #Step 3 is to calculate the pressure loss due to friction effects
        Delta_Pf = (((2*fann*rho*(avg_vel**2)*v.depth)/(g*Pipe_id))/144)
        #Note that Delta_Pf units are PSIA (absolute PSI)
        #Note that the equation is divided by 144 to conver to PSI
        #print("The Value of Delta_Pf is: " + str(Delta_Pf))

        #Step 4 is to calculate the wellbore injection pressure
                #for the actual model we will need to call the Pwh from the facilities module
        p_wf_t = (Pwh-Delta_Pf+((rho*v.depth)/144))
        #print("The Value of p_wf_t is: " + str(p_wf_t))

        return p_wf_t
