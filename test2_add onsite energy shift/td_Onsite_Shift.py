# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:47:20 2026

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt


E0 = 0 #onsite energy 影響能帶中心位置
E01 = 2

k = np.linspace(-np.pi, np.pi)
t = 1 #hopping
a = 1 #unit lattice
E1 = E0 -2*t* np.cos(k*a) #色散關係

 
E2 = E01 -2*t* np.cos(k*a)#E(k) = -2tcos(ka)


plt.figure(figsize=(8, 6),dpi=200)
plt.plot ( k, E1, label=r"$E_0=0$" ,color = 'blue', linewidth=2)
plt.plot ( k, E2,label=r"$E_0=2$",color = 'red', linewidth=2)
plt.xticks(ticks=[-np.pi , 0 , np.pi ], labels=['-π', '0', 'π'])
plt.xlabel("$ka$")
plt.ylabel("Energy (units of t)")
plt.title("1D Tight-Binding Band Structure: Onsite Energy Shift")
plt.grid(True)
plt.legend()
plt.show()
#補充
#更改中心位置不影響其bandwidth