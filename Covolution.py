import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

# Define the time vector for the signals
t = np.linspace(0, 1, 1000)

# Define the low-frequency signal (s1), high-frequency signal (s2), and mid-range frequency signal (s3)
s1 = np.sin(2 * np.pi * 1 * t)  # Low frequency signal (1Hz)
s2 = np.sin(2 * np.pi * 250 * t)  # High frequency signal (250Hz)
s3 = np.sin(2 * np.pi * 15 * t)  # Mid-range frequency signal (15Hz)

# Combine the signals to create s4
s4 = s1 + s2 + s3

# Define the sampling rate and Nyquist frequency
sampling_rate = 1000  # Hz
nyquist_freq = 0.5 * sampling_rate

# Cutoff frequencies for different filters
lowpass_cutoff = 20  # Low-pass filter cutoff frequency (in Hz)
highpass_cutoff = 5  # High-pass filter cutoff frequency (in Hz)
bandstop_low_cutoff = 20  # Band-stop filter lower cutoff frequency (in Hz)
bandstop_high_cutoff = 100  # Band-stop filter higher cutoff frequency (in Hz)
bandpass_low_cutoff = 10  # Band-pass filter lower cutoff frequency (in Hz)
bandpass_high_cutoff = 50  # Band-pass filter higher cutoff frequency (in Hz)

# Design low-pass filter
low_b, low_a = butter(N=6, Wn=lowpass_cutoff/nyquist_freq, btype='low', analog=False)
# Design high-pass filter
high_b, high_a = butter(N=6, Wn=highpass_cutoff/nyquist_freq, btype='high', analog=False)
# Design band-stop filter
bandstop_b, bandstop_a = butter(N=6, Wn=[bandstop_low_cutoff/nyquist_freq, bandstop_high_cutoff/nyquist_freq],
                                btype='bandstop', analog=False)
# Design band-pass filter
bandpass_b, bandpass_a = butter(N=6, Wn=[bandpass_low_cutoff/nyquist_freq, bandpass_high_cutoff/nyquist_freq],
                                btype='bandpass', analog=False)

# Apply filters to the signals
low_filtered_signal = filtfilt(low_b, low_a, s4)
high_filtered_signal = filtfilt(high_b, high_a, s4)
bandstop_filtered_signal = filtfilt(bandstop_b, bandstop_a, s4)
bandpass_filtered_signal = filtfilt(bandpass_b, bandpass_a, s4)

# Frequency response of the filters
w_low, h_low = freqz(low_b, low_a, worN=8000)
magnitude_response_low = np.abs(h_low)
w_high, h_high = freqz(high_b, high_a, worN=8000)
magnitude_response_high = np.abs(h_high)
w_bandstop, h_bandstop = freqz(bandstop_b, bandstop_a, worN=8000)
magnitude_response_bandstop = np.abs(h_bandstop)
w_bandpass, h_bandpass = freqz(bandpass_b, bandpass_a, worN=8000)
magnitude_response_bandpass = np.abs(h_bandpass)

# Plot the original and filtered signals
plt.figure(figsize=(12, 10))

plt.subplot(5, 1, 1)
plt.plot(t, s1, label='Low Frequency Signal (s1)')
plt.plot(t, s2, label='High Frequency Signal (s2)')
plt.plot(t, s3, label='Mid-range Frequency Signal (s3)')
plt.plot(t, s4, label='Combined Signal (s4)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(t, low_filtered_signal, label='Filtered Signal (Low-Pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(t, high_filtered_signal, label='Filtered Signal (High-Pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 4)
plt.plot(t, bandstop_filtered_signal, label='Filtered Signal (Band-Stop)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 5)
plt.plot(t, bandpass_filtered_signal, label='Filtered Signal (Band-Pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Plot the frequency responses of the filters
plt.figure(figsize=(12, 8))

plt.subplot(4,1,1)
plt.plot(0.5 * sampling_rate * w_low / np.pi, magnitude_response_low, label='Low-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response of Low-Pass Filters')
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(0.5 * sampling_rate * w_high / np.pi, magnitude_response_high, label='High-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response of High-Pass Filters')
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(0.5 * sampling_rate * w_bandstop / np.pi, magnitude_response_bandstop, label='Band-Stop Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response of Band-Stop Filters')
plt.grid(True)

plt.subplot(4,1,4)
plt.plot(0.5 * sampling_rate * w_bandpass / np.pi, magnitude_response_bandpass, label='Band-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response of Band-Pass Filters')
plt.grid(True)

plt.tight_layout()
plt.show()
