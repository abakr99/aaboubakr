#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:57:37 2024

@author: ahmed
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot
from numpy.fft import fftshift, fft, fftfreq, ifft
import scipy.fftpack
from matplotlib import interactive
import LT.box as b
df = pd.read_csv('/Users/ahmed/Documents/Advanced Lab/scaled signal.csv')
df.head()
#%%
import matplotlib.pyplot as plt
print("Line graph: ")
plt.plot(df["x"], (df["y"]))  # Calculate the absolute value of y
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.title("Scaled Signal Data Voltage vs Time")
plt.xticks(np.arange(min(df["x"]), max(df["x"])+1, 1.0))  # Set x-axis ticks for every second
plt.show()
#%%
#Filtering Signal 

N = len(df)
T = (df["x"].iloc[1] - df["x"].iloc[0])
y = (df['y'])
yf = fft(y)
xf = np.fft.fftfreq(N, T)

# Identify the cutoff frequency (modify this based on your data)
cutoff_frequency = 20000  # Example: 50 Hz

# Create a mask for frequencies above the cutoff (Low-pass filter)
mask = np.abs(xf) > cutoff_frequency

# Apply the mask to the FFT result (Set high frequencies to zero)
yf_filtered = yf.copy()
yf_filtered[mask] = 0

# Inverse FFT to get the filtered time domain signal
y_filtered = ifft(yf_filtered)

plt.plot(df["x"], np.abs(y_filtered), label="Filtered")
plt.title("Filtered Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")

plt.tight_layout()
plt.show()

#%%
# Fourier Transform Spectral Magnitude
N = len(df)
T = (df["x"].iloc[1] - df["x"].iloc[0])
x = np.linspace(0, N * T, N)
y = np.abs(df['y'])
yf = fft(y)

# Calculate spectral magnitude from FFT result
spectral_magnitude = 2.0/N * np.abs(yf[0:N//2])

b.plot_line(np.fft.fftfreq(N, d=T)[0:N//2],(spectral_magnitude))
plt.xlabel("Frequency Hz")
plt.ylabel("Spectral Magnitude (RMS)")
plt.title("Fourier Transform Spectral Magnitude")
b.pl.show()
#%%
decibel_spectrum = 20 * np.log10((spectral_magnitude)/0.775)
b.plot_spline(np.fft.fftfreq(N, d=T)[0:N//2],(decibel_spectrum))
#%%
spectral_magnitude_normalized = spectral_magnitude / np.max(spectral_magnitude)
b.plot_spline(np.fft.fftfreq(N, d=T)[0:N//2], spectral_magnitude_normalized)
plt.xlabel("Frequency Hz")
plt.ylabel("Normalized Spectral Magnitude")
plt.title("Normalized Fourier Transform Spectral Magnitude")
plt.ylim(0, 0.4)
plt.xlim(0, 70)
b.pl.show()

# %%
# Spectral Phase 
# Time and voltage data
#time_data = df["x"]
#voltage_data = df["y"]

# Calculate the FFT
#sampling_rate = 1 / (time_data[1] - time_data[0])  # Assuming uniform sampling
#N = len(time_data)
#frequencies = fftfreq(N, d=1/sampling_rate)
#fft_values = fft(voltage_data)
#fft_values_shifted = fftshift(fft_values)

# Calculate the phase
#phase = np.angle(fft_values_shifted)

# Plot the Phase
# plt.figure()
# plt.plot(frequencies, phase)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Radians")
# plt.title("Fourier Transform Spectral Phase")
# plt.show()

#%%

N = len(df)
T = (df["x"].iloc[1] - df["x"].iloc[0])
y = (df['y'])

# FFT
yf = fft(y)
xf = fftfreq(N, T)

# Identify a cutoff frequency for the filter
cutoff_frequency = 20000  # Example: 50 Hz

# Extend the mask to the full length of yf
mask = np.abs(xf) > cutoff_frequency
yf_filtered = yf.copy()
yf_filtered[mask] = 0

# Recalculate spectral magnitude and decibel spectrum with filtered FFT
spectral_magnitude_filtered = 2.0/N * np.abs(yf_filtered[:N//2])
decibel_spectrum_filtered = 20 * np.log10(spectral_magnitude_filtered)  # Adding a small value to avoid log(0)

# Plotting the filtered decibel spectrum
plt.plot(xf[:N//2], decibel_spectrum_filtered)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Spectral Magnitude (dB)")
plt.title("Filtered Fourier Transform Spectral Magnitude (Decibels)")
plt.xlim(20, 20000)
plt.show()
# %%
