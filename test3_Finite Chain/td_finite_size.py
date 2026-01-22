# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:45:14 2026

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt


E0 = 0 #onsite energy 影響能帶中心位置


t = 1 #hopping
N = 10 #number of lattice sites ,system size or chain length
n = np.arange(1,N) #能階編號energy level(量子數)
theta = np.linspace( 0,np.pi) #連續
theta_n = n*np.pi/(N + 1) #不連續

#finite
En = E0 - 2*t* np.cos(theta_n) #色散關係(不連續) E(k) = E0-2tcos(θ)

#infinite
E_ift = E0 -2*t* np.cos(theta) # 色散關係(連續)


plt.figure(figsize=(8, 6),dpi=200)
plt.scatter( theta_n, En, label=r"$E_n$" ,color = 'blue', linewidth=2)
plt.plot( theta , E_ift,label=r"$E_∞$",color = 'red', linewidth=2)
plt.xlabel("$Energy \ level$")
plt.ylabel("Energy (units of t)")
plt.title("1D Tight-Binding Energy Spectrum (Finite Chain, N = 10)") #Energy Spectrum 能譜
plt.grid(True)
plt.legend()
plt.show()