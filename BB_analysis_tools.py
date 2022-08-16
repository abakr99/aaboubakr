#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:49:49 2022

@author: boeglinw
"""

import numpy as np
import LT.box as B
from scipy import interpolate as INT

#%% photo-detector (PbS) spectral sensitiviy correction

class photo_sensor:
    def __init__(self, file, norm_int):
        """
        Initialize photo-sensor correction calculation

        Parameters
        ----------
        file : strip
            correction parameter file.
        norm_int : float numpy array
            current normalization spectrum

        Returns
        -------
        None.

        """
        # int_norm: normalization intensity distribution
        d = B.get_file(file)
        self.rd = d
        self.i_norm = d.par['i_norm']
        self.norm_int = norm_int[self.i_norm]
        self.offset_f = INT.interp1d(d['lambda'], d['offset'])
        self.slope_f = INT.interp1d(d['lambda'], d['slope'])
        

    def R_rel(self, x, lam):
        # relative intensity at wavelength lambda for a relative intensity x at the normalization wavelength
        o = self.offset_f(lam)
        m = self.slope_f(lam)
        return m*x + o
    
    def corr(self, l, int_exp):
        """
        calculate spectral correction factor

        Parameters
        ----------
        l : float array
            array of wavelength.
        int_exp : float array
            intensities to be corrected.
        int_norm : float
            normalization intensity at normalization wavelength.

        Returns
        -------
        float array
        Correction factors  correcting for spectral photo diode response

        """
        # relativ intensity at normalization wavelength
        i_rel = int_exp[self.i_norm]/self.norm_int  
        corr_fact = 1./self.R_rel(i_rel, l)
        return corr_fact
        
        
#%% W emissivity function
class W_em:
    def __init__(self, p_file='W_emissivity.data'):
        """
        Initialize emissivity calculation

        Parameters
        ----------
        p_file : string
            emissivity data file name (default = W_emissivity.data)

        Returns
        -------
        None.

        """
        d = B.get_file(p_file)
        self.d = d
        self.l_min = d['lmin']
        self.l_max = d['lmax']
        self.l0 = d['l0']
        self.a0 = d['a0']
        self.a1 = d['a1']
        self.b0 = d['b0']
        self.b1 = d['b1']
        self.b2 = d['b2']
        self.c0 = d['c0']
        self.c1 = d['c1']
        self.T0 = d.par.get_value('T0')
        self.calc = np.vectorize(self.em_s)
            
    def __call__(self, lam, T):
        return self.calc(lam, T)
    
        
    def em_s(self, lam,T):
        """
        Calulcate emissivity for a given wavelength and temperature

        Parameters
        ----------
        lam : float
            wavelength (nm).
        T : float
            temperature (K)

        Returns
        -------
        eps : float
            emissivity.

        """
        # get the correct range
        sel = (lam>=self.l_min) & (lam<self.l_max)
        if sel.max() == False:
            if lam < self.l_min[0]:
                sel[0] = True
            else:
                sel[-1] = True
        # get the parameters
        l0 = self.l0[sel][0]
        a0 = self.a0[sel][0]
        a1 = self.a1[sel][0]
        b0 = self.b0[sel][0]
        b1 = self.b1[sel][0]
        b2 = self.b2[sel][0]
        c0 = self.c0[sel][0]
        c1 = self.c1[sel][0]
        T0 = self.T0
        dT = (T - T0)/1000.
        dl = (lam - l0)/1000.
        self.dl = dl
        self.dT = dT
        self.l0_s = l0
        self.a0_s = a0
        self.a1_s = a1
        self.b0_s = b0
        self.b1_s = b1
        self.b2_s = b2
        self.c0_s = c0
        self.c1_s = c1
        eps = self.a0_s + self.a1_s*self.dT +\
            (self.b0_s + self.b1_s*self.dT + self.b2_s*self.dT**2)*self.dl + \
                (self.c0_s + self.c1_s*self.dT)*self.dl**2
        return eps


#%% read the ht text file
def get_ht(f):
    """
    Load LEOI-63 data file

    Parameters
    ----------
    f : string
        hr-file name.

    Returns
    -------
    float numpy array 
        array of wavelengths in nm.
    float numpy array
        array of measured intensities (arb. units).

    """
    header = "WL(nm)    Value"
    d = open(f).readlines()
    found = False
    r = []
    for l in d:
        if found:
            vs = l.split()
            r.append( [float(vs[0]), float(vs[1])])
            continue
        if (l.find(header) >= 0):
            found = True
        else:
            continue
    r = np.array(r)
    return r[:,0], r[:,1]
