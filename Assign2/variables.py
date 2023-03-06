
# wells
rw =                    0 # Wellbore Radius Inner radius of injection well tubing measured in ft
n_wells =               0 # Wells,Number of wells,Number of injection wells in system
rel_rough =             0 # Drilling,Relative roughness,Relative roughness of wellbore,,,0.0006,diml
depth =                 5500 #Drilling,Well total depth,Average depth of wells to be drilled,5000,6000,5500,ft
rho_CO2sc =             37.5 #Drilling,CO2 fluid density at Super Critcal, lb/ft3 

# pipeline
n_pc =                  0 # Pipeline,Number of connections,Number of clients/sources we plan to bring in,50,1,3,diml
m_dot =                 0 # Pipeline,Mass_flow_rate,CO2 mass flow rate,kg/s
p_d =                   8 # Pipeline,Diameter,Inner diameter of pipe,in
p_l =                   0 #Pipeline,Length,Length from sales point to facility,ft
gravity =               0 #Pipeline,Gravity,ft/s^2
abs_rough =             0 #Pipeline,Absolute Roughness,in
cost_per_foot =         0 #Pipeline,Cost per foot,Cost for one foot of piping,,,,$
cost_per_pc =           0 #Pipeline,Cost per connection,Cost for one source connection,,,,$
press_source =          0 #Pipeline,Pressure at Source,Pressure at the source,,,,psi
temp_source =           0 #Pipeline,Temperature at Source,Temperature at the source,,,,deg F

# facility
n_comp =                0 #Facility,Number of Compressors,Number of Compressors,diml
n_hx =                  0 #Facility,Number of Condensers,Number of Condensers,diml
pou_i_comp =            0 #Facility,Compressor outlet pressure,"Pressure at outlet of each compressor i, up to n_comp",psi
tou_i_hx =              0 #Facility,HX Outlet Temperature,"Temp at outlet of each HX k, up to n_hx",C
cp_CO2 =                0 # Facility,CO2 Cp,Specific heat capacity of CO2 at constant pressure,,,0.844,KJ/(kgK)
cv_CO2 =                0 #Facility,CO2 Cp,Specific heat capacity of CO2 at constant pressure,,,0.655,KJ/(kgK)
adia_index =            0 #Facility,Adiabatic Index,Ratio of Cp/Cv,,,1.289,diml
CO2_IDEAL_GAS_CONST =   8.3145 #Facility,CO2 Ideal Gas Constant,Ideal Gas Constant,,,8.3145,J/molK
CO2_compressability =   0 #Facility,CO2 Compressibility Factor,Compressibility Factor (non-ideal Gas),,,Table,diml
h_CO2 =                 0 #Facility,CO2 Enthalpy,Internal energy of CO2,,,Table,kJ/kg
pin_1_comp =            0 #Facility,1st Compressor inlet  Pressure,Pressure at inlet of 1st compressor,1500,10,14.8,psi
tin_1_comp =            0 #Facility,1st Compressor inlet_Temp,Temp at inlet of 1st compressor,1000,0,25,C
z_fac =                 0 #Facility,Elevation,"Sea-level, onshore, elevation of facility equipment",0,0,0,ft

# subsurface
por =                   0 # Subsurface,Porosity,Porosity of the reservoir rock we are injecting into,%
perm =                  0 #Subsurface,Permeability,Permeability of the reservoir rock, mD
q_max =                 0 # Subsurface,Reservoir capcity,Frio Reservoir CO2 Storage Capacity (P5 Volume estimates),"megatons, Mt"
skin =                  0 # Subsurface,Skin,Assumed skin around the wellbore due to completion,diml
CO2SC_VISC =            0 # Subsurface,CO2 viscosity,Viscosity of CO2 in the reservoir (assume temp 100 degF),,,0.682,cP
well_life =             0 #Subsurface,Well life,Assumed years of injection for each well,,,20,years
FVF_CO2SC =             0 #Subsurface,CO2 formation volume factor,,Formation volume factor for supercritical CO2 at p_res & T_res,,,0.0247,cf/scf
p_res =                 0 #Subsurface,Reservoir pressure,Initial pressure of the Frio reservoir (assumed constant / infinite acting),,,2234,psi
CO2SC_DEN =             0 #Subsurface,CO2 density,Density of supercritical CO2,,,37.5,lb/ft^3
h_res =                 0 #Subsurface,Reservoir thickness,Frio reservoir thickness,,,150,ft
t_res =                 0 #Subsurface,Reservoir temperature,Frio reservoir temperature,,,135,deg F
p_injmax =              0 #Subsurface,Maximum injection pressure,Maximum pressure that can be injected without fracturing Frio formation,,,3600,psi

# finance
hxfc =                 2.5 #HX Fuel costs,Cost of fuel needed to generate temperature difference for HX,$10.00 ,$1.50 ,$2.50 ,$/mmbtu
cpcc =                 0.2 #Comp Cost Coefficient,The per-unit cost for running the compressor (electricity),$0.40 ,$0.10 ,$0.20 ,$/kWh
discount_rate =        0.1 #Discount Rate,Assumed discount rate for project,,,10,diml
c_site =             23000 #Wellsite costs,includes leasing costs and other annual costs,,,23000, $/well
tax_credit =            85 #Tax credit,45Q tax credit for point source sequestered CO2,,,85,$/tonne
time =                  20 #Well injection time, assumed duration of well life for each well,,,20,years