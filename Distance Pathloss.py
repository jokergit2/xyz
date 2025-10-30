# To log distance pathloss array
import numpy as np
import matplotlib.pyplot as plt

# Constants
pa = 0.01           # Power at reference distance (dB)
pt = 100            # Transmitted power
d0 = 100            # Reference distance
d = np.arange(100, 2000, 50)  # Distance from 100 to 2000 in steps of 50

# Path loss at reference distance
pl0 = 10 * np.log10(pa / p0)

# Path loss exponents
n_values = np.arange(2.0, 4.5, 0.5)

plt.figure(figsize=(8,6))

# Plotting
for n in n_values:
    pr = pl0 + 10 * n * np.log10(d / d0)
    pt_db = 10 * np.log10(pt)
    pr_db = pt_db - pr
    plt.plot(d, pr_db, '*', label=f'n = {n:.1f}')  # Star marker only

plt.xlabel("Distance (d)")
plt.ylabel("Path Loss (dB)")
plt.title("Path Loss vs Distance for different exponents")
plt.legend()
plt.grid(True)
plt.show()
