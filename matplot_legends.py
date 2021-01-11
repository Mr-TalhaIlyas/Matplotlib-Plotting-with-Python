# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:22:34 2020

@author: Talha
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(7,9))
#plt.subplot(211)
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")

# Place a legend above this subplot, expanding itself to
# fully use the given bounding box.
leg = plt.legend(bbox_to_anchor=(0, -.1, 1, 5), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0., prop=dict(size=10), shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.4)
#%%
plt.figure(figsize=(7,9))
#plt.subplot(223)
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")
# Place a legend to the right of this smaller subplot.
leg = plt.legend(bbox_to_anchor=(1.05, 1, 1, .1), loc='upper left', 
           ncol=2, mode="expand", borderaxespad=0., prop=dict(size=10), shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()
