#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:19:05 2022

@author: ahmed
"""
#%% Import Modules
import numpy as np
import LT.box as B

#%% 
def peakpos(h):

   x1, x2 = B.pl.xlim()
   h.fit(x1,x2)
   h.plot_fit()
   return h.mean.value, h.mean.err

#%% Callibration Data BA 133

cba133 = B.get_spectrum('callibration BA133.Spe')
                        
cba133.plot()

peakcba133 = peakpos(cba133)

#%% Array for BA 133 

Bacpeak = np.array([14.080949391559628, 36.144781582788326, 148.21879193689495])
Bacenergy = np.array([0.031, 0.081, 0.356])


#%% Callibration Data CO 60

co60 = B.get_spectrum('callibration CO60.Spe')
co60.plot()
peakco60 = peakpos(co60)

#%% Array for Co

Co60peak = np.array([465.09921096778197, 526.5163635496415])
Coenergy = np.array([1.1732, 1.3325])


#%% Callibration Data Cs 137

c_Cs137 = B.get_spectrum('callibration CS137.Spe')
c_Cs137.plot()

#%% Array for Cs 137

Cspeak = np.array([268.72193314534877])
Csenergy = np.array([0.6617])

#%% Combine all Callibrations into fit 

allpos = np.array(list(Bacpeak)+list(Co60peak)+list(Cspeak))
alle = np.array(list(Bacenergy)+list(Coenergy)+list(Csenergy))

B.plot_exp(allpos,alle)
call = B.linefit(allpos,alle)

#%% 30 Degrees 

sp30_t = B.get_spectrum('30degrees.Spe', calibration = call)
sp30_e = B.get_spectrum('30degrees_without.spe', calibration = call)
sp30 = sp30_t - sp30_e
pos_30 = 0.5616352102918551

#%% 40 Degrees

sp40_t = B.get_spectrum('40degrees.Spe', calibration = call)
sp40_e = B.get_spectrum('40degrees_without.Spe', calibration = call)
sp40 = sp40_t - sp40_e
pos_40 = 0.5116529159120623

#%% 60 Degrees

sp60_t = B.get_spectrum('60degrees.Spe', calibration = call)
sp60_e = B.get_spectrum('60degrees_without.Spe', calibration = call)
sp60 = sp60_t - sp60_e 
pos_60 = 0.4070034712037666

#%% 80 Degrees

sp80_t = B.get_spectrum('80degrees.Spe', calibration = call)
sp80_e = B.get_spectrum('80degrees_without.Spe', calibration = call)
sp80 = sp80_t - sp80_e
pos_80 = 0.33328754341179156

#%% 100 Degrees

sp100_t = B.get_spectrum('100degrees.Spe', calibration = call)
sp100_e = B.get_spectrum('100degrees_without.Spe', calibration = call)
sp100 = sp100_t - sp100_e
pos_100 = 0.2677537485449891

#%% 120 Degrees

sp120_t = B.get_spectrum('120degrees.Spe', calibration = call)
sp120_e = B.get_spectrum('120degrees_without.Spe', calibration = call)
sp120 = sp120_t - sp120_e
pos_120 = 0.2286631544457761

#%% Ratio E0/Ef

E0 = 0.6617
Ef = np.array([0.5613829517503356,0.5117652185652376,0.40685557336007827,0.3322373777827937,0.26703983208498533,0.2289693120976159])
sig_ef = np.array([0.001,0.001,0.001,0.001,0.001,0.001])
theta = [0.523599,0.698132,1.0472,1.39626,1.74533,2.0944]
cos = (1-np.cos(theta))

ratio_plot = B.plot_exp(cos, E0/Ef)
lf = B.linefit(cos, E0/Ef)
M = E0/1.2534628222003183


