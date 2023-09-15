# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:35:41 2023

@author: regal
"""

import matplotlib.pyplot as plt

figure, axis = plt.subplots(2,1, figsize=(6,5))
plt.subplots_adjust(hspace=0.4) 

# Create lists angle and intensity
angle1 = []
intensity1 = []

# Open non-simulated file and read data
file = open('RF-1-19.3.txt')
data1 = file.readlines()
file.close()

# Divide text data into two lists, angle and intensity
for line in data1[151:]:
    split = line.strip().split(',')
    angle1.append(float(split[0]))
    intensity1.append(float(split[1]))
    
axis[0].plot(angle1, intensity1)
axis[0].set_title("Non-Simulated - ZIF-71", fontsize = 14)
axis[0].set_xlim([0, 30])

# Set a larger title for the entire figure
figure.suptitle("RF-1-19, PXRD2", fontsize=18)  # Adjust the fontsize as needed

# Open Simulated file and read data
file2 = open('ZIF-71profilenolabels.txt')
data2 = file2.readlines()
file.close()

angle2 = []
intensity2 = []

# Divide text data into two lists, angle and intensity
for line in data2[0:]:
    split = line.strip().split(',')
    angle2.append(float(split[0]))
    intensity2.append(float(split[1]))

axis[1].plot(angle2, intensity2)
plt.xlim([0,30])
axis[1].set_title("Simulated", fontsize = 14)

# Add a note to the top figure
#note_text = "Scherrer Size: 77.4 nm"
#figure.text(.7, .8, note_text, fontsize=12, ha='center', bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='none'))
axis[0].set_yticklabels([])
axis[1].set_yticklabels([])


plt.show()

