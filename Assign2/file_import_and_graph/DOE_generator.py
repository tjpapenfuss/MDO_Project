##############################################################################################
# This module will generate a DOE given a file that has factors and levels. 
# Inputs: fileName - this is a file with factors and levels.
# Outputs: 
#   key_list - all the individual factors from the fileName. This is the first row of items
#   val_list - all the levels of each factor. This is all the unique values for each factor
#   DF - a data frame that has a DOE generated. For more information on how this is created
#        please reference the docs here: https://pypi.org/project/pycubedoe/
##############################################################################################

import csv
import collections
import pycubedoe as pc

def DOE_generator(fileName):

    dict = collections.defaultdict(list)

    with open(fileName, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k, v in row.items():
                dict[k].append(v)
    # print(dict)
    # print(dict["Wellbore Radius"])
    key_list = list(dict.keys())
    val_list = list(dict.values())
    DOE = pc.pycubeDOE(numeric = None, categorical = dict)

    # print(DOE)

    DOE.to_csv('DOE_tanner.csv')
    return key_list, val_list, DOE


# Below is for testing the above functionality works. 
key_list, val_list, df = DOE_generator('DOE_options_only.csv')
print(df)
# print(key_list)
