#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:04:40 2022

@author: ahmed
"""

#%% Import Modules
import numpy as np
import LT.box as B 

#%% Get Data file 

one = B.get_file('1storder.data')
two = B.get_file('2ndorder.data')
Angle1 = one['Angle']
Angle2 = two['Angle']

#%% Angles

thetaa= 2.70642389
theta0= 2.20871417

thetain = ((theta0-thetaa)/2)

#thetaout = (Angle1)-((thetaa+theta0)/2)
thetaout = (Angle1)-((thetaa+thetain))

D=(1/1200)*1e-3
#%% Path Length

delta1 = D*np.cos(thetain)
delta2= D*np.cos(thetaout)
deltatot = delta1-delta2
#%% Convert Wavelength

m_d = [-2,-1,1,2]
def lam(D,Angle,m_d):
   return (D*np.sin(Angle)/m_d)

lam(D,Angle1,m_d)
 
lam = deltatot/m_d 

B.plot_line(Angle1,Angle2)

#%% Calculate Wavelength Uncertainty

sigin = 0.0090
sigout = 0.0090

sig_lam = np.sqrt((-D*np.sin(thetain)**2)*(sigin)**2+(D*np.sin(thetaout)**2)*(sigout)**2)

#%% Calculate Energy 

h = 6.626e-34
c = 2.99e8
E = (h*c)/(lam)

#%% Calculate Energy Uncertainity 

sig_e = np.sqrt((h*c)/((lam)**2)*(sig_lam)**2)

#%% Plot 1/lam
n = [1,2,3]
n_2 = np.array([2,3,4,5])
lam_1 = 1/np.sort((np.abs(lam)))
#n = np.array(m_d)
#n= np.array(n)
#n_2 = np.array(n_2)
#n_1 = 1/((n_2**2))

B.plot_exp(1 - (1/((n_2)**2)), lam_1[::-1])
B.linefit(1 - (1/((n_2)**2)), lam_1[::-1])
