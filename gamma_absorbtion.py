#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:03:57 2022

@author: ahmed
"""

import numpy as np
import LT.box as B
#%%
fl = B.get_file('f_name.data')

delta_t = fl.par['integration_time']
file_list = fl['file_name']
N_p = fl['N_pb']
#%%
all_histos =[]
counts = []
sig_counts = []
#%%
for i,d in enumerate(file_list):
    
    print(f"File {d}: Contains {i} abosorber plates")
#%%
for i,d in enumerate(file_list):
    sp = B.get_spectrum(d)
    all_histos.append(sp)
#%%
for h in all_histos:
    C, dc = h.sum(250,350)
    counts.append(C)
    sig_counts.append(dc)
#%%

B.pl.figure()
all_histos[0].plot(), all_histos[6].plot(), all_histos[8].plot()
#%%

counts = np.array(counts)
sig_counts = np.array(sig_counts)

#%%

R = counts/delta_t
sig_R = sig_counts/delta_t

#%%

B.plot_exp(R,sig_R)
B.pl.xlabel('Number of Plates')
B.pl.ylabel('Counts/s')
B.pl.title('Absorption of 0.617 MeV gamma rays in Pb')
#%%

sel = N_p>=0

#%%

counts_c = counts-counts[-1]

#%%

sig_counts_c = np.sqrt((sig_counts)**2 + sig_counts[-1]**2)

#%%

C = counts_c[sel]
dC = sig_counts[sel]
N = N_p[sel]

#%%

lnC = np.log(C)

#%%

dlnC = 1/C * dC

#%%

B.plot_exp(lnC,N,dlnC)

#%%

abs_fit = B.linefit(lnC,N,dlnC)

#%%

mu = abs_fit.slope
sig_mu = abs_fit.sigma_s

print(f'mu = {mu:.2e} +/- {sig_mu:.2e}')

#%% 

X_12 = -(np.log(2)/mu)

#%%

sig_X_12 = (np.log(2)/(mu)**2)*sig_mu