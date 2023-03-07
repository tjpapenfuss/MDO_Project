## This Facility design assumes an 7-stage compression w/ 7 condensors to deliver CO2 from X-conditions in the pipeline.py to the supercritical point for injection. This section of code will calcuate the energy required at each stage, the emissions generated at each stage, and the anticipated cost at each stage.

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

##import all needed modules##
import variables as v
#import numpy as np
#import pandas as pd

print ("import complete")
print()

## 12 Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p1 = 50 #psi =v.pipe_press_out
m_dot = 0.1 # v.m_dot #kg/s
m = m_dot*3600*24*1 #convert to total mass on daily basis at 100% runtime
print ("annual co2 entering plant ", m*365, " kg CO2 per year")
T1 = 298 #kelvin =v.T1+273
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p2 = 100 #psi =v.p_ou_12_comp 

rho1 = n_mole*p1*M_co2/(v.CO2_IDEAL_GAS_CONST*T1) # density of CO2 at 1; m3/kg

print ("rho1 ", rho1)

v1_dot = m_dot / rho1           #volumetric flowrate at inlet of compressor, m^3/s

print ("v1_dot ", v1_dot)

v2_dot = (p1*v1_dot**n/p2)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v2_dot ", v2_dot)

T2 = (p2/p1)**((n-1)/n)*T1 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W12 is ", T2," K")

