import matplotlib.pyplot as plt
import numpy as np

# Data for stability classification and knockdown factors
batdorf_Z = [50, 100, 200, 400,580, 700, 1000, 1500, 2000, 3000, 5000]
batdorf_Z2 = [50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000]
# Imperfection-sensitive regime (low Z)
kdf_imperfection = [0.808, 0.727, 0.654, 0.573, 0.507, 0.467, 0.429, 0.406, 0.374, 0.342]

# Transition zone (mid Z)
kdf_transition = [0.622, 0.478, 0.437, 0.437,0.47, 0.455, 0.425, 0.404, 0.388, 0.366, 0.331]

# Local buckling-dominated regime (high Z)
kdf_local_buckling = [0.663, 0.487, 0.465, 0.489, 0.56, 0.6, 0.64, 0.676, 0.72, 0.791]

# Create plot
plt.figure(figsize=(8, 5))

# Add background color for different stability regimes
plt.axvspan(0, 200, color='red', alpha=0.2, label="Regime 1")  # Light Red
plt.axvspan(200, 580, color='yellow', alpha=0.2, label="Regime 2")  # Light Gray
plt.axvspan(580, 5000, color='green', alpha=0.2, label="Regime 3")  # Light Blue

# plt.axvspan(0, 200, color='red', alpha=0.2, label="Global-Trigger Collapse Regime (worst case)")  # Light Red
# plt.axvspan(200, 580, color='yellow', alpha=0.2, label="Regime Transition Zone")  # Light Gray
# plt.axvspan(580, 5000, color='green', alpha=0.2, label="Local-Trigger Collapse Regime (worst case)")  # Light Blue


plt.plot(batdorf_Z2, kdf_imperfection, 'bo-', label="Local Buckling (LRSM)")
plt.plot(batdorf_Z, kdf_transition, 'ko--', label="Monte Carlo Simulation (1% Quantil - LRSM & MGI w/t = 1)")
plt.plot(batdorf_Z2, kdf_local_buckling, 'ro-', label="Monte Carlo Simulation (1% Quantil - MGI w/t = 1)")

# Set axis limits
plt.xlim(0, 2000)
plt.ylim(0, 1)

# Labels and legend
plt.xscale("linear")
plt.xlabel("Batdorf Parameter Z", fontsize=16)
#plt.xlabel("Generalized Shell Slenderness Z (-)", fontsize=16)
plt.ylabel("Knockdown Factor KDF", fontsize=16)
#plt.ylabel("Strength Reduction Factor SRF (-)", fontsize=16)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.3), ncol=2)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Save as high-quality TIFF file
plt.savefig("figure_8.tiff", format="tiff", dpi=600, bbox_inches="tight")

# Show plot
plt.show()
