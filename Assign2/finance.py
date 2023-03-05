# This module handles all financial calculations for the MDO CO2 sequestration project
# Variable and parameter descriptions can be found in variables.py file

#Varables used in this file: (comment out after confirming it works) 
q_inj = 50 #mcf/d
n_wells = 5 #wells
p_l = 10000 #ft
p_d = 8 #in
depth = 5500 #ft

#Parameters used in this file: (comment out after confirming it works) 
hxfc = 2.5 #$/mmbtu
cpcc = 0.2 #$/kWh
c_site = 23000 #$/well
tax_credit = 85 #$/tonne
time = 20 #years
discount_rate = 0.1 #dimensionless

#useful conversions: (may move this to separate file for use across model?)
tonne_m3_convert = 556.20 #m3/tonne
m3_cf_convert = 35.32 #cf/m3
tonne_mcf_convert = tonne_m3_convert*m3_cf_convert #mcf/tonne
m_ft_convert = 3.28084 #ft/m
dollar_2005_2023_convert = 1.53 #$2023/$2005

### Revenue ###
revenue = tax_credit/tonne_mcf_convert*q_inj*n_wells*365*time

### Capex ###
CAPEX_well = (-3.9*10**(-8)*(depth/m_ft_convert)**3 + 4*10**(-4)*(depth/m_ft_convert)**2 - 0.84*(depth/m_ft_convert) + 903)*(depth/m_ft_convert)*dollar_2005_2023_convert
CAPEX_wells_total = CAPEX_well*n_wells
CAPEX_pipeline = ((32.086*(p_l/(m_ft_convert*1000))**(-0.033*p_d))*(p_l/m_ft_convert))*dollar_2005_2023_convert
CAPEX_facility = 0 ############# NEEDS UPDATE ########
CAPEX_site = (c_site*n_wells)*dollar_2005_2023_convert
CAPEX_total = CAPEX_wells_total+CAPEX_facility+CAPEX_pipeline+CAPEX_site

print(CAPEX_well)
print(CAPEX_wells_total)
print(CAPEX_pipeline)
print(CAPEX_site)
print(CAPEX_total)

### OPEX / Variable Cost ###


### NPV ###