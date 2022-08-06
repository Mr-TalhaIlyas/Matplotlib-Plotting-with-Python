# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:07:15 2022

@author: talha
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 700
# create data
fx = [65,72,236]
fy = [82.71,71.74,85.2]
['R-50', 'R-101', 'IR']

y5x=[10,20]
y5y=[81.92,84.82]

y4x=[14,28]
y4y=[84.32,81.47]

ssx=[42,46]
ssy=[76.47,77.07]

rx=[87,104]
ry=[81.8,79.67]

cx=[197]
cy=[60.45]

ex=[39,54,95]
ey=[81.58,83.38,84.11]

dx=[121]
dy=[91.76]

plt.figure(figsize=(8,6))
plt.plot(fx, fy, label = "Faster-RCNN", marker='<')#"Faster-RCNN"
plt.text(fx[0]+.8, fy[0]-1.7, 'R-50', fontsize=9)
plt.text(fx[1]-1.8, fy[1]-1.8, 'R-101', fontsize=9)
plt.text(fx[2]+.5, fy[2]+.5, 'IR', fontsize=9)

plt.plot(y4x, y4y, label = "YOLOv4", marker="v")
plt.text(y4x[0]-12, y4y[0], 'csp', fontsize=9)
plt.text(y4x[1], y4y[1]-1.5, 'p7', fontsize=9)

plt.plot(y5x, y5y, label = "YOLOv5", marker="^")
plt.text(y5x[0], y5y[0]-2, 'v5s', fontsize=9)
plt.text(y5x[1], y5y[1]+1, 'v5x', fontsize=9)

plt.plot(dx, dy, label = "DIANA", marker='*')
plt.text(dx[0]+.5, dy[0]+.5, 'DIANA', fontsize=9)

plt.plot(ssx, ssy, label = "SSD", marker=".")
plt.text(ssx[0]-1.7, ssy[0]-1.7, 'lite', fontsize=9)
plt.text(ssx[1]+.5, ssy[1]+.5, 'lite+', fontsize=9)

plt.plot(rx, ry, label = "Retina-Net", marker='p')
plt.text(rx[0]+1.4, ry[0], 'R-50', fontsize=9)
plt.text(rx[1]+1.4, ry[1], 'R-101', fontsize=9)

plt.plot(cx, cy, label = "Center-Net", marker='X')
plt.text(cx[0]+.5, cy[0]+.5, 'HG-104', fontsize=9)

plt.plot(ex, ey, label = "Efficent-Det", marker='d')
plt.text(ex[0]-.8, ey[0]+1, 'D0', fontsize=9)
plt.text(ex[1]+.7, ey[1]+.7, 'D1', fontsize=9)
plt.text(ex[2]+.7, ey[2]+.7, 'D3', fontsize=9)


plt.legend( loc='lower left', ncol=2)
plt.xlim(0.0, 250)
plt.ylim(50, 100)
plt.grid(color='0.9', linestyle='--')
plt.show()
