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


def experiment(injection_tubing_diameter, num_wells, num_connections, mass_flow_rate, pipeline_diameter, 
                pipeline_length, num_compressors, num_condensers, comp_out_press, p2,p4,p6,p8,p10,p12):
    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Pipeline
    # Required inputs:  m_dot, press_source, p_d, p_l, n_pc
    # Outputs: p_i, t_i, v_i
    # ------------------------------------------------------------------------------------------------------------------ #
    diameter_inches = pipeline_diameter / 12
    pipes_press_out, pipes_vel_out, pipes_temp_out = pipes.pipes_out(mass_flow_rate, variables.press_source, 
                                                                diameter_inches, pipeline_length) # , variables.n_pc)
    print("Pipes pressure output: ", pipes_press_out)
    print("Pipes velocity output: ", pipes_vel_out)
    #print("Pipes temperature output: ", pipes_temp_out)
    #print("Pipes cost output: ", pipes_cost_out)


    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Facilities
    # Required inputs: m_dot, pi, Ti, 
    # Outputs: po,To, 
    # ------------------------------------------------------------------------------------------------------------------ #

    ## 12 Compressor ------------------------------------------------------------------------------##
    press_out = 345 # pipes_press_out * 6.89476  #
    p2 = 700 #kPa
    test_temp_out = pipes_temp_out # 300
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


    ##CO2 generated----------------------------------------------------------------------------------##
    tot_co2_gen = facilities.co2_gen(CO2_emit_12,CO2_emit_23,CO2_emit_34,CO2_emit_45,CO2_emit_56,CO2_emit_67,CO2_emit_78,CO2_emit_910,CO2_emit_1011,CO2_emit_1112,CO2_emit_1213,CO2_emit_1314,CO2_emit_1415)
    print("annual co2 entering plant ", mtot/1000/1000000, " million metric tons/year")
    print("total_co2_gen: ", tot_co2_gen/1000/1000000, " million metric tons/year")
    print("net co2 MMT/year", -(mtot-tot_co2_gen)/1000/1000000)

    ##FAC Capex----------------------------------------------------------------------------------##
    cost_comp_capex, cost_hx_capex, CAPEX_facilities = facilities.fac_capex(comp_capex_12,comp_capex_34,comp_capex_56,comp_capex_78,comp_capex_910,comp_capex_1112,comp_capex_1314,hx_capex_23,hx_capex_45,hx_capex_67,hx_capex_89,hx_capex_1011,hx_capex_1213,hx_capex_1415)

    ##FAC OPEX----------------------------------------------------------------------------------##
    cost_comp_opex, cost_hx_opex, OPEX_facilities = facilities.fac_opex (comp_opex_12,comp_opex_34,comp_opex_56,comp_opex_78,comp_opex_910,comp_opex_1112,comp_opex_1314,hx_opex_23,hx_opex_45,hx_opex_67,hx_opex_89,hx_opex_1011,hx_opex_1213,hx_opex_1415)


    # ------------------------------------------------------------------------------------------------------------------ #
    # Module name: Wells
    # Required inputs: avg_vol, Pwh
    # Outputs: p_wf_t
    # ------------------------------------------------------------------------------------------------------------------ #
    pressure_wellhead = p15 / 6.89476
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
    return NPV, mtot, CAPEX_total



# TO DO: Add in the DOE generation functionality. 
imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
npv_array = []
mtot_array = []
capex_array = []
for index, row in imported_df.iterrows():
    # Variable initialization from the DOE. 
    
    NPV,mtot,CAPEX_total = experiment(imported_df.loc[index]["Injection Tubing Diameter"],
                        imported_df.loc[index]["Number of Wells"],
                        imported_df.loc[index]["Number of Connections"],
                        imported_df.loc[index]["Mass Flow Rate"],
                        imported_df.loc[index]["Pipeline Diameter"],
                        imported_df.loc[index]["Pipeline Length"],
                        imported_df.loc[index]["Number of Compressors"],
                        imported_df.loc[index]["Number of Condensers"],
                        imported_df.loc[index]["Compressor Outlet Pressure"],
                        imported_df.loc[index]["p2"],
                        imported_df.loc[index]["p4"],
                        imported_df.loc[index]["p6"],
                        imported_df.loc[index]["p8"],
                        imported_df.loc[index]["p10"],
                        imported_df.loc[index]["p12"])
    #Net_Present_Value_Array = [NPV, NPV]
    npv_array.append(NPV)
    mtot_array.append(mtot/1000/1000000)
    capex_array.append(CAPEX_total)
    #print(imported_df)
imported_df["NPV"] = npv_array
imported_df["mtot"] = mtot_array
imported_df["CAPEX_total"] = capex_array
imported_df.to_csv("final_df.csv")