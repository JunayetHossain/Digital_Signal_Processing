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

# Add random noise to s3 to create s4
noise = np.random.normal(0, 0.5, len(t))  # Generate random noise
s4 = s3 + noise

# Perform FFT on s4
fft_s4 = np.fft.fft(s4)

# Calculate the magnitudes of FFT coefficients
fft_magnitudes = np.abs(fft_s4)

# Set a threshold based on a percentage of the maximum magnitude
threshold_percent = 10  # Adjust the threshold percentage as needed
threshold = threshold_percent * np.max(fft_magnitudes) / 100

# Zero out frequencies below the threshold
fft_s4[fft_magnitudes < threshold] = 0

# Perform inverse FFT to obtain the denoised signal
s4_denoised = np.fft.ifft(fft_s4)

# Plotting the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, s4)
plt.title('Signal s4 with Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, np.real(s4_denoised))
plt.title('Denoised Signal s4')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
