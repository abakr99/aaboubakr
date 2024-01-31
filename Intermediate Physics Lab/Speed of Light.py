#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:46:58 2022

@author: ahmed
"""

#%% Import Modules
import numpy as np
import LT.box as B

#%% conversion factor
mm_2_m = 1e-2

#%% From the position measurements subtract the position for zero (or very slow) rotation

cw = B.get_file('Clockwise.data')
ccw = B.get_file('Counter.data')
cposition = cw['Position']*mm_2_m
cfreq = cw['Frequency']
omegac = 2*np.pi*cfreq
ccwposition = ccw['Position']
ccwfreq = ccw['Frequency']
omegaccw = 2*np.pi*ccwfreq

#%% Parameters

D1 = 7.5819
D2 = 7.49427
f2 = 0.255
sig_cpos = np.ones_like(cposition)*0.002*mm_2_m
c_pub = 3e8
sig_ccwpos = np.ones_like(ccwposition)*0.002*mm_2_m

#%% Plot the measured x  as a function of w. Select different signs for CW and CCW rotation.

plot1 = B.plot_exp(omegac,cposition,sig_cpos)
cfit = B.linefit(omegac,cposition,sig_cpos)
d_tot = D1 + D2
c_c = (4*f2*d_tot)/cfit.slope
sig_c_c = c_c/cfit.slope*cfit.sigma_s

sig_c = np.sqrt((4*(d_tot)/c_c*0.001)**2+(4*f2*(1+D2)/c_c*0.001)**2+(4*f2*(1+D1)/c_c*0.001)**2+(4*(d_tot)/(c_c)**2*0.001)**2)

#%% Counter Clockwise
plot2 = B.plot_exp(omegaccw,ccwposition,sig_ccwpos)
ccwfit = B.linefit(omegaccw,ccwposition,sig_ccwpos)
c_ccw = (4*f2*d_tot)/ccwfit.slope
sig_ccw = np.sqrt((4*(d_tot)/c_ccw*0.001)**2+(4*f2*(1+D2)/c_c*0.001)**2+(4*f2*(1+D1)/c_ccw*0.001)**2+(4*(d_tot)/(c_ccw)**2*0.001)**2)

deltac = cposition - cposition[0]
deltaccw = ccwposition - cposition[0]

deltacplot = B.plot_exp(deltac, omegac)
detlaccwplot = B.plot_exp(deltaccw,ccwfreq)
#%% rearange deltax

c_cw = ((4*cfreq*f2*D1)/deltac)+((4*cfreq*f2*D2)/deltac)
c_ccw = ((4*ccwfreq*f2*D1)/deltaccw)+((4*ccwfreq*f2*D2)/deltaccw)

c_cw1 = np.array(c_cw[1:10])

c_cw1mean = np.mean(c_cw1)
c_ccwmean = np. mean(c_ccw)