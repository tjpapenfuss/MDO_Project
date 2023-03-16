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
# key_list, val_list, df = DOE_generator('DOE_options_only.csv')
# print(df)
# print(key_list)