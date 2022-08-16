#%%Photo-Electric Effect Lab

import numpy as np
import LT.box as B

#%%yellow
#get data
fy=B.get_file("Yellow.data")
Vy=B.get_data(fy,"V")
Iy=B.get_data(fy,"I")
#%% scatter plot
y_plot = B.plot_exp(Vy,Iy,.01, plot_title="Yellow (578nm)",x_label="Voltage (V)", y_label="Current, I (mA)")
#%% Set limits & fit line
r1=B.in_between(1.25, 3.5, Vy)
r2=B.in_between(.5, .7, Vy)
r3=B.in_between(.6, .8, Vy)
l1=B.linefit(Vy[r1], Iy[r1],)
l2=B.linefit(Vy[r2], Iy[r2],)
l3=B.linefit(Vy[r3], Iy[r3],)
#%% Extend linefits using y = mx + b
Ext_x1=np.array([.25, 1.0, 1.5]) #x values for extended line 1
Ext_y1=l1.slope*Ext_x1+l1.offset    #extended line 1
Ext_x2=np.array([.6, .5, .7])
Ext_y2=l2.slope*Ext_x2+l2.offset
Ext_x3=np.array([.5, .75, 1.0])
Ext_y3=l3.slope*Ext_x3+l3.offset
# %%Plot fitted and extended lines
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5) #line 1
B.plot_line(l2.xpl,l2.ypl, color="green", linewidth=.5)
B.plot_line(l3.xpl,l3.ypl, color="black",linewidth=.5)
B.plot_line(Ext_x1,Ext_y1,color="blue", linewidth=.5) #extended 1
B.plot_line(Ext_x2,Ext_y2, color="green", linewidth=.5)
B.plot_line(Ext_x3,Ext_y3, color="black", linewidth=.5)
B.pl.show()
#%% Calculate V at the intersect point of extended lines 1 and 2
V_stopL=(l1.offset-l2.offset)/(l2.slope-l1.slope)
V_stopR=(l1.offset-l3.offset)/(l3.slope-l1.slope)
Vsy=(V_stopL+V_stopR)/2
print("V stop(y) = ", Vsy)
#%% for second(higher) intercept
V_stopLy=V_stopL


#%% green
#get data
fg=B.get_file("Green.data")
Vg=B.get_data(fg,"V")
Ig=B.get_data(fg,"I")
#%% scatter plot
B.plot_exp(Vg,Ig,.01, plot_title="Green (546nm)",x_label="Voltage (V)", y_label="Current, I (mA)")
#%% Set limits & fit line
r1=B.in_between(1.25, 3.5, Vg)
r2=B.in_between(.65, .75, Vg)
r3=B.in_between(.8, .9, Vg)
l1=B.linefit(Vg[r1], Ig[r1],)
l2=B.linefit(Vg[r2], Ig[r2],)
l3=B.linefit(Vg[r3], Ig[r3],)
#%%Extend linefits using y = mx + b
Ext_x1=np.array([.5, 1.0, 1.5]) #x values for extended line 1
Ext_y1=l1.slope*Ext_x1+l1.offset    #extended line 1
Ext_x2=np.array([.5, .7, .9])
Ext_y2=l2.slope*Ext_x2+l2.offset
Ext_x3=np.array([.5, .75, 1.0])
Ext_y3=l3.slope*Ext_x3+l3.offset

#%%Plot fitted and extended lines
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5) #line 1
B.plot_line(l2.xpl,l2.ypl, color="green", linewidth=.5)
B.plot_line(l3.xpl,l3.ypl, color="black",linewidth=.5)
B.plot_line(Ext_x1,Ext_y1,color="blue", linewidth=.5) #extended 1
B.plot_line(Ext_x2,Ext_y2, color="green", linewidth=.5)
B.plot_line(Ext_x3,Ext_y3, color="black", linewidth=.5)
B.pl.show()

#%% Calculate V at the intersect point of extended lines 1 and 2

V_stopL=(l1.offset-l2.offset)/(l2.slope-l1.slope)
V_stopR=(l1.offset-l3.offset)/(l3.slope-l1.slope)
Vsg=(V_stopL+V_stopR)/2
print("V stop(g) = ", Vsg)

#%% for second(higher) intercept
#V_stopLg=V_stopL

