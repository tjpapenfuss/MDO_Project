# ------------------------------------------------------------------------------------------------------------------ #
# 16.888 MDO; Multidisciplinary Design Optimization. 
# Project: Design and optimization of CO2 injection. 
# Authors: John Beilstein, Warren Anderson, Brooke DiMartino, Stephen Tainter, Tanner Papenfuss
# Team name: Terra Sparkling
# ------------------------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------------------------ #
# Import all necessary packages
# ------------------------------------------------------------------------------------------------------------------ #
from numpy import *
import variables
import pipeline as pipes
import finance as finance
import subsurface as sub
import facilities
import wells as wells
import pandas as pd


def experiment(input_tuple):
    num_wells = input_tuple[0]
    num_connections = input_tuple[1]
    mass_flow_rate = num_connections*2
    pipeline_diameter = input_tuple[2]
    pipeline_length = input_tuple[3]
    p2 = input_tuple[4]
    p4 = input_tuple[5]
    p6 = input_tuple[6]
    p8 = input_tuple[7]
    p10 = input_tuple[8]
    p12 = input_tuple[9]
    
    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Facilities
    # Required inputs: m_dot, pi, Ti, 
    # Outputs: po,To, 
    # ------------------------------------------------------------------------------------------------------------------ #

    ## 12 Compressor ------------------------------------------------------------------------------##
    #press_out = 345 
    press_out = variables.press_source# at or below 350 kPa
    p2 = press_out #kPa
    test_temp_out = variables.temp_source # 300
    m_dot = mass_flow_rate
    p2,T2,W12,CO2_emit_12,comp_capex_12,comp_om_12,comp_opex_12,m_dot,mtot = facilities.work_comp(press_out, p2, m_dot, test_temp_out)

    ##23 Heat Exchanger ----------------------------------------------------------------------------##
    T3 = variables.T_out_hx+273
    p3,T3,Q23,Q_cool_23,CO2_emit_23,hx_capex_23,hx_opexelec_23,hx_opref_23,hx_opwat_23,hx_opex_23 = facilities.heat_hx(p2,T2,T3,m_dot)

    ## 34 Compressor ------------------------------------------------------------------------------##
    #p4 = 1500 #kPa
    p4,T4,W34,CO2_emit_34,comp_capex_34,comp_om_34,comp_opex_34,m_dot,mtot = facilities.work_comp(p3,p4, m_dot, T3)

    ##45 Heat Exchanger ----------------------------------------------------------------------------##
    T5 = variables.T_out_hx+273
    p5,T5,Q45,Q_cool_45,CO2_emit_45,hx_capex_45,hx_opexelec_45,hx_opref_45,hx_opwat_45,hx_opex_45 = facilities.heat_hx(p4,T4,T5,m_dot)

    ## 56 Compressor ------------------------------------------------------------------------------##
    #p6 = 2500 #kPa
    p6,T6,W56,CO2_emit_56,comp_capex_56,comp_om_56,comp_opex_56,m_dot,mtot = facilities.work_comp(p5, p6, m_dot, T5)

    ##67 Heat Exchanger ----------------------------------------------------------------------------##
    T7 = variables.T_out_hx+273
    p7,T7,Q67,Q_cool_67,CO2_emit_67,hx_capex_67,hx_opexelec_67,hx_opref_67,hx_opwat_67,hx_opex_67 = facilities.heat_hx(p6,T6,T7,m_dot)

    ## 78Compressor ------------------------------------------------------------------------------##
    #p8 = 4000 #kPa
    p8,T8,W78,CO2_emit_78,comp_capex_78,comp_om_78,comp_opex_78,m_dot,mtot = facilities.work_comp(p7, p8, m_dot, T7)

    ##89 Heat Exchanger ----------------------------------------------------------------------------##
    T9 = variables.T_out_hx+273
    p9,T9,Q89,Q_cool_89,CO2_emit_89,hx_capex_89,hx_opexelec_89,hx_opref_89,hx_opwat_89,hx_opex_89 = facilities.heat_hx(p8,T8,T9,m_dot)

    ## 910Compressor ------------------------------------------------------------------------------##
    #p10 = 5500 #kPa
    p10,T10,W910,CO2_emit_910,comp_capex_910,comp_om_910,comp_opex_910,m_dot,mtot = facilities.work_comp(p9, p10, m_dot, T9)

    ##1011 Heat Exchanger ----------------------------------------------------------------------------##
    T11 = variables.T_out_hx+273
    p11,T11,Q1011,Q_cool_1011,CO2_emit_1011,hx_capex_1011,hx_opexelec_1011,hx_opref_1011,hx_opwat_1011,hx_opex_1011 = facilities.heat_hx(p10,T10,T11,m_dot)

    ##1112 Compressor ------------------------------------------------------------------------------##
    #p12 = 6500 #kPa
    p12,T12,W1112,CO2_emit_1112,comp_capex_1112,comp_om_1112,comp_opex_1112,m_dot,mtot = facilities.work_comp(p11, p12, m_dot, T11)

    ##1213 Heat Exchanger ----------------------------------------------------------------------------##
    T13 = variables.T_out_hx+273
    p13,T13,Q1213,Q_cool_1213,CO2_emit_1213,hx_capex_1213,hx_opexelec_1213,hx_opref_1213,hx_opwat_1213,hx_opex_1213 = facilities.heat_hx(p12,T12,T13,m_dot)

    ##1314 Compressor ------------------------------------------------------------------------------##
    p14 = variables.CO2_crit_p #kPa
    p14,T14,W1314,CO2_emit_1314,comp_capex_1314,comp_om_1314,comp_opex_1314,m_dot,mtot = facilities.work_comp(p13, p14, m_dot, T13)

    ##1415 Heat Exchanger ----------------------------------------------------------------------------##
    # p15 is the well head pressure
    T15 = variables.T_out_hx+273
    p15,T15,Q1415,Q_cool_1415,CO2_emit_1415,hx_capex_1415,hx_opexelec_1415,hx_opref_1415,hx_opwat_1415,hx_opex_1415 = facilities.heat_hx(p14,T14,T15,m_dot)

    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Pipeline
    # Required inputs:  mass_dot, press_source, p_d, p_l, n_pc (all units are SI (ft, lbsf, lbsm, PSI))
    # Outputs: press_i (kPa), vel_i (m/s), temp_i (K), CO2_emit_d, comp_capex_d, comp_opex_d
    # ------------------------------------------------------------------------------------------------------------------ #

    diameter_inches = pipeline_diameter / 12
    pipes_press_out, pipes_vel_out, pipes_temp_out, CO2_emit_pipes, comp_capex_pipes, comp_opex_pipes = pipes.pipes_out(mass_flow_rate, 
                                                                                                p15, 
                                                                                                diameter_inches, 
                                                                                                pipeline_length, T15)

    ##CO2 generated----------------------------------------------------------------------------------##
    tot_co2_gen = facilities.co2_gen(CO2_emit_pipes,CO2_emit_12,CO2_emit_23,CO2_emit_34,CO2_emit_45,CO2_emit_56,CO2_emit_67,CO2_emit_78,CO2_emit_910,CO2_emit_1011,CO2_emit_1112,CO2_emit_1213,CO2_emit_1314,CO2_emit_1415)
    print("annual co2 entering plant ", mtot/1000/1000000, " million metric tons/year")
    print("total_co2_gen: ", tot_co2_gen/1000/1000000, " million metric tons/year")
    print("net co2 MMT/year", -(mtot-tot_co2_gen)/1000/1000000)

    ##FAC Capex----------------------------------------------------------------------------------##
    cost_comp_capex, cost_hx_capex, CAPEX_facilities = facilities.fac_capex(comp_capex_pipes,comp_capex_12,comp_capex_34,comp_capex_56,comp_capex_78,comp_capex_910,comp_capex_1112,comp_capex_1314,hx_capex_23,hx_capex_45,hx_capex_67,hx_capex_89,hx_capex_1011,hx_capex_1213,hx_capex_1415)

    ##FAC OPEX----------------------------------------------------------------------------------##
    cost_comp_opex, cost_hx_opex, OPEX_facilities = facilities.fac_opex (comp_opex_pipes,comp_opex_12,comp_opex_34,comp_opex_56,comp_opex_78,comp_opex_910,comp_opex_1112,comp_opex_1314,hx_opex_23,hx_opex_45,hx_opex_67,hx_opex_89,hx_opex_1011,hx_opex_1213,hx_opex_1415)


    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Wells
    # Required inputs: avg_vol, Pwh
    # Outputs: p_wf_t
    # ------------------------------------------------------------------------------------------------------------------ #
    pressure_wellhead = pipes_press_out / 6.89476
    mass_flow_rate_wells = (mass_flow_rate * 2.2) / num_wells
    p_wf_t = wells.wells(mass_flow_rate_wells, pressure_wellhead)
    print("The Value of p_wf_t wellbore injection pressure is: " + str(p_wf_t))

    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Subsurface
    # Required inputs: p_wf_t
    # Outputs: q_inj
    # ------------------------------------------------------------------------------------------------------------------ #
    q_inj = sub.subsurface(p_wf_t)
    print("The Value of q_inj injection volume is: " + str(q_inj))


    #Module name: Finance
    #Required inputs: p_d, p_l, q_inj, n_wells
    #Outputs: NPV
    # q_inj=50                #q_inj should be an output of a subsurface function, so delete this once it's available
    q_inj_finance = q_inj / 1000 # Convert from scf to mcf
    revenue = finance.revenue_func(q_inj_finance, variables.n_wells) 
    CAPEX_total, CAPEX_pipeline, CAPEX_site = finance.CAPEX_func(variables.p_l, variables.p_d, variables.n_wells, num_connections, CAPEX_facilities)
    OPEX_total = finance.OPEX_func(CAPEX_pipeline, variables.n_wells, OPEX_facilities)
    NPV = finance.NPV_func(CAPEX_total, revenue, CAPEX_site, OPEX_total)

    print("The Value of NPV is: " + str(NPV))
    print("The Value of CAPEX_total is: " + str(CAPEX_total))
    print("The Value of OPEX_total is: " + str(OPEX_total))
    print("The Value of CAPEX_pipeline is: " + str(CAPEX_pipeline))
    # We need to make this negative so we can minimize it.

    # Adding in Constraints
    # 1. Qinj * num_wells * time <= Qmax
    # q_const is the q_inj constraint in scf/day converted to mcf/year * 365 days/year * time * num_wells
    # This whole thing is devided by 19.64 to convert from mcf to tonnes. Then converted to MMT/year
    q_constraint = (((q_inj / 1000) * 365 * num_wells * variables.time) / 19.64) / 1000000
    if(q_constraint > variables.Q_max):
        NPV = -1000000 + NPV

    # 2. The pressure at the bottom of the well cannot exceed max inj pressure which is determined
    # by reservoir pore pressure fracture gradient, PWH > Pwf
    if(p_wf_t > variables.p_injmax):
        NPV = -1000000 + NPV

    return -NPV

