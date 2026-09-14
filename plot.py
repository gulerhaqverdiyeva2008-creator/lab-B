import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# 1. Read decay_observed.csv (skip header)
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', unpack=True, skiprows=1)

# 2. Set N0 to the first observed value and build analytical curve
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# 3. Make 1x2 subplot with shared axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

ax1.scatter(t, observed)
ax1.set_title("Observed data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")

ax2.plot(t, analytical, color='r')
ax2.set_title("Analytical")
ax2.set_xlabel("Time")

# 4. Save the figure
plt.savefig('figure.png')