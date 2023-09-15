# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:28:39 2023

@author: regal
"""

## Creating an XRD file to fit Quinn's xrd autonormalization from a simulated .txt

# Create a copy of a regular PXRD file to be overwritten. Load it in here.
PXRD = open('PXRDfiletobereplaced.txt')
data = PXRD.readlines()

# Check if the file has at least 151 lines
if len(data) >= 151:
    # Remove all lines past 151
    data = data[151:]

    # Open the same file for writing to overwrite it with the first 151 lines
    with open('PXRDfiletobereplaced.txt', 'w') as file:
        file.writelines(data)

    print("All lines past line 151 have been removed.")
else:
    print("The file has fewer than 151 lines. No lines were removed.")

# Close that file and open your simulation file (it should only have values separated by commas)
PXRD.close()
simulatedPXRD = open('ZIF-11 Profile.txt')
simulatedData = simulatedPXRD.readlines()
simulatedPXRD.close()

angle = []
intensity = [] 

# Create angle and intensity lists from simulation data
for line in simulatedData[0:]:
    print(line)
    split = line.strip().split('\t')
    angle.append(float(split[0]))
    intensity.append(float(split[1]))


# Open the original file to rewrite the 
with open('PXRDfiletobereplaced.txt', 'a') as PXRD:
    # Write the data from both lists in the desired format
    # Zip combines the items in the lists
    for item1, item2 in zip(angle, intensity):
        # f" is the start of an f string, which allows you to put expressions in the {}
        # .5f means to format the float with 5 decimal places
        # , \n adds a comma and a new line to the string
        line = f"{item1:.5f}, {item2:.5f},\n"
        PXRD.write(line)

print("Data has been appended to file.")

print(PXRD)

