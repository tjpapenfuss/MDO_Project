
# wells
rw =              0.12175 #Wellbore Radius Inner radius of injection well tubing measured in ft
n_wells =              10 #Wells,Number of wells,Number of injection wells in system
rel_rough =        0.0006 #Drilling,Relative roughness,Relative roughness of wellbore,,,0.0006,diml
depth =              5500 #Drilling,Well total depth,Average depth of wells to be drilled,5000,6000,5500,ft
rho_CO2sc =          37.5 #Drilling,CO2 fluid density at Super Critcal, lb/ft3 

# pipeline
n_pc =                  0 #Pipeline,Number of connections,Number of clients/sources we plan to bring in,50,1,3,diml
m_dot =               0.2 #Pipeline,Mass_flow_rate,CO2 mass flow rate,lbs/s
p_d =                 .25 #Pipeline,Diameter,Inner diameter of pipe,in
p_l =               10000 #Pipeline,Length,Length from sales point to facility,ft

gravity =          32.174 #Pipeline,Gravity,ft/s^2
abs_rough =            .1 #Pipeline,Absolute Roughness,in
cost_per_foot =        10 #Pipeline,Cost per foot,Cost for one foot of piping,,,,$
cost_per_pc =          50 #Pipeline,Cost per connection,Cost for one source connection,,,,$
press_source =        150 #Pipeline,Pressure at Source,Pressure at the source,,,,psi
temp_source =         293 #Pipeline,Temperature at Source,Temperature at the source,,,,k
p1 =                    0 #Pipeline pressure at inlet of facility, psi
T1 =                    0 #Pipeline temperature at inlet of facility, psi

# facility
n_comp =                0 #Facility,Number of Compressors,Number of Compressors,diml
n_hx =                  0 #Facility,Number of Condensers,Number of Condensers,diml

p_ou_12_comp =          0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 12, up to n_comp",psi
p_ou_34_comp =          0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 34, up to n_comp",psi
p_ou_56_comp =          0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 56, up to n_comp",psi
p_ou_78_comp =          0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 78, up to n_comp",psi
p_ou_910_comp =         0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 910, up to n_comp",psi
p_ou_1112_comp =        0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 1112, up to n_comp",psi
p_ou_1314_comp =        0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor 1314, up to n_comp",psi
t_ou_23_hx =            0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 23, up to n_hx",C
t_ou_45_hx =            0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 45, up to n_hx",C
t_ou_67_hx =            0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 67, up to n_hx",C
t_ou_89_hx =            0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 89, up to n_hx",C
t_ou_1011_hx =          0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 1011, up to n_hx",C
t_ou_1213_hx =          0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 1213, up to n_hx",C
t_ou_1415_hx =          0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX 1415, up to n_hx",C
cp_CO2 =            0.844 #Facility,CO2 Cp,Specific heat capacity of CO2 at constant pressure,,,0.844,KJ/(kgK)
cv_CO2 =            0.655 #Facility,CO2 Cp,Specific heat capacity of CO2 at constant pressure,,,0.655,KJ/(kgK)

adia_index =            0 #Facility,Adiabatic Index,Ratio of Cp/Cv,,,1.289,diml
CO2_IDEAL_GAS_CONST =   8.3145 #Facility,CO2 Ideal Gas Constant,Ideal Gas Constant,,,8.3145,J/molK
CO2_compressability =   0 #Facility,CO2 Compressibility Factor,Compressibility Factor (non-ideal Gas),,,Table,diml
h_CO2 =                 0 #Facility,CO2 Enthalpy,Internal energy of CO2,,,Table,kJ/kg
pin_1_comp =            0 #Facility,1st Compressor inlet  Pressure,Pressure at inlet of 1st compressor,1500,10,14.8,psi
tin_1_comp =            0 #Facility,1st Compressor inlet_Temp,Temp at inlet of 1st compressor,1000,0,25,C
z_fac =                 0 #Facility,Elevation,"Sea-level, onshore, elevation of facility equipment",0,0,0,ft
n_poly =             1.33 #polytropic expansion exponent
M_co2 =             44.01 #g/mol MolasMass CO2
n_mole =                1 #number of moles of CO2 for ideal gas law
CO2_emit =            110 #table of emitted CO2 per unit gas combusted; lb/MMBtu
NG_price =           3.06 #estimate of natural gas price $/MMBTU
ann_elec =         932212 #average estimated heat exchanger electricity needs for a 1231kW sized HX;
TX_grid =             941 #2021 average of co2 emitted by the electrical grid in TX; lb/MWh
comp_capex =       2020.6 #simply grabbed from a paper that showed the estimated capital cost of a compressor; $/(kW)
hx_capex =         247.35 #simply grabbed from a paper that showed a $300k HX delivered 1231kW of cooling; $/(kW) cooled
hx_elec =           75.66 #simply grabbed from a paper that showed electrical needs for a certain kW cooler (kWh_elec/kWcooled) per year
hx_refrig =        0.0097 #simply grabbed from a paper that showed refrigerant needs for a certain kW cooler (kg_refrig/kWcooled) per year
hx_water =          0.183 #simply grabbed from a paper that showed water needs for a certain kW cooler (m3_water/kWcooled) per year
hx_elec_price =      0.15 #TX average rate of elec ($/kWh)
hx_refrig_price =   0.1*3 #simply grabbed from a paper that based off of mexico needs. Tripled cost as a rough est. for usa prices ($/kg)
hx_water_price =    0.830 #harris county estimated water costs ($/m3)
comp_om_cost =    0.01108 #simply grabbed from a paper that showed the est o&m non-fuel costs $/kWh



# subsurface
por =                0.22 #Porosity,Porosity of the reservoir rock we are injecting into,%
perm =                200 #Permeability,Permeability of the reservoir rock, mD
Q_max =             87000 #Reservoir capcity,Frio Reservoir CO2 Storage Capacity (P5 Volume estimates),"megatons, Mt"
skin =                  0 #Skin,Assumed skin around the wellbore due to completion,diml
visc_CO2SC =        0.682 #CO2 viscosity,Viscosity of CO2 in the reservoir (assume temp 100 degF),,,0.682,cP
Z_CO2SC =           0.992 #CO2 formation volume factor,,Formation volume factor for supercritical CO2 at p_res & T_res,,,0.0247,cf/scf
well_life =            20 #Well life,Assumed years of injection for each well,,,20,years
p_res =              2234 #Reservoir pressure,Initial pressure of the Frio reservoir (assumed constant / infinite acting),,,2234,psi
density_CO2SC =      37.5 #CO2 density,Density of supercritical CO2,,,37.5,lb/ft^3
h_res =               150 #Reservoir thickness,Frio reservoir thickness,,,150,ft
t_res =               135 #Reservoir temperature,Frio reservoir temperature,,,135,deg F
p_injmax =           3600 #Maximum injection pressure,Maximum pressure that can be injected without fracturing Frio formation,,,3600,psi

# finance
hxfc =                 2.5 #HX Fuel costs,Cost of fuel needed to generate temperature difference for HX,$10.00 ,$1.50 ,$2.50 ,$/mmbtu
cpcc =                 0.2 #Comp Cost Coefficient,The per-unit cost for running the compressor (electricity),$0.40 ,$0.10 ,$0.20 ,$/kWh
discount_rate =        0.1 #Discount Rate,Assumed discount rate for project,,,10,diml
c_site =             23000 #Wellsite costs,includes leasing costs and other annual costs,,,23000, $/well
tax_credit =            85 #Tax credit,45Q tax credit for point source sequestered CO2,,,85,$/tonne
time =                  20 #Well injection time, assumed duration of well life for each well,,,20,years