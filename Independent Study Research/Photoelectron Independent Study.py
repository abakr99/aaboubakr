#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:09:48 2023

@author: ahmed
"""
#%%
import numpy as np
import LT.box as b
import ROOT as R
import bin_info3 as BI
from scipy.stats import poisson
from scipy.special import factorial
from scipy import optimize
import matplotlib.pyplot as plt

#%%
ec = 1.6e-4 # femto coulomb
tgate = 50e-9
#%%
data = b.get_file('Voltage vs Charge.data')
data.show_data('V:E')

V = data['V']
E = data['E']*1.0E+15

b.plot_exp(V, E)
fit = b.polyfit(V, E)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Charge (fC)')
b.pl.title('Total Charge as a Function of Voltage')
#%%
# Determine Charge from QDC Documentation CAEN Model V792 and Gain 

#Q = ((V)/(1000+50))*tgate
#gain = Q/I
G = (E*100)/(ec)

b.plot_exp(V,G)
fit1 = b.polyfit(V,G)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Gain')
b.pl.title('Gain as a Function of Voltage')
#%% Determine Logarithm from Power Law

b.pl.figure()
lG = np.log10(G)
lV = np.log10(V/1000)
b.plot_exp(lV,lG)
gf = b.linefit(lV,lG)
b.pl.xlabel('Logarithm Voltage (kV)')
b.pl.ylabel('Logarithm Gain')
b.pl.title('Logarithm Gain as a Function of Logarithm Voltage')



# E*100 goes to femto C
# Divide by ec

#%%
# Retake data from 1500 V to 2000 V see if graph's overlap

data2= b.get_file('Voltage vs Charge stack.data')
data2.show_data('V:E')

V2 = data2['V']
E2 = data2['E']

b.plot_exp(V2, E2)
fit = b.polyfit(V2, E2)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Charge (fC)')
b.pl.title('Total Charge as a Function of Voltage')

#%% Determine Charge of QDC from new data 

# inclV and incE are included values due to first 3 data points being 0

incV = data2['V'][3:]
incE = data2['E'][3:]

G2 = (incE*100)/(ec)

b.plot_exp(incV,G2)
fit2 = b.polyfit(incV,G2)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Gain')
b.pl.title('Gain as a Function of Voltage')

#%% Logarithm Gain 

b.pl.figure()
lG2 = np.log10(G2)
lV2 = np.log10(incV/1000)
b.plot_exp(lV2,lG2)
gf2 = b.linefit(lV2,lG2)
b.pl.xlabel('Logarithm Voltage (kV)')
b.pl.ylabel('Logarithm Gain')
b.pl.title('Logarithm Gain as a Function of Logarithm Voltage')

#%% Overlaping Charge vs Voltage
b.pl.figure()
b.plot_exp(V,E)
b.plot_exp(V2,E2)
b.polyfit(V,E)
b.polyfit(V2,E2)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Charge (fC)')
b.pl.title('Total Charge as a Function of Voltage')

#%% Overlaping Voltage vs Gain

b.pl.figure()
b.plot_exp(V, G)
b.plot_exp(incV,G2)
b.polyfit(V,G)
b.polyfit(incV,G2)
b.pl.xlabel('Voltage (V)')
b.pl.ylabel('Gain')
b.pl.title('Gain as a Function of Voltage')

#%% Overlaping Log Gain vs Log Voltage

b.pl.figure()
b.plot_exp(lV,lG)
b.plot_exp(lV2,lG2)
b.linefit(lV,lG)
b.linefit(lV2,lG2)
b.pl.xlabel('Logarithm Voltage (kV)')
b.pl.ylabel('Logarithm Gain')
b.pl.title('Logarithm Gain as a Function of Logarithm Voltage')

#%% Determine the Number of Single Photoelectrons 

hist_file = R.TFile('/Users/ahmed/Documents/Analysis/No Amplifier/adc15_488.root')
r_histo = hist_file.ha15

h = BI.get_histo_data(r_histo)
h.make_arrays()
hh = b.histo(bin_center= h.xb, bin_content= h.cont, filled = False,)
title = r_histo.GetName()
xl = (r_histo.GetXaxis()).GetTitle() 
hh.xlabel = xl
hh.title = title
#hh.plot_exp()
hh.plot(filled = False,ignore_zeros=True,)
#hh.fit()
#poisson(h.xb)
#hh.fit(174.,180.)
hh.fit(183.,187.)
#hh.fit(190.,193.)
#hh.fit(194.,198.)
#hh.plot_fit()


# noramlize histogram
hn = hn = hh/hh.sum()[0]

#%% Make bin content nonzero

nonzero = np.where(h.cont > 0)[0]
ran_min = h.xb[nonzero[0]]
ran_max = h.xb[nonzero[-1]+1]
range_bins = len(nonzero)
range = (ran_min, ran_max)

muv = ec * 1.5551875e+22




#%% Fit Function For Number of Photoelectrons 

mu = b.Parameter(0.000001,'mu' )

Q0 = b.Parameter(177.75988066198994, 'Q0')
sigma_Q0 = b.Parameter(1.1506974806961914, 'sigma_Q0')


Q1 = b.Parameter(8., 'Q1')
sigma_Q1 = b.Parameter(1., 'sigma_Q1')

w = b.Parameter(0.01,'w')
a = b.Parameter(1,'a')


N_max = 7
nr = np.arange(N_max)+1

#%%

mu.set(1.5)
sigma_Q0.set(0.8)
sigma_Q1.set(3.)


def P(x):
    return ((mu()**x)*np.exp(-mu()))/(factorial(x))


def Gp(x):
    g = np.exp(-(x-Q0())**2/(2*sigma_Q0()**2)) / (np.sqrt(2*np.pi)*sigma_Q0())
    return g


def Gn(x,n):
    Q_sh = w()/a()
    g = np.exp(-(x-Q_sh-Q0()-n*Q1())**2/(2*n*sigma_Q1()**2)) / (np.sqrt(2*np.pi*n)*sigma_Q1())
    return g



def bkg(x):
    bk = a()*np.heaviside(x - Q0(),1.) * np.exp(-a()*(x-Q0()))
    return bk


def S(x):
    ped =(  (1-w())*Gp(x)+w()*bkg(x) ) * np.exp(-mu())    # n= 0 contrbution
    #
    xx,nn = xx,nn = np.meshgrid(x,nr)  # meshgrid for n-range and x
    
    # calculate Poissons for n > 0
    Pc = P(nn)
    
    # calculate corresponding Gaussians
    Gc = Gn(xx,nn)
    
    # Product of Gauss and Poisson
    PG = Pc*Gc
    PGs = np.apply_along_axis(np.sum, 0, PG)
    
    return ped + PGs




#%% fit normalized histo
sel = b.in_between(150., 250., hn.bin_center)

xf = hn.bin_center[sel]
yf = hn.bin_content[sel]
dyf = hn.bin_error[sel]

w.set(0.1)

hn.set_window(150., 250.)
hn.plot(filled = False)

hf = b.genfit(S, [mu, Q0, Q1, sigma_Q0, sigma_Q1], xf , yf, dyf)

# b.plot_exp(xf, (hf.func(xf) - yf)/dyf, dyf/dyf)
    
#%%

# sum over Possons (nr)



scale_factor = 1500/ np.max(PGs)  # compute scaling factor
scaled_PGs = PGs * scale_factor  # apply scaling factor to PGs array

plt.plot(xv, scaled_PGs) 

plt.plot(xv, PGs)

#%%
def f(x):
    gauss = np.exp(-0.5*((x-x_ped())/sigma_ped())**2) / (np.sqrt(2*np.pi)*sigma_ped())
    poisson_sum = sum([np.exp(-((x-n*x_pe-x_ped)**2)/(4*n*(sigma_pe**2 - sigma_ped**2))) * lambd**(n-1) / (factorial(n-1)*n)
        for n in range(1, 10)
    ]) * N_evt / (np.sqrt(2*np.pi)*sigma_pe)
    return gauss + poisson_sum + np.exp(-(x-x_ped))

#def f(A_1,sig_ped,x_ped,sig_pe,x_pe,lambd,n,w,a):
   # fit = (1-w)((A_1)/(np.sqrt(2*np.pi)*sig_ped)) * math.exp(-((x-x_ped)/(sig_ped)))**2 + sum[((mu**2)math.exp(-mu))] * (N_evt)/((np.sqrt(2*np.pi))*(np.sqrt(n))*sig_pe) * math.exp(-((x-x_ped-(w/a)-n*(x_pe))**2)/(2*n*(sig_pe)**2))
  #  return fit
  
def f(x, A_1, sig_ped, x_ped, sig_pe, x_pe, lambd, n, w, a, N_evt):
    mu = lambd * n * (x_pe - x_ped - w/a)
    term1 = (1-w)*((A_1)/(np.sqrt(2*np.pi)*sig_ped)) * math.exp(-((x-x_ped)/(sig_ped))**2)
    term2 = sum([mu**2 * math.exp(-mu) for mu in range(N_evt)]) * (N_evt)/((np.sqrt(2*np.pi))*(np.sqrt(n))*sig_pe) * math.exp(-((x-x_ped-(w/a)-n*(x_pe))**2)/(2*n*(sig_pe)**2))
    fit = term1 + term2
    return fit

optimize.curve_fit(P,nonzero,mu)

#%%
hist_list = []

for i in range(482,503):
    root_file = f"/Users/ahmed/Documents/Analysis/No Amplifier/adc15_{i}.root"
    hist_file = R.TFile(root_file)
    r_histo = hist_file.ha15
    

    h = R.TH1F("h", "", r_histo.GetNbinsX(), r_histo.GetXaxis().GetXmin(), r_histo.GetXaxis().GetXmax())
    for j in range(1, r_histo.GetNbinsX()+1):
        h.SetBinContent(j, r_histo.GetBinContent(j))
        h.SetBinError(j, r_histo.GetBinError(j))
        hist_list.append(h)

for h in hist_list:
    fig, ax = plt.subplots()
    x = [h.GetBinCenter(i) 
         for i in range(1, h.GetNbinsX()+1)]
    y = [h.GetBinContent(i) 
         for i in range(1, h.GetNbinsX()+1)]
    ax.plot(x, y)
    ax.set_xlabel(h.GetXaxis().GetTitle())
    ax.set_ylabel("Counts")
    ax.set_title(h.GetName())
    plt.show()
    
#%% Method 3 Test

n_pe = np.array([0.182,0.260,0.319,0.373,0.548,0.729,0.833,0.997,1.336,1.650,1.892,2.194,2.552,2.589,2.882,3.332,3.756,4.102])
cores_V =np.array([1650,1700,1750,1800,1850,1900,1950,2000,2050,2100,2150,2200,2250,2300,2350,2400,2450,2500])
cores_kV = cores_V/1000
sig_n_pe = np.sqrt(n_pe)
np.std(n_pe)

b.plot_exp(cores_kV,n_pe)

#%% test of method 1 for 2100V 

A1 = 1.80006e+02
N_evt = 45045
#-ln(P_0) + ln(A_1) - ln(N_evt)
P_0 = A1/N_evt

np.log10(P_0)



    
#%%
        

    x = [h.GetBinCenter(i) for i in range(1, h.GetNbinsX()+1)]
    y = [h.GetBinContent(i) for i in range(1, h.GetNbinsX()+1)]
    plt.plot(x, y)
    plt.xlabel(h.GetXaxis().GetTitle())
    plt.ylabel("Entries")
    plt.title(r_histo.GetName())
    plt.show()