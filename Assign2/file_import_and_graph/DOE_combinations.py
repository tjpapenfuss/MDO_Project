import csv
import collections
import pycubedoe as pc

dict = collections.defaultdict(list)

with open('DOE_options_only.csv', 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for k, v in row.items():
            dict[k].append(v)
print(dict)
print(dict["Wellbore Radius"])

DOE = pc.pycubeDOE(numeric = None, categorical = dict)

print(DOE)

DOE.to_csv('DOE_tanner.csv')
