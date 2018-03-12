#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:15:09 2018

@author: ec2017b226
"""
import matplotlib.pyplot as plt
 
# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]
 
# plotting points as a scatter plot
plt.scatter(x, y, label= "star", color= "purple", 
            marker= "*", s=30)
 
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()
 
# function to show the plot
plt.show()
