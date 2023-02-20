This project was created for 16.888 Multi-Diciplinary Design Optimization.
Authors: Tanner Papenfuss, Brooke DiMartino, Stephen Tainter, John Beilstein, and Warren Anderson

Description of the files:
options.csv: This file contains the options that are generated via our options table here: https://mitprod-my.sharepoint.com/:x:/g/personal/tpapenfu_mit_edu/EcfoBNSw6I5NiL4NYc-GxtUBrLK-wFBOtJgtZOg6KNoT0w?e=6KZxx7.
In this file we also assign values to each of the options given certain metrics. ***INSERT METRICS WHEN FINALIZED***

architectures.csv: This file contains the sample architectures that will be fed into the model.py file. These architectures are not necessarily feasible, they are just options to consider for our final design. Eventually we will select a few of these architectures and generate a tradespace. 

model.py: Python file that computes for each architecture in architectures.csv a score for each metric, including cost. 

outputTesting.csv: The output file from model.py. This contains the scores for each architecture. This will be ported to a tradespace graph. 