#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:31:29 2022

@author: ahmed
"""
#%% Import Modules

import numpy as np
import LT.box as B
import BB_analysis_tools as BBT

#%% knowns

h = 6.6266e-34
c = 2.99e8
k = 1.38e-23
nm = 1e-9

#%% Make a plot of lamp temp as a function of current 

lamp = B.get_file('lamp.data')
temp = lamp['Temp']
current = lamp['Current']
lamp_plot = B.plot_line(current,temp)

#%% Fit a second order polynomial to lamp temperature as a function of current.

ployfit = B.polyfit(current,temp,2)

#%% Load the normalization file (the first data set at a current setting of 2.50A) and store the wavelength and Intensities in arrays called e.g. lam_norm and I_norm

l_norm, I_norm = BBT.get_ht('normalization.ht')

normplot = B.plot_line(l_norm, I_norm)

#%% Initialize the emissivity calculation 

em = BBT.W_em()

#%% Program the black body spectrum

def B_lt(ll,t):
    l = ll*nm
    y = (2*h*c**2)/((l**5)*(np.e**((h*c)/(l*k*t))-1))*nm
    return y

#%% Calculate the black-body spectrum for the normalization temperature

I_calc = B_lt(l_norm,2940)

#%% Calculate the emissivity  for the given temperature and wavelengths using the function em as follows:
    
em_norm = em(l_norm, 2940)
f_tr = em_norm*I_calc/I_norm

#%% 

l_exp123,I_exp123 = BBT.get_ht('1.23A.ht')
l_exp145, I_exp145 = BBT.get_ht('1.45A.ht')
l_exp167, I_exp167 = BBT.get_ht('1.67A.ht')
l_exp188, I_exp188 = BBT.get_ht('1.88A.ht')
l_exp210, I_exp210 = BBT.get_ht('2.10A.ht')
l_exp232, I_exp232 = BBT.get_ht('2.32A.ht')


I_exp_corr123 = I_exp123*f_tr
I_exp_corr145 = I_exp145*f_tr
I_exp_corr167 = I_exp167*f_tr
I_exp_corr188 = I_exp188*f_tr
I_exp_corr210 = I_exp210*f_tr
I_exp_corr232 = I_exp232*f_tr

#%% Initialize the calculation using the photo_sensor class

PD = BBT.photo_sensor('R_parameters.data', I_norm)

#%% Calculate the sensitivity correction factors

p_corr210 = PD.corr(l_exp210, I_exp210)
p_corr123 = PD.corr(l_exp123, I_exp123)
p_corr145 = PD.corr(l_exp145, I_exp145)
p_corr167 = PD.corr(l_exp167, I_exp167)
p_corr188 = PD.corr(l_exp188, I_exp188)
p_corr232 = PD.corr(l_exp232, I_exp232)


#%% Multiply the spectrum by the transfer function f_tr and the sensitivity correction factor p_corr

I_exp210corr = I_exp_corr210 * p_corr210
I_exp123corr = I_exp_corr123 * p_corr123
I_exp145corr = I_exp_corr145 * p_corr145
I_exp167corr = I_exp_corr167 * p_corr167
I_exp188corr = I_exp_corr188 * p_corr188
I_exp232corr = I_exp_corr232 * p_corr232

#%% Model the lamp spectrum and fit it to the measured and corrected spectrum for any lamp current

lampspec210 = B.plot_line(l_exp210, I_exp210corr)
lampspec123 = B.plot_line(l_exp123, I_exp123corr)
lampspec145 = B.plot_line(l_exp145, I_exp145corr)
lampspec167 = B.plot_line(l_exp167, I_exp167corr)
lampspec188 = B.plot_line(l_exp188, I_exp188corr)
lampspec232 = B.plot_line(l_exp232, I_exp232corr)

#%% Setup Paramenter

T_f = B.Parameter(2000.,'T_f')
A = B.Parameter(0.6,'A')

#%% Write a fit function called I_fit 

def B_lt_fit(ll):
    l = ll*nm
    em_l = em(ll, T_f())
    y = (2*h*c**2)/((l**5)*(np.e**((h*c)/(l*k*T_f()))-1))*A()*nm*em_l
    return y

sel = l_exp210>830
I_fit = B.genfit(B_lt_fit,[T_f,A],x = l_exp210[sel], y = I_exp210corr[sel])
B.plot_exp(l_exp210[sel], I_exp210corr[sel])

#%% Fit your corrected spectra, make a plot of the data and the fit and store the fit parameters in a list.

sel = l_exp210>830
I_fit_123 = B.genfit(B_lt_fit,[T_f,A],x = l_exp123[sel], y = I_exp123corr[sel])
B.plot_exp(l_exp123[sel], I_exp123corr[sel])

a_123 = A.value;T_f123 = T_f.value


I_fit_145 = B.genfit(B_lt_fit,[T_f,A],x = l_exp145[sel], y = I_exp145corr[sel])
B.plot_exp(l_exp145[sel], I_exp145corr[sel])
a_145 = A.value;T_f145 = T_f.value

I_fit_167 = B.genfit(B_lt_fit,[T_f,A],x = l_exp167[sel], y = I_exp167corr[sel])
B.plot_exp(l_exp167[sel], I_exp167corr[sel])
a_167 = A.value;T_f167 = T_f.value


I_fit_188 = B.genfit(B_lt_fit,[T_f,A],x = l_exp188[sel], y = I_exp188corr[sel])
B.plot_exp(l_exp188[sel], I_exp188corr[sel])
a_188 = A.value;T_f188 = T_f.value

I_fit_210 = B.genfit(B_lt_fit,[T_f,A],x = l_exp210[sel], y = I_exp210corr[sel])
B.plot_exp(l_exp210[sel], I_exp210corr[sel])
a_210 = A.value;T_f210 = T_f.value

I_fit_232 = B.genfit(B_lt_fit,[T_f,A],x = l_exp232[sel], y = I_exp232corr[sel])
B.plot_exp(l_exp232[sel], I_exp232corr[sel])
a_232 = A.value;T_f232 = T_f.value

#%% Wiens Law 

B_exp123 = I_exp123corr / (a_123 * em(l_exp123,T_f123))
B_exp145 = I_exp145corr / (a_145 * em(l_exp145,T_f145))
B_exp167 = I_exp167corr / (a_167 * em(l_exp167,T_f167))
B_exp188 = I_exp188corr / (a_188 * em(l_exp188,T_f188))
B_exp210 = I_exp210corr / (a_210 * em(l_exp145,T_f210))
B_exp232 = I_exp232corr / (a_232 * em(l_exp232,T_f232))

#%% Numerical Integration

int_123 = np.diff(l_exp123)[0]*B_exp123.sum()
int_145 = np.diff(l_exp145)[0]*B_exp145.sum()
int_167 = np.diff(l_exp167)[0]*B_exp167.sum()
int_188 = np.diff(l_exp188)[0]*B_exp188.sum()
int_210 = np.diff(l_exp210)[0]*B_exp210.sum()
int_232 = np.diff(l_exp232)[0]*B_exp232.sum()

#%% Plot Logarithm 

T_f = np.array([T_f123,T_f145,T_f167,T_f188,T_f210,T_f232])
p_tot = np.array([int_123,int_145,int_167,int_188,int_210,int_232])
log_T = np.log(T_f)
log_p = np.log(p_tot)
log_plot = B.plot_exp(log_T,log_p)
steph_fit = B.linefit(log_T,log_p)

#%% 
ll = np.linspace(0.1, 10000,10000)
ssl_l = ll<830
ssl_u = 2500<ll
ssl_mid = (~ssl_l)&(~ssl_u)

# T_l = 2500
f_corr = []
for T_l in T_f:
    bb_s = B_lt(ll,T_l)
    dl = np.diff(ll)[0]
    int_l = (bb_s[ssl_l]*dl).sum()
    int_u = (bb_s[ssl_u]*dl).sum()
    int_m = (bb_s[ssl_mid]*dl).sum()
    int_tot = int_l + int_u + int_m
    f_corr.append(int_tot/int_m)
    
f_corr = np.array(f_corr)

ptot_corr = p_tot * f_corr

log_p = np.log(ptot_corr)
log_plot = B.plot_exp(log_T,log_p)
steph_fit = B.linefit(log_T,log_p)




