#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:13:15 2018

@author: ec2017b226
"""
import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
right = [1, 2, 3, 4, 5]
 
# heights of bars
height = [10, 24, 36, 40, 5]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
 
# plotting a bar chart
plt.bar(right, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()
