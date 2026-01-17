# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 11:07:40 2026

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt


E0 = 0 #onsite energy 影響能帶中心位置

k = np.linspace(-np.pi, np.pi)
t = 1
a = 1 
E1 = E0 -2*t* np.cos(k*a)

t1 = 5 
E2 = E0 -2*t1* np.cos(k*a)#E(k) = -2tcos(ka)


plt.figure(figsize=(8, 6),dpi=200)
plt.plot ( k, E1,color = 'blue', linewidth=2)
plt.plot ( k, E2,color = 'red', linewidth=2)
plt.xticks(ticks=[-np.pi , 0 , np.pi ], labels=['-π', '0', 'π'])
plt.xlabel("$ka$")
plt.ylabel("Energy (units of t)")
plt.title("1D Tight-Binding Band Structure")
plt.grid(True)
plt.show()
#補充
#hopping 越大 → 能帶越寬 → 電子越容易移動
#延伸Disorder  隨機 onsite energy看 band 展寬或破壞

