#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:12:47 2022

@author: ahmed
"""

import numpy as np
import LT.box as B

#%% 

lowcount = B.get_file('lowcount.data')
l_data = lowcount['Low']

def mean(X):
    mean = (1/200) * np.sum(X)
    return mean

print(mean(l_data))

def var(l_data):
    var = (1/(200-1)) * np.sum((l_data-mean(l_data)))**2
    return var 

print(var(l_data))


def set_range(first_bin = 0, bin_width = 1., Nbins = 10):
    rmin = first_bin -bin_width/2.
    rmax = rmin + Nbins*bin_width
    return (rmin,rmax)


lowcount_histo = B.histo(l_data, range = set_range(0.,1,5), bins = 10)
lowcount_histo.plot()


#%%

highcount = B.get_file('highcount.data')
h_data = highcount['High']

def mean(X):
    mean = (1/200) * np.sum(X)
    return mean

print(mean(h_data))

def set_range(first_bin = 150, bin_width = 10., Nbins = 10):
    rmin = first_bin -bin_width/2.
    rmax = rmin + Nbins*bin_width
    return (rmin,rmax)

highcount_histo = B.histo(h_data, range = set_range(0., 100, 170), bins = 11)
highcount_histo.plot()
