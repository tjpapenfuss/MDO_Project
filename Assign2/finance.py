# This module handles all financial calculations for the MDO CO2 sequestration project
# Variable and parameter descriptions can be found in variables.py file

#import variables
import variables

#Parameters used in this file: hxfc, cpcc, c_site, tax_credit, time, discount_rate


### Revenue ###
def revenue_func(q_inj, n_wells):
    #variables/parameters used
    tax_credit = variables.tax_credit
    time = variables.time

    #useful conversions: (may move this to separate file for use across model?)
    tonne_m3_convert = 556.20 #m3/tonne
    m3_cf_convert = 35.315 #cf/m3
    tonne_mcf_convert = (tonne_m3_convert*m3_cf_convert)/1000 #mcf/tonne

    revenue = tax_credit/tonne_mcf_convert*q_inj*n_wells*365*time
    return revenue

### Capex ###
def CAPEX_func(p_l,p_d, n_wells):
    #variables/parameters used
    depth = variables.depth
    c_site = variables.c_site

    #useful conversions: (may move this to separate file for use across model?)
    m_ft_convert = 3.28084 #ft/m
    dollar_2005_2023_convert = 1.53 #$2023/$2005
    
    CAPEX_well = (-3.9*10**(-8)*(depth/m_ft_convert)**3 + 4*10**(-4)*(depth/m_ft_convert)**2 - 0.84*(depth/m_ft_convert) + 903)*(depth/m_ft_convert)*dollar_2005_2023_convert
    CAPEX_wells_total = CAPEX_well*n_wells
    CAPEX_pipeline = ((32.086*(p_l/(m_ft_convert*1000))**(-0.033*p_d))*(p_l/m_ft_convert))*dollar_2005_2023_convert
    CAPEX_facility = 0      ############# NEEDS UPDATE!!!!! ########
    CAPEX_site = (c_site*n_wells)*dollar_2005_2023_convert
    CAPEX_total = CAPEX_wells_total+CAPEX_facility+CAPEX_pipeline+CAPEX_site
    return CAPEX_total, CAPEX_pipeline, CAPEX_site

### OPEX / Variable Cost ###
def OPEX_func(CAPEX_pipeline, n_wells):
    #variables/parameters used
    depth = variables.depth

    #useful conversions: (may move this to separate file for use across model?)
    m_ft_convert = 3.28084 #ft/m
    dollar_2005_2023_convert = 1.53 #$2023/$2005

    OPEX_pipeline = CAPEX_pipeline*0.022
    OPEX_wells = (8.76*(depth/m_ft_convert)+13267)*dollar_2005_2023_convert*n_wells
    OPEX_facility = 0        ############# NEEDS UPDATE!!!!!! ########
    OPEX_total = OPEX_facility+OPEX_pipeline+OPEX_wells
    return OPEX_total

### NPV ###
def NPV_func(CAPEX_total, revenue, CAPEX_site, OPEX_total):
    #variables/parameters used
    discount_rate = variables.discount_rate

    NPV=(0-CAPEX_total)/1000000

    for y in range(1,20):
        cashflow=revenue-CAPEX_site-OPEX_total
        discounted_CF=(cashflow/(1+discount_rate)**y)/1000000
        NPV=NPV+discounted_CF
    return NPV
