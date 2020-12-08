# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:00:32 2018

@author: Ashlee
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,101,1)
plt.plot(t,t,'r--')
plt.ylabel('t')
#plt.show() #somewhat like hold on in matlab

plt.plot(t,t**2,'bs')
plt.plot(t,t**3,'g^')

#plt.axis([0, 20, 0, 30])
plt.savefig('exampleplot.png')
plt.show()

fig = plt.figure(figsize=(10.0,3.0))

axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.set_ylabel('t')
axes1.plot(t,t,'r--')
axes2.set_ylabel('t^2')
axes2.plot(t,t**2,'bs')
axes3.set_ylabel('t^3')
axes3.plot(t,t**3,'g^')

fig.tight_layout()
plt.show()