#%% blue
#get data
fb=B.get_file("Blue.data")
Vb=B.get_data(fb,"V")
Ib=B.get_data(fb,"I")
#%% scatter plot
B.plot_exp(Vb,Ib,.01, plot_title="Blue (436nm)",x_label="Voltage (V)", y_label="Current, I (mA)")
#%% Set limits & fit line

r1=B.in_between(2., 3.5, Vb)
r2=B.in_between(1.2, 1.4, Vb)
r3=B.in_between(1.4, 1.7, Vb)
l1=B.linefit(Vb[r1], Ib[r1],)
l2=B.linefit(Vb[r2], Ib[r2],)
l3=B.linefit(Vb[r3], Ib[r3],)
#%% Extend linefits using y = mx + b
Ext_x1=np.array([1.25, 1.75, 2.]) #x values for extended line 1
Ext_y1=l1.slope*Ext_x1+l1.offset    #extended line 1
Ext_x2=np.array([1.2, 1.25, 1.6])
Ext_y2=l2.slope*Ext_x2+l2.offset
Ext_x3=np.array([1.25, 1.6, 1.8])
Ext_y3=l3.slope*Ext_x3+l3.offset

#%% Plot fitted and extended lines
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5) #line 1
B.plot_line(l2.xpl,l2.ypl, color="green", linewidth=.5)
B.plot_line(l3.xpl,l3.ypl, color="black",linewidth=.5)
B.plot_line(Ext_x1,Ext_y1,color="blue", linewidth=.5) #extended 1
B.plot_line(Ext_x2,Ext_y2, color="green", linewidth=.5)
B.plot_line(Ext_x3,Ext_y3, color="black", linewidth=.5)
B.pl.show()

#%% Calculate V at the intersect point of extended lines 1 and 2
V_stopL=(l1.offset-l2.offset)/(l2.slope-l1.slope)
V_stopR=(l1.offset-l3.offset)/(l3.slope-l1.slope)
Vsb=(V_stopL+V_stopR)/2
print("V stop(b) = ", Vsb)

#%% for second(higher) intercept
V_stopLb=V_stopL

#%% violet
#get data
fv=B.get_file("Violet.data")
Vv=B.get_data(fv,"V")
Iv=B.get_data(fv,"I")

#%% scatter plot
B.plot_exp(Vv,Iv,.01, plot_title="Violet (405nm)",x_label="Voltage (V)", y_label="Current, I (mA)")

#%% Set limits & fit line
r1=B.in_between(2., 3.5, Vv)
r2=B.in_between(1.2, 1.4, Vv)
r3=B.in_between(1.4, 1.7, Vv)
l1=B.linefit(Vv[r1], Iv[r1],)
l2=B.linefit(Vv[r2], Iv[r2],)
l3=B.linefit(Vv[r3], Iv[r3],)

#%% Extend linefits using y = mx + b
Ext_x1=np.array([1.25, 1.75, 2.4]) #x values for extended line 1
Ext_y1=l1.slope*Ext_x1+l1.offset    #extended line 1
Ext_x2=np.array([1.2, 1.25, 1.6])
Ext_y2=l2.slope*Ext_x2+l2.offset
Ext_x3=np.array([1.25, 1.6, 1.8])
Ext_y3=l3.slope*Ext_x3+l3.offset

#%% Plot fitted and extended lines
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5) #line 1
B.plot_line(l2.xpl,l2.ypl, color="green", linewidth=.5)
B.plot_line(l3.xpl,l3.ypl, color="black",linewidth=.5)
B.plot_line(Ext_x1,Ext_y1,color="blue", linewidth=.5) #extended 1
B.plot_line(Ext_x2,Ext_y2, color="green", linewidth=.5)
B.plot_line(Ext_x3,Ext_y3, color="black", linewidth=.5)
B.pl.show()

#%% Calculate V at the intersect point of extended lines 1 and 2
V_stopL=(l1.offset-l2.offset)/(l2.slope-l1.slope)
V_stopR=(l1.offset-l3.offset)/(l3.slope-l1.slope)
Vsv=(V_stopL+V_stopR)/2
print("V stop(v) = ", Vsv)

#%% for second(higher) intercept
V_stopLv=V_stopL
    
