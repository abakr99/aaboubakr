# E/M Ratio Script
# Calclulations and Data Anaylsis 

import numpy as np
import LT.box as b

# Voltage 150 Data Anaylsis and Calculations
# R = Radius of Coil
# r = Radius of Electron Path (r=D/2)

#%%
d_exp = b.get_file('V_400.data')
I = d_exp['I']
D = d_exp['D']*0.01
dD = d_exp['dD']*0.01

r= D/2
dr=dD/2
V = d_exp.par['Vol']
#%%
N = 132
D_cm = 29.5
mu0 = 4*np.pi*1.00e-7
R_cm = D_cm/2
R = R_cm*0.01

ec = 1.6e-19
me = 9.11e-31
rem_pub = ec/me

# Calculate the Magnetic Field (Bf)

def Bf(I, R, N):
    Bf = mu0*N*I/R * (4./5.)**1.5
    return Bf

# Calculate EM Ratio Rem

def Rem(I, Bf, r):
    Rem = 2*V/(Bf**2 * r**2)
    return Rem

B_exp = Bf(I,R,N)
R_em = Rem(I, B_exp, r)



#%%

sig_n = 0 
sig_V = 0.5
sig_I = 0.005
sig_R = 0.5*1e-2

#%% 

# Calculate Sigma B

def sig_bf(I):
    sig = (4/5)**(3/2) * mu0 * np.sqrt((I/R)**2 * sig_n**2 + (I*N/R*2)**2 * sig_R**2 + (N/R)**2 * sig_I**2)
    return sig


#%% 

# Calculate Uncertinty in B 


sig_B_exp = sig_bf(I)

# Calculate Uncertintiny in Rem

sig_rem = np.sqrt((2/(B_exp**2 * r**2))**2 * sig_V**2 + (4*V/(B_exp**3 * r**2)**2 * sig_B_exp**2 + (4*V/(B_exp**2 * r**3))**2 * dr**2))

#%% 

b.plot_exp(I, R_em, sig_rem) 
b.pl.xlabel('Current (I)')
b.pl.ylabel('Charge to Mass ratio')
b.pl.title('Charge to Mass Ratio as a Function of Current (150 V)')

#%% 

# Weighted Mean

def W_mean(X,sig):
    W = 1/(sig**2)
    S1 = np.sum(X*W)
    S2 = np.sum(W)
    Xmean = S1/S2
    Sig_Xmean = np.sqrt(1/(S2))
    return Xmean, Sig_Xmean

rem_mean, sig_remmean = W_mean(R_em, sig_rem)

ratio = rem_mean / rem_pub
uncertainty_ratio = (rem_mean - rem_pub) / sig_remmean




                                                                                          