W_12 = -1*(p1*v1_dot**n*(v2_dot**(1-n)-v1_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W12 done flux by compressor is", W_12, " kW")

# Emissions ----------------------- #
CO2_emit = v.CO2_emit/293.07*0.453 #convert to kg/kWh
CO2_emit_12 = CO2_emit*W_12*24*365 #total annual kg emissions in kg

print ("W12 emits approximately", CO2_emit_12, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex = v.comp_capex #$/(kW)
comp_capex_12 = W_12*comp_capex

print ("W12 capital costs approximately $", comp_capex_12)

# Operating Costs (Fuel Costs) for now -------------- #
NG_price = v.NG_price/293.07 #$/(kW)
comp_om_12 = W_12*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_12 = W_12*NG_price*365 + comp_om_12

print ("W12 fuel costs approximately $", comp_opex_12, " per year")
print()










## 23 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T3 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_23_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h23 = cp*(T3-T2)

Q_23 = m_dot*(h23) #in kJ/s or kW
Q_cool_23 = -Q_23 #the amount of heat gained by the cooling fluid

print ("Q23 done onto HX is", Q_23, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW/s)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX23 = unit_ann_elec*Q_cool_23 #total elec used by HX in kWh

CO2_emit_23 = Elec_HX23*TX_grid/1000*24*365 #total emissions from HX annually, kg

print ("Q23 emits approximately", CO2_emit_23, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_23 = hx_capex*Q_cool_23 #$ capital cost

print ("Q23 capital costs approximately $", hx_capex_23)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_23 = v.hx_elec*Q_cool_23*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_23 = v.hx_refrig*Q_cool_23*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_23 = v.hx_water*Q_cool_23*v.hx_water_price

#Total OPEX
hx_opex_23 = hx_opelec_23+hx_opref_23+hx_opwat_23

print ("Q23 operating costs approximately $", hx_opex_23, " per year")
print()









## 34 Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p3 = p2 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p4 = 250 #psi =v.p_ou_34_comp 

rho3 = n_mole*p3*M_co2/(v.CO2_IDEAL_GAS_CONST*T3) # density of CO2 at 1; m3/kg

print ("rho3 ", rho3)

v3_dot = m_dot / rho3           #volumetric flowrate at inlet of compressor, m^3/s

print ("v3_dot ", v3_dot)

v4_dot = (p3*v3_dot**n/p4)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v4_dot ", v4_dot)

T4 = (p4/p3)**((n-1)/n)*T3 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W34 is ", T4," K")

W_34 = -1*(p3*v3_dot**n*(v4_dot**(1-n)-v3_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W34 done flux by compressor is", W_34, " kW")

# Emissions ----------------------- #
CO2_emit_34 = CO2_emit*W_34*24*365 #total annual kg emissions in kg

print ("W34 emits approximately", CO2_emit_34, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_34 = W_34*comp_capex

print ("W34 capital costs approximately $", comp_capex_34)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_34 = W_34*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_34 = W_34*NG_price*365 + comp_om_34

print ("W34 fuel costs approximately $", comp_opex_34, " per year")
print()








## 45 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T5 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_45_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h45 = cp*(T5-T4)

Q_45 = m_dot*(h45) #in kJ/s or kW
Q_cool_45 = -Q_45 #the amount of heat gained by the cooling fluid

print ("Q45 done onto HX is", Q_45, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX45 = unit_ann_elec*Q_cool_45 #total elec used by HX in kWh

CO2_emit_45 = Elec_HX45*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q45 emits approximately", CO2_emit_45, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_45 = hx_capex*Q_cool_45 #$ capital cost

print ("Q45 capital costs approximately $", hx_capex_45)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_45 = v.hx_elec*Q_cool_45*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_45 = v.hx_refrig*Q_cool_45*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_45 = v.hx_water*Q_cool_45*v.hx_water_price

#Total OPEX
hx_opex_45 = hx_opelec_45+hx_opref_45+hx_opwat_45

print ("Q45 operating costs approximately $", hx_opex_45, " per year")
print()








## 56 Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p5 = p4 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p6 = 350 #psi =v.p_ou_56_comp 

rho5 = n_mole*p5*M_co2/(v.CO2_IDEAL_GAS_CONST*T5) # density of CO2 at 1; m3/kg

print ("rho5 ", rho5)

v5_dot = m_dot / rho5           #volumetric flowrate at inlet of compressor, m^3/s

print ("v5_dot ", v5_dot)

v6_dot = (p5*v5_dot**n/p6)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v6_dot ", v6_dot)

T6 = (p6/p5)**((n-1)/n)*T5 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W56 is ", T6," K")

W_56 = -1*(p5*v5_dot**n*(v6_dot**(1-n)-v5_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W56 done flux by compressor is", W_56, " kW")

# Emissions ----------------------- #
CO2_emit_56 = CO2_emit*W_56*24*365 #total annual kg emissions in kg

print ("W56 emits approximately", CO2_emit_56, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_56 = W_56*comp_capex

print ("W56 capital costs approximately $", comp_capex_56)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_56 = W_56*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_56 = W_56*NG_price*365 + comp_om_56

print ("W56 fuel costs approximately $", comp_opex_56, " per year")
print()









## 67 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T7 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_67_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h67 = cp*(T7-T6)

Q_67 = m_dot*(h67) #in kJ/s or kW
Q_cool_67 = -Q_67 #the amount of heat gained by the cooling fluid

print ("Q67 done onto HX is", Q_67, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX67 = unit_ann_elec*Q_cool_67 #total elec used by HX in kWh

CO2_emit_67 = Elec_HX67*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q67 emits approximately", CO2_emit_67, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_67 = hx_capex*Q_cool_67 #$ capital cost

print ("Q67 capital costs approximately $", hx_capex_67)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_67 = v.hx_elec*Q_cool_67*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_67 = v.hx_refrig*Q_cool_67*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_67 = v.hx_water*Q_cool_67*v.hx_water_price

#Total OPEX
hx_opex_67 = hx_opelec_67+hx_opref_67+hx_opwat_67

print ("Q67 operating costs approximately $", hx_opex_67, " per year")
print()









## 78 Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p7 = p6 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p8 = 550 #psi =v.p_ou_78_comp 

rho7 = n_mole*p7*M_co2/(v.CO2_IDEAL_GAS_CONST*T7) # density of CO2 at 1; m3/kg

print ("rho7 ", rho7)

v7_dot = m_dot / rho7           #volumetric flowrate at inlet of compressor, m^3/s

print ("v7_dot ", v7_dot)

v8_dot = (p7*v7_dot**n/p8)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v8_dot ", v8_dot)

T8 = (p8/p7)**((n-1)/n)*T7 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W56 is ", T8," K")

W_78 = -1*(p7*v7_dot**n*(v8_dot**(1-n)-v7_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W78 done flux by compressor is", W_78, " kW")

# Emissions ----------------------- #
CO2_emit_78 = CO2_emit*W_78*24*365 #total annual kg emissions in kg

print ("W78 emits approximately", CO2_emit_78, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_78 = W_78*comp_capex

print ("W78 capital costs approximately $", comp_capex_78)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_78 = W_78*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_78 = W_78*NG_price*365 + comp_om_78

print ("W78 fuel costs approximately $", comp_opex_78, " per year")
print()









## 89 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T9 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_89_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h89 = cp*(T9-T8)

Q_89 = m_dot*(h89) #in kJ/s or kW
Q_cool_89 = -Q_89 #the amount of heat gained by the cooling fluid

print ("Q89 done onto HX is", Q_89, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX89 = unit_ann_elec*Q_cool_89 #total elec used by HX in kWh

CO2_emit_89 = Elec_HX89*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q89 emits approximately", CO2_emit_89, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_89 = hx_capex*Q_cool_89 #$ capital cost

print ("Q89 capital costs approximately $", hx_capex_89)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_89 = v.hx_elec*Q_cool_89*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_89 = v.hx_refrig*Q_cool_89*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_89 = v.hx_water*Q_cool_89*v.hx_water_price

#Total OPEX
hx_opex_89 = hx_opelec_89+hx_opref_89+hx_opwat_89

print ("Q89 operating costs approximately $", hx_opex_89, " per year")
print()









## 910 Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p9 = p8 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p10 = 700 #psi =v.p_ou_910_comp 

rho9 = n_mole*p9*M_co2/(v.CO2_IDEAL_GAS_CONST*T9) # density of CO2 at 1; m3/kg

print ("rho9 ", rho9)

v9_dot = m_dot / rho9           #volumetric flowrate at inlet of compressor, m^3/s

print ("v9_dot ", v9_dot)

v10_dot = (p9*v9_dot**n/p10)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v10_dot ", v10_dot)

T10 = (p10/p9)**((n-1)/n)*T9 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W910 is ", T10," K")

W_910 = -1*(p9*v9_dot**n*(v10_dot**(1-n)-v9_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W910 done flux by compressor is", W_910, " kW")

# Emissions ----------------------- #
CO2_emit_910 = CO2_emit*W_910*24*365 #total annual kg emissions in kg

print ("W910 emits approximately", CO2_emit_910, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_910 = W_910*comp_capex

print ("W910 capital costs approximately $", comp_capex_910)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_910 = W_910*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_910 = W_910*NG_price*365 + comp_om_910

print ("W910 fuel costs approximately $", comp_opex_910, " per year")
print()









## 1011 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T11 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_1011_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h1011 = cp*(T11-T10)

Q_1011 = m_dot*(h1011) #in kJ/s or kW
Q_cool_1011 = -Q_1011 #the amount of heat gained by the cooling fluid

print ("Q1011 done onto HX is", Q_1011, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX1011 = unit_ann_elec*Q_cool_1011 #total elec used by HX in kWh

CO2_emit_1011 = Elec_HX1011*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q1011 emits approximately", CO2_emit_1011, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_1011 = hx_capex*Q_cool_1011 #$ capital cost

print ("Q1011 capital costs approximately $", hx_capex_1011)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_1011 = v.hx_elec*Q_cool_1011*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_1011 = v.hx_refrig*Q_cool_1011*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_1011 = v.hx_water*Q_cool_1011*v.hx_water_price

#Total OPEX
hx_opex_1011 = hx_opelec_1011+hx_opref_1011+hx_opwat_1011

print ("Q1011 operating costs approximately $", hx_opex_1011, " per year")
print()









## 1112Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p11 = p10 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p12 = 900 #psi =v.p_ou_1112_comp 

rho11 = n_mole*p11*M_co2/(v.CO2_IDEAL_GAS_CONST*T11) # density of CO2 at 1; m3/kg

print ("rho11 ", rho11)

v11_dot = m_dot / rho11           #volumetric flowrate at inlet of compressor, m^3/s

print ("v11_dot ", v11_dot)

v12_dot = (p11*v11_dot**n/p12)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v12_dot ", v12_dot)

T12 = (p12/p11)**((n-1)/n)*T11 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W1112 is ", T12," K")

W_1112 = -1*(p11*v11_dot**n*(v12_dot**(1-n)-v11_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W1112 done flux by compressor is", W_1112, " kW")

# Emissions ----------------------- #
CO2_emit_1112 = CO2_emit*W_1112*24*365 #total annual kg emissions in kg

print ("W1112 emits approximately", CO2_emit_1112, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_1112 = W_1112*comp_capex

print ("W1112 capital costs approximately $", comp_capex_1112)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_1112 = W_1112*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_1112 = W_1112*NG_price*365 + comp_om_1112 

print ("W1112 fuel costs approximately $", comp_opex_1112, " per year")
print()









## 1213 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T13 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_1213_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h1213 = cp*(T13-T12)

Q_1213 = m_dot*(h1213) #in kJ/s or kW
Q_cool_1213 = -Q_1213 #the amount of heat gained by the cooling fluid

print ("Q1213 done onto HX is", Q_1213, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX1213 = unit_ann_elec*Q_cool_1213 #total elec used by HX in kWh

CO2_emit_1213 = Elec_HX1213*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q1213 emits approximately", CO2_emit_1213, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_1213 = hx_capex*Q_cool_1213 #$ capital cost

print ("Q1213 capital costs approximately $", hx_capex_1213)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_1213 = v.hx_elec*Q_cool_1213*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_1213 = v.hx_refrig*Q_cool_1213*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_1213 = v.hx_water*Q_cool_1213*v.hx_water_price

#Total OPEX
hx_opex_1213 = hx_opelec_1213+hx_opref_1213+hx_opwat_1213

print ("Q1213 operating costs approximately $", hx_opex_1213, " per year")
print()









## 1314Compressor ------------------------------------------------------------------------------##

# Work done ------------------------- #
p13 = p12 #psi
n_mole = v.n_mole
M_co2 = v.M_co2/1000 #kg/mol
n = v.n_poly
p14 = 1080 #psi =v.p_ou_1314_comp 

rho13 = n_mole*p13*M_co2/(v.CO2_IDEAL_GAS_CONST*T13) # density of CO2 at 1; m3/kg

print ("rho13 ", rho13)

v13_dot = m_dot / rho13           #volumetric flowrate at inlet of compressor, m^3/s

print ("v13_dot ", v13_dot)

v14_dot = (p13*v13_dot**n/p14)**(1/n)        #volumetric flowrate at outlet of compressor, m^3/s

print ("v14_dot ", v14_dot)

T14 = (p14/p13)**((n-1)/n)*T13 #Temperature at the outlet of the compressor, K  

print ("Temp at outlet of W1314 is ", T14," K")

W_1314 = -1*(p13*v13_dot**n*(v14_dot**(1-n)-v13_dot**(1-n))/(1-n)) ##Work done flux by compressor 12, in kW

print ("W1314 done flux by compressor is", W_1314, " kW")

# Emissions ----------------------- #
CO2_emit_1314 = CO2_emit*W_1314*24*365 #total annual kg emissions in kg

print ("W1314 emits approximately", CO2_emit_1314, " kg CO2 per year")

# Capital Costs ---------------------- #
#assume average cost for now; consider makign more complex cost down the road using if statements to classify based on the table

comp_capex_1314 = W_1314*comp_capex

print ("W1314 capital costs approximately $", comp_capex_1314)

# Operating Costs (Fuel Costs) for now -------------- #
comp_om_1314 = W_1314*24*365*v.comp_om_cost #annual non-fuel o&m costs
comp_opex_1314 = W_1314*NG_price*365 + comp_om_1314

print ("W1314 fuel costs approximately $", comp_opex_1314, " per year")
print()









## 1415 Heat Exchanger ------------------------------------------------------------------------------##

# Heat Transferred --------------------------#

T15 = 25+273 #outlet temperature of CO2 from HX; =v.t_ou_1415_hx + 273
cp = v.cp_CO2 #kJ/(kgK)
h1415 = cp*(T15-T14)

Q_1415 = m_dot*(h1415) #in kJ/s or kW
Q_cool_1415 = -Q_1415 #the amount of heat gained by the cooling fluid

print ("Q1415 done onto HX is", Q_1415, " kW")

# Emissions ----------------------- #
unit_ann_elec = v.ann_elec/1231 #elec used per kW/s cooled; kWh/(kW)
TX_grid = v.TX_grid*0.453 #2021 CO2 emissions per MWh from tx grid; kg/MWh

Elec_HX1415 = unit_ann_elec*Q_cool_1415 #total elec used by HX in kWh

CO2_emit_1415 = Elec_HX1415*TX_grid*24*365 #total emissions from HX per year, kg

print ("Q1415 emits approximately", CO2_emit_1415, " kg CO2 per year")

# Capital Costs ------------------- #
#assumes an example chiller from paper
#note 1TR = 3.51865kW

hx_capex = v.hx_capex
hx_capex_1415 = hx_capex*Q_cool_1415 #$ capital cost

print ("Q1415 capital costs approximately $", hx_capex_1415)

# Operating Costs ------------------- #
#Electrical costs
hx_opelec_1415 = v.hx_elec*Q_cool_1415*v.hx_elec_price #elec cost in $ per year

#Refrigerant consumed per year
hx_opref_1415 = v.hx_refrig*Q_cool_1415*v.hx_refrig_price #refrigcost in $ per year

#Water costs
hx_opwat_1415 = v.hx_water*Q_cool_1415*v.hx_water_price

#Total OPEX
hx_opex_1415 = hx_opelec_1415+hx_opref_1415+hx_opwat_1415

print ("Q1415 operating costs approximately $", hx_opex_1415, " per year")
print()



















############# COMPILED RESULTS ####################################################################################################################
print()
print()

#Coupled Variables ------------------------------------------------#

#Wellhead pressure ---------------------------------#
v15_dot = v14_dot
p15 = p14
rho_15 = n_mole*p15*M_co2/(v.CO2_IDEAL_GAS_CONST*T15)


pwf = p15
m_dot_wh = v15_dot*rho_15 #mass flow rate in kg/s

print("Wellhead mass flow rate", m_dot_wh, " kg/s")
print("Wellhead pressure", p15, " psi")
print("Wellhead temperature", T15-273, " C")
print("Approximate CO2 processed ", m_dot_wh*3600*24*365, " kg")
print("Approximate CO2 processed ", m_dot_wh*3600*24*365/1000/1000, " Million metric T")

#CO2 Generated ---------------------------------#

q_co2_gen = CO2_emit_12 + CO2_emit_23 + CO2_emit_34 + CO2_emit_45 + CO2_emit_56 + CO2_emit_67 + CO2_emit_78 + CO2_emit_910 + CO2_emit_1011 + CO2_emit_1112 + CO2_emit_1213 + CO2_emit_1314 + CO2_emit_1415 #annual co2 generated with the process (kg)

print("CO2 Generated ", q_co2_gen, " kg")
print("CO2 Generated ", q_co2_gen/1000/1000, " Million metric T")

#Total Capex ---------------------------------#

cost_comp_capex = comp_capex_12 + comp_capex_34 + comp_capex_56 + comp_capex_78 + comp_capex_910 + comp_capex_1112 + comp_capex_1314 #capital cost for compressors ($)
cost_hx_capex = hx_capex_23 + hx_capex_45 + hx_capex_67 + hx_capex_89 + hx_capex_1011 + hx_capex_1213 + hx_capex_1415 #capital cost for hx ($)

cost_fac_capex = cost_comp_capex + cost_hx_capex #Total fac cost 

#Total Opex ---------------------------------#

cost_comp_opex = comp_opex_12 + comp_opex_34 + comp_opex_56 + comp_opex_78 + comp_opex_910 + comp_opex_1112 + comp_opex_1314 #operating cost for compressors ($)
cost_hx_opex = hx_opex_23 + hx_opex_45 + hx_opex_67 + hx_opex_89 + hx_opex_1011 + hx_opex_1213 + hx_opex_1415 #operating cost for hx ($)

cost_fac_opex = cost_comp_opex + cost_hx_opex


print("Total Capital Expenses $", cost_fac_capex)
print("Total Annual Operating Expenses $", cost_fac_opex)