#%% UV
#get data
fu=B.get_file("UV.data")
Vu=B.get_data(fu,"V")
Iu=B.get_data(fu,"I")
#%% scatter plot
B.plot_exp(Vu,Iu,.01, plot_title="UV (365nm)",x_label="Voltage (V)", y_label="Current, I (mA)")
#%% Set limits & fit line

r1=B.in_between(2.25, 3.5, Vu)
r2=B.in_between(1.5, 1.8, Vu)
r3=B.in_between(1.7, 1.9, Vu)
l1=B.linefit(Vu[r1], Iu[r1],)
l2=B.linefit(Vu[r2], Iu[r2],)
l3=B.linefit(Vu[r3], Iu[r3],)

#%% Extend linefits using y = mx + b
Ext_x1=np.array([1.6, 1.8, 2.3]) #x values for extended line 1
Ext_y1=l1.slope*Ext_x1+l1.offset    #extended line 1
Ext_x2=np.array([1.8, 1.9, 2.])
Ext_y2=l2.slope*Ext_x2+l2.offset
Ext_x3=np.array([1.6, 1.85, 2.25])
Ext_y3=l3.slope*Ext_x3+l3.offset

#%% Plot fitted and extended lines

B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5) #line 1
B.plot_line(l2.xpl,l2.ypl, color="green", linewidth=.5)
B.plot_line(l3.xpl,l3.ypl, color="black",linewidth=.5)
B.plot_line(Ext_x1,Ext_y1,color="blue", linewidth=.5) #extended 1
B.plot_line(Ext_x2,Ext_y2, color="green", linewidth=.5)
B.plot_line(Ext_x3,Ext_y3, color="black", linewidth=.5)
B.pl.show()

#%% Calculate V at the intersect point of extended lines 1 and 2
V_stopL=(l1.offset-l2.offset)/(l2.slope-l1.slope)
V_stopR=(l1.offset-l3.offset)/(l3.slope-l1.slope)
Vsu=(V_stopL+V_stopR)/2
print("V stop(uv) = ", Vsu)

#%% for second(higher) intercept
V_stopLu=V_stopL

#%% Plotting Frequency vs Stopping Voltage
#Voltage Error
deV = ((V_stopLy-Vsy)+(V_stopL-Vsg)+(V_stopLb-Vsb)+(V_stopLv-Vsv)+(V_stopLu-Vsu))/5

#wavelengths
vy=578
vg=546
vb=436
vv=405
vu=365

Vstops=np.array([Vsy,Vsg,Vsb,Vsv,Vsu])
Freq=np.array([1/vy,1/vg,1/vb,1/vv,1/vu])

B.plot_exp(Freq, Vstops, deV, plot_title="Electron Energies vs Frequencies",x_label="Frequencies (Hz)", y_label="Electron Energies (eV)")
r1=B.in_between(0, 2., Freq)
l1=B.linefit(Freq[r1], Vstops[r1])
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5)
B.pl.show()

#%% hc is the slope and phi is the offset
hc=l1.slope
phi=l1.offset

print("hc = ", hc)
print("Work Function (phi) = ", phi)

#%% using the 2nd (higher) intercept
Vstops=np.array([V_stopLy,V_stopL,V_stopLb,V_stopLv,V_stopLu])
Freq=np.array([1/vy,1/vg,1/vb,1/vv,1/vu])

B.plot_exp(Freq, Vstops, deV,plot_title="Electron Energies for Second Intercept vs Frequencies",x_label="Frequencies (Hz)", y_label="Electron Energies (eV)")
r1=B.in_between(0, 2., Freq)
l1=B.linefit(Freq[r1], Vstops[r1])
B.plot_line(l1.xpl,l1.ypl, color="blue", linewidth=.5)
B.pl.show()

#%% hc is the slope and phi is the offset
hcL=l1.slope
phiL=l1.offset
#%%
print("hc(second) = ", hcL)
print("Work Function (second, phi) = ", phiL)

print("deV Yellow = ", V_stopLy-Vsy)
print("deV Green = ", V_stopL-Vsg)
print("deV Blue = ", V_stopLb-Vsb)
print("deV Violet = ", V_stopLv-Vsv)
print("deV UV = ", V_stopLu-Vsu)