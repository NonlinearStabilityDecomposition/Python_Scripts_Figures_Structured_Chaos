import numpy as np
import matplotlib.pyplot as plt

# Data definition
Z_values = np.array([50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000, 10000])

# Knockdown factor values for different w/t ratios
wt_values = [0.5, 1, 2, 3, 4, 6, 8]
knockdown_factors = {
    0.5: np.array([0.698, 0.57, 0.547, 0.524, 0.485, 0.46, 0.425, 0.403, 0.372, 0.34, 0.301]),
    1: np.array([0.622, 0.478, 0.437, 0.437, 0.455, 0.425, 0.404, 0.388, 0.366, 0.331, 0.298]),
    2: np.array([0.546, 0.42, 0.367, 0.353, 0.351, 0.359, 0.365, 0.357, 0.337, 0.32, 0.286]),
    3: np.array([0.522, 0.381, 0.325, 0.311, 0.298, 0.306, 0.313, 0.316, 0.318, 0.307, 0.267]),
    4: np.array([0.494, 0.358, 0.297, 0.283, 0.28, 0.273, 0.273, 0.286, 0.287, 0.283, 0.254]),
    6: np.array([0.484, 0.341, 0.276, 0.253, 0.243, 0.24, 0.24, 0.238, 0.239, 0.246, 0.232]),
    8: np.array([0.468, 0.322, 0.259, 0.235, 0.216, 0.214, 0.209, 0.21, 0.217, 0.221, 0.218]),
}

# 99% Confidence intervals (Lower and Upper Bounds)
lower_bounds = {
    0.5: np.array([0.665, 0.561, 0.54, 0.503, 0.479, 0.453, 0.397, 0.367, 0.337, 0.298, 0.298]),
    1: np.array([0.605, 0.465, 0.431, 0.423, 0.443, 0.408, 0.387, 0.38, 0.36, 0.325, 0.294]),
    2: np.array([0.517, 0.402, 0.358, 0.348, 0.345, 0.352, 0.357, 0.336, 0.327, 0.305, 0.272]),
    3: np.array([0.515, 0.374, 0.323, 0.306, 0.291, 0.3, 0.304, 0.303, 0.307, 0.295, 0.257]),
    4: np.array([0.485, 0.356, 0.281, 0.277, 0.274, 0.267, 0.264, 0.28, 0.283, 0.268, 0.232]),
    6: np.array([0.468, 0.33, 0.269, 0.249, 0.239, 0.234, 0.237, 0.231, 0.236, 0.234, 0.215]),
    8: np.array([0.457, 0.311, 0.248, 0.231, 0.212, 0.208, 0.206, 0.202, 0.21, 0.209, 0.21]),
}

upper_bounds = {
    0.5: np.array([0.731, 0.579, 0.553, 0.545, 0.492, 0.467, 0.429, 0.408, 0.376, 0.342, 0.304]),
    1: np.array([0.64, 0.491, 0.443, 0.45, 0.466, 0.443, 0.421, 0.397, 0.371, 0.337, 0.301]),
    2: np.array([0.575, 0.439, 0.377, 0.357, 0.357, 0.367, 0.373, 0.377, 0.348, 0.335, 0.299]),
    3: np.array([0.528, 0.387, 0.328, 0.317, 0.305, 0.311, 0.322, 0.33, 0.328, 0.319, 0.277]),
    4: np.array([0.502, 0.361, 0.312, 0.29, 0.287, 0.279, 0.283, 0.293, 0.291, 0.299, 0.276]),
    6: np.array([0.5, 0.352, 0.283, 0.258, 0.247, 0.246, 0.244, 0.245, 0.242, 0.259, 0.25]),
    8: np.array([0.478, 0.333, 0.269, 0.239, 0.22, 0.219, 0.212, 0.218, 0.223, 0.233, 0.227]),
}

# Create figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Define colors for different w/t values
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink']

# Left plot (Linear scale)
for i, wt in enumerate(wt_values):
    axes[0].plot(Z_values, knockdown_factors[wt], marker='o', linestyle='-', color=colors[i], label=f"w/t = {wt}")
    axes[0].fill_between(Z_values, lower_bounds[wt], upper_bounds[wt], color=colors[i], alpha=0.2)

axes[0].set_xlabel("Batdorf Parameter Z", fontsize=14)
axes[0].set_ylabel("Knockdown Factor KDF", fontsize=14)
axes[0].set_title("Monte Carlo Simulation (1% Quantil & 99% Confidence Intervals - LRSM & MGI)", fontsize=14)
axes[0].title.set_position([1.15, 1.05])
axes[0].set_xlim(50, 3000)
axes[0].set_ylim(0, 1)
axes[0].grid(True, linestyle="--", linewidth=0.5)
axes[0].legend(loc="upper right", fontsize=10)

# Right plot (Log scale)
for i, wt in enumerate(wt_values):
    axes[1].plot(Z_values, knockdown_factors[wt], marker='o', linestyle='-', color=colors[i], label=f"w/t = {wt}")
    axes[1].fill_between(Z_values, lower_bounds[wt], upper_bounds[wt], color=colors[i], alpha=0.2)

axes[1].set_xlabel("Batdorf Parameter Z", fontsize=14)
#axes[1].set_title("Knockdown Factors with Confidence Intervals (Log Scale)", fontsize=14)
axes[1].set_xscale("log")
axes[1].set_xlim(50, 10000)
axes[1].set_ylim(0, 1)
axes[1].grid(True, linestyle="--", linewidth=0.5)
axes[1].legend(loc="upper right", fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()
