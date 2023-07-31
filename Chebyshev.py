import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby1, filtfilt

# Generate time axis
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second

# Generate signals s1 and s2
f1 = 10  # Frequency of s1 (in Hz)
f2 = 20  # Frequency of s2 (in Hz)
s1 = np.sin(2*np.pi*f1*t)  # Signal s1
s2 = np.sin(2*np.pi*f2*t)  # Signal s2

# Calculate s3 as the sum of s1 and s2
s3 = s1 + s2

# Add random noise to s3 to create s4
noise = np.random.normal(0, 0.5, len(t))  # Generate random noise
s4 = s3 + noise

# Chebyshev filter parameters
cutoff_freq = 30  # Cutoff frequency in Hz
order = 4  # Filter order
rp = 1  # Passband ripple in dB

# Normalize the cutoff frequency
normalized_cutoff_freq = cutoff_freq / (0.5 * fs)

# Design Chebyshev filter
b, a = cheby1(order, rp, normalized_cutoff_freq, btype='low', analog=False, output='ba')

# Apply the Chebyshev filter to the noisy signal
s4_denoised = filtfilt(b, a, s4)

# Plotting the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, s4)
plt.title('Signal s4 with Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, s4_denoised)
plt.title('Denoised Signal s4')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()



