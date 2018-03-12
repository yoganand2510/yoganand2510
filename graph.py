#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:59:46 2018

@author: ec2017b226
"""

import matplotlib.pyplot as plt

x = [6,12,18,24,30,36]
y = [15,30,45,60,85,100]

plt.xlabel('This is the horizontal axis')
plt.ylabel('This is the vertical axis')
plt.title('kya re graph ah?')

plt.plot(x,y)
plt.show()