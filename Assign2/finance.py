# This module handles all financial calculations for the MDO CO2 sequestration project
# Variable and parameter descriptions can be found in variables.py file

#import variables
import variables

#Varables used in this file: (comment out after confirming it works) 
q_inj = 50 #mcf/d


#Parameters used in this file: hxfc, cpcc, c_site, tax_credit, time, discount_rate

#useful conversions: (may move this to separate file for use across model?)
tonne_m3_convert = 556.20 #m3/tonne
m3_cf_convert = 35.315 #cf/m3
tonne_mcf_convert = (tonne_m3_convert*m3_cf_convert)/1000 #mcf/tonne
m_ft_convert = 3.28084 #ft/m
dollar_2005_2023_convert = 1.53 #$2023/$2005

### Revenue ###
revenue = variables.tax_credit/tonne_mcf_convert*q_inj*variables.n_wells*365*variables.time
print("revenue       %d" % (revenue))

### Capex ###
CAPEX_well = (-3.9*10**(-8)*(variables.depth/m_ft_convert)**3 + 4*10**(-4)*(variables.depth/m_ft_convert)**2 - 0.84*(variables.depth/m_ft_convert) + 903)*(variables.depth/m_ft_convert)*dollar_2005_2023_convert
CAPEX_wells_total = CAPEX_well*variables.n_wells
CAPEX_pipeline = ((32.086*(variables.p_l/(m_ft_convert*1000))**(-0.033*variables.p_d))*(variables.p_l/m_ft_convert))*dollar_2005_2023_convert
CAPEX_facility = 0      ############# NEEDS UPDATE!!!!! ########
CAPEX_site = (variables.c_site*variables.n_wells)*dollar_2005_2023_convert
CAPEX_total = CAPEX_wells_total+CAPEX_facility+CAPEX_pipeline+CAPEX_site
print("CAPEX_total   %d" % (CAPEX_total))

### OPEX / Variable Cost ###
OPEX_pipeline = CAPEX_pipeline*0.022
OPEX_wells = (8.76*(variables.depth/m_ft_convert)+13267)*dollar_2005_2023_convert
OPEX_facility = 0        ############# NEEDS UPDATE!!!!!! ########
OPEX_total = OPEX_facility+OPEX_pipeline+OPEX_wells
print("OPEX_total    %d" % (OPEX_total))

### NPV ###
NPV=(0-CAPEX_total)/1000000

for y in range(1,20):
    cashflow=revenue-CAPEX_site-OPEX_total
    discounted_CF=(cashflow/(1+variables.discount_rate)**y)/1000000
    NPV=NPV+discounted_CF

print("NPV           %f" % (NPV))