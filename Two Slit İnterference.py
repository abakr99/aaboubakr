#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:14:37 2022

@author: ahmed
"""
#%%İmport Modules
import numpy as np
import LT.box as B
import LT_Fit.parameters as p
import LT_Fit.gen_fit as g

#%%

lam = 670e-9
L = 500
D = B.Parameter(0.1e-3, 'D') 
S = B.Parameter(0.5e-3, 'S')
x0 = B.Parameter(3.4, 'x0')
I0 = B.Parameter(1., 'I0')


#%% Get data file Single Slit Right and plot
single_right = B.get_file('Single Slit Right.data')
rposition = single_right['Position']
rvoltage = single_right['Voltage']
sl = rposition<9.5
rp = rposition[sl]
rv = rvoltage[sl]
rvn = rv/rv.max()
rplot = B.plot_exp(rp, rvn)
#B.plot_line(rp, rvn)


#%% Get Data file Double Slit and plot
double = B.get_file('Double Slit.data')
dposition = double['Position']
dvoltage = double['Voltage']
dl = (.4<dposition) & (dposition<9)
dp = dposition[dl] + np.pi * 1e-12
dv = dvoltage[dl]
dvn = dv/dv.max()
dplot = B.plot_line(dp, dv)
dplote = B.plot_exp(dp, dv)

#%% Get Data file Single Slit Left and plot
single_left = B.get_file('Single Slit Left.data')
lposition = single_left['Position']
lvoltage = single_left['Voltage']
sr = lposition<9.5
lp = lposition[sr]
lv = lvoltage[sr]
lvn = lv/lv.max()
lplot = B.plot_exp(lp, lv)
#B.plot_line(lp, lv)
#%% Convert position to viewing angle

#%% Single Slit Viewing Angle

def Is(x):
    th = (x-x0())/L
    phi = 2*np.pi/lam*D()*np.sin(th)
    I = I0()*(np.sin(phi/2)/(phi/2))**2
    return I

#%% Fit right single slit

rplot = B.plot_exp(rp, rvn)
r_fit = B.genfit(Is,[D,x0,I0], x = rp, y = rvn)
print(f'Right Slit Witdth = {D}')
B.pl.title('Intensity as a Function of Viewing Angle Right Single Slit')
B.pl.xlabel('Position (mm)')
B.pl.ylabel('Intensity (Theta)')

#%% Fit Left Slit

rplot = B.plot_exp(lp, lvn)
r_fit = B.genfit(Is,[D,x0,I0], x = rp, y = lvn)
print(f'Left Slit Witdth = {D}')
B.pl.title('Intensity as a Function of Viewing Angle Left Single Slit')
B.pl.xlabel('Position (mm)')
B.pl.ylabel('Intensity (Theta)')


#%% Double Slit Fit

def Intensity(x):
    k = 2.*np.pi/lam                
    phi = k*D()*np.sin((x-x0())/L)
    psi = k*S()*np.sin((x-x0())/L)
    I = I0()*(np.sin(phi/2.)/(phi/2.))**2 * np.cos(psi/2.)**2
    return I 

#%%
B.plot_exp(dp, dvn)
B.plot_line(dp, dvn)
dxt = np.linspace(dp.min(),dp.max(), 1000) 
x0.set(4.3)
D.set(0.8e-4)  
S.set(3.1e-4)  
B.plot_line(dxt, Intensity(dxt))
#%%
d_fit = g.genfit(Intensity, [D,S,x0,I0] , x= dp, y= dvn, plot_fit = False)
B.plot_exp(dp, dvn)
B.plot_line(dxt, Intensity(dxt))
print(f'Double Slit Witdth = {D}')
B.pl.title('Intensity as a Function of Viewing Angle Double Slit')
B.pl.xlabel('Position (mm)')
B.pl.ylabel('Intensity (Theta)')


