##############################################################################################
# This module will perform calculations for the main effects
# Inputs: 'dict' as a dictionary, and 'var' as a string
# Outputs: 'factor_score_matrix' (factor, level, main effect on var variable)
##############################################################################################
#This module takes in a DOE dataframe named df and computes the main effects for each factor level described in dict.
#The main effects are recorded for each factor level based upon their impact on the dependent variable defined in
#'var'.  'var' must match the column title of the dependent variable
#As an example passing main_effect(dict,'NPV') will calculate the effects of each factor and level in 'dict' upon
#the independent variable 'NPV'


def main_effect(dict,var):

    import csv
    import collections
    import pandas as pd
    import numpy as np
    import DOE_generator as deo_gen

    #Change the filepath in this line to reflect where the "DOE_options_only.csv" resides.
    key_list,val_list,df = deo_gen.DOE_generator('C:/Users/jbeil/MDO_Project/Assign2/file_import_and_graph/DOE_options_only.csv')

    output = key_list[8]
    df[output] = df[output].astype('int32')

    reader = csv.DictReader(df)

    #Calculate the overall mean of NPV.  This assumes the NPV column is labeled 'NPV'
    npv_total = df[output].sum()
    npv_count = len(df)
    npv_mean = npv_total / npv_count
    index = 0

    # Create a scoring matrix for each unique factor in the current list
    factor_score_matrix = np.array([["Factor","Factor Level","Main Effect"]], dtype=object)

    for key in key_list:
        #For each key in the dictionary, reset the factor list and import all the values in the "options only" .csv.  
        factor_list = []
        initial_list = val_list[index]
        for x in initial_list:
            # Proceed with only unique values for each factor
            if x not in factor_list:
                factor_list.append(x)
        
        for current_factor in factor_list:
            #This will filter the data frame on the currently selected factor.  Then it will compute the mean for the currently selected factor
            temp_df = df[df[key] == current_factor]
            factor_npv = temp_df[output].sum()
            factor_mean = factor_npv / len(temp_df)

            #This will filter the data frame on all values other than the currently selected factor.  Then it will compute the mean NPV for these other values
            temp_df = df[df[key] != current_factor]
            nonfactor_npv = temp_df[output].sum()
            nonfactor_mean = factor_npv / len(temp_df)

            main_effect = factor_mean - npv_mean
            print(key + ' factor ' + current_factor + ' has a main effect of ' + str(main_effect))
            temp_array = np.array([[str(key), str(current_factor), str(main_effect)]], dtype=object)
            factor_score_matrix = np.vstack((factor_score_matrix, temp_array))
            x='foo'

        index += 1
      
    return factor_score_matrix

main_effect('5','NPV')