#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:17:49 2018

@author: ec2017b226
"""
# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
 
# setting the x - coordinates
x = np.arange(0, 6*(np.pi),.1)
# setting the corresponding y - coordinates
y = np.cos(x)
 
# potting the points
plt.plot(x, y)
 
# function to show the plot
plt.show()
