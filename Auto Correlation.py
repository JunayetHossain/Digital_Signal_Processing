import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 4, 5, 6, 2])
y = np.array([4, 5, 6])

N = len(x)
M = len(y)

# Using numpy's correlate function
correlation_np = np.correlate(x, y, "full")

# Using manual calculation for cross-correlation
correlation_sum = []
for k in range(-(N - 1), M):
    sum_k = 0
    for i in range(max(0, k), min(N, N + M - abs(k))):
        sum_k += x[i] * y[i - k]
    correlation_sum.append(sum_k)

corr_manual = np.array(correlation_sum)

print("Correlation (using np.correlate):", correlation_np)
print("Correlation (manual calculation):", corr_manual)

# Plotting the results
plt.figure()
plt.stem(np.arange(-(N - 1), M), corr_manual, use_line_collection=True)
plt.xlabel('Time Lag (k)')
plt.ylabel('Correlation')
plt.title('Cross-Correlation of x and y')
plt.grid(True)
plt.show()