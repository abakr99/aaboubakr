#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:20:00 2021

@author: boeglinw
"""

import numpy as np
import LT.box as B
import ROOT as R

import bin_info3 as BI


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
