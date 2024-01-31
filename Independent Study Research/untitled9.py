#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:42:26 2023

@author: ahmed
"""

import numpy as np
import LT.box as B
import ROOT as R
from scipy.special import binom
from scipy.stats import norm as normal, poisson
import matplotlib.pyplot as plt

import bin_info3 as BI

hist_file = R.TFile('/Users/ahmed/Documents/Analysis/No Amplifier/adc15_488.root')
r_histo = hist_file.ha15

# convert root histo to LT.box histo
def get_1d_root_histo(r_histo):
    # get approriate histogram
    hr = BI.get_histo_data(r_histo)
    # make arrays with the correct shape
    hr.make_arrays()
    # make a histo2d
    hd = B.histo(bin_center = hr.xb, bin_content = hr.cont, bin_error = hr.dcont ) 
    # transfer the labels and title
    title = r_histo.GetName()
    xl = (r_histo.GetXaxis()).GetTitle() 
    hd.xlabel = xl
    hd.title = title
    return hd

#%%

h = BI.get_histo_data(r_histo)
h.make_arrays()
hh = B.histo(bin_center= h.xb, bin_content= h.cont, filled = False)
title = r_histo.GetName()
xl = (r_histo.GetXaxis()).GetTitle() 
hh.xlabel = xl
hh.title = title
#hh.plot_exp()
hh.plot(filled = True,)
hh.fit()
poisson(h.xb)
hh.fit(174.,180.)
hh.fit(183.,187.)
#hh.fit(190.,193.)
#hh.fit(194.,198.)
hh.plot_fit()

#%%

#mean = bin_centers * bin_content.sum() / bin_content.size
def poisson_distribution(mean_photoelectrons, num_events):
    photoelectrons = np.random.poisson(mean_photoelectrons, num_events)
    return photoelectrons



#%%

adc15_500 = R.TFile('/Users/ahmed/Documents/Analysis/No Amplifier/adc15_500.root')
adc15_500_hist = adc15_500.ha15

#%%

h1 = BI.get_histo_data(adc15_500_hist)
h1.make_arrays()
hh1 = B.histo(bin_center= h1.xb, bin_content= h1.cont,)
title = adc15_500.GetName()
xl = (r_histo.GetXaxis()).GetTitle() 
hh1.xlabel = xl
hh1.title = title
hh1.plot(filled = False)

#%% 

def get_2d_root_histo(r_histo):
    # get approriate histogram
    hb = BI.get_histo_data(r_histo)
    # make arrays with the correct shape
    hb.make_arrays(reshape = True)
    # make a histo2d
    hd2 = B.histo2d(x_bin_center = hb.xb[:,0], y_bin_center = hb.yb[0,:], bin_content = hb.cont, bin_error = hb.dcont ) 
    # transfer the labels and title
    title = r_histo.GetName()
    xl = (r_histo.GetXaxis()).GetTitle()
    yl = (r_histo.GetYaxis()).GetTitle()  
    hd2.xlabel = xl
    hd2.ylabel = yl
    hd2.title = title
    return hd2
#%%

sqrt2pi = np.sqrt(2.0 *np.pi)
K = np.arange(1,2100)

def pmt_spe_scipy(x,norm,eped,eped_sigma,spe,spe_sigma,lambda_):
    p_ped = np.exp(-lambda_)
    ped_signal = norm * p_ped * normal.pdf(x,eped,eped_sigma)
    
    p = poisson.pmf(K,lambda_)
    
    significant = p > 1e-5
    p_sig = p[significant]
    k_sig = K[significant]
    pe_sigma = np.sqrt(k_sig * spe_sigma ** 2 + eped_sigma ** 2)
    pe_signal = norm*p_sig*normal.pdf(x[:, None], eped + k_sig*spe, pe_sigma)
    return ped_signal + pe_signal.sum(1)

nonzero_cont = np.where(h.cont > 0)[0]

#%%

mean_photoelectrons = 193.1751569789477
k =45053
# Calculate the Poisson distribution of the data
x = np.arange(0, np.max(nonzero_cont)+1)
pmf = np.zeros(len(x))
pmf[k] = (mean_photoelectrons**k * np.exp(-mean_photoelectrons)) / np.math.factorial(k)

# Plot the Poisson distribution of the data
fig, ax = plt.subplots()
ax.bar(x, pmf)
ax.set_xlabel('Number of photoelectrons')
ax.set_ylabel('Probability')
ax.set_title('Poisson distribution of photoelectrons from actual data')
plt.show()