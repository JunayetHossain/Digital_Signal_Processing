import numpy as np
from scipy.fft import fftfreq

# Define the number of data points and sample spacing
n_data_points = 5
sample_spacing = 0.1

# Calculate the frequencies using scipy.fft.fftfreq()
frequencies = fftfreq(n_data_points, d=sample_spacing)

# Print the frequencies
print("Frequencies associated with DFT components:")
print(frequencies)

