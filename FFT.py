import numpy as np
import matplotlib.pyplot as plt

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

# Perform FFT on s1, s2, and s3
fft_s1 = np.fft.fft(s1)
fft_s2 = np.fft.fft(s2)
fft_s3 = np.fft.fft(s3)

# Calculate frequency axis for plotting
freq = np.fft.fftfreq(len(t), 1/fs)

# Plotting the FFT results
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(freq, np.abs(fft_s1))
plt.title('FFT of s1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(fft_s2))
plt.title('FFT of s2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(fft_s3))
plt.title('FFT of s3')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
