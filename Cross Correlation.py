import numpy as np

x = np.array([3, 4, 5, 6, 2])
y = np.array([4, 5, 6])

if len(x) > len(y):
    y = np.pad(y, (0, len(x)-len(y)), mode='constant')
else:
    x = np.pad(x, (0, len(y)-len(x)), mode='constant')

ccf_xy = np.zeros(2*len(x)-1)
for k in range(-len(x)+1, len(x)):
    if k < 0:
        ccf_xy[k+len(x)-1] = np.sum(x[:k] * y[-k:])
    elif k == 0:
        ccf_xy[k+len(x)-1] = np.sum(x * y)
    else:
        ccf_xy[k+len(x)-1] = np.sum(x[k:] * y[:-k])

print(ccf_xy)