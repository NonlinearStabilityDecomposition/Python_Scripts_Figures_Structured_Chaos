import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# MDC Daten
hook_curve_data = {
    "Z": [50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000, 10000],
    "LB_0": [0.803, 0.714, 0.647, 0.57, 0.505, 0.463, 0.427, 0.403, 0.371, 0.338, 0.303],
    "Q_0":  [0.808, 0.727, 0.654, 0.573, 0.507, 0.467, 0.429, 0.406, 0.374, 0.342, 0.308],
    "UB_0": [0.812, 0.741, 0.661, 0.576, 0.508, 0.47, 0.431, 0.408, 0.378, 0.347, 0.313],
    "LB_1": [0.622, 0.546, 0.516, 0.48, 0.456, 0.418, 0.382, 0.374, 0.343, 0.305, 0.273],
    "Q_1":  [0.65, 0.56, 0.537, 0.492, 0.467, 0.434, 0.402, 0.387, 0.354, 0.325, 0.289],
    "UB_1": [0.679, 0.575, 0.558, 0.504, 0.477, 0.451, 0.422, 0.399, 0.365, 0.345, 0.305],
    "LB_2": [0.569, 0.481, 0.431, 0.406, 0.4, 0.36, 0.346, 0.332, 0.324, 0.301, 0.279],
    "Q_2":  [0.583, 0.5, 0.444, 0.424, 0.407, 0.383, 0.372, 0.357, 0.336, 0.315, 0.286],
    "UB_2": [0.597, 0.519, 0.457, 0.442, 0.415, 0.407, 0.397, 0.382, 0.348, 0.33, 0.292],
}
df_hook = pd.DataFrame(hook_curve_data).astype("float64")

# Experimental-Daten laden
df_exp = pd.read_csv("Daten8.txt", delim_whitespace=True, names=["Z", "KDF"]).astype("float64")

# Fit-Funktion (Power Law)
def power_law(Z, a, b):
    return a * Z**b

# Zwei nebeneinanderliegende Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), sharey=True)
colors = ["gray", "green", "orange"]
w_t_values = [0, 1, 2]
fit_results = []

# Plot links: MDCs + CI + Experimente
for i, color in zip(w_t_values, colors):
    Z = df_hook["Z"].values
    Q = df_hook[f"Q_{i}"].values
    LB = df_hook[f"LB_{i}"].values
    UB = df_hook[f"UB_{i}"].values

    ax1.plot(Z, Q, color=color, marker="o", linestyle="-", linewidth=2,
             label=f"Mechanistic Design Curves (CFRP - w/t = {i})")
    ax1.fill_between(Z, LB, UB, color=color, alpha=0.2)

# Experimente einzeichnen
ax1.scatter(df_exp["Z"], df_exp["KDF"], color="blue", marker="o", s=60, alpha=0.8,
            label="CFRP Composite Cylinder exp. data (222), 1965–2024")

ax1.set_xlabel("Batdorf Parameter Z", fontsize=16)
ax1.set_ylabel("Knockdown Factor KDF", fontsize=16)
ax1.set_title("MDC for CFRP Composite Cylinders with Confidence Intervals", fontsize=16)
ax1.set_xlim(0, 4000)
ax1.set_ylim(0.0, 1.0)
ax1.grid(True, linestyle="--", linewidth=0.3)
ax1.legend(fontsize=10, loc="lower left", frameon=True)

# Plot rechts: Power Law Fits
for i, color in zip(w_t_values, colors):
    Z = df_hook["Z"].values
    KDF = df_hook[f"Q_{i}"].values
    popt, _ = curve_fit(power_law, Z, KDF)
    KDF_fit = power_law(Z, *popt)
    r_squared = r2_score(KDF, KDF_fit)
    fit_results.append((i, popt[0], popt[1], r_squared))

    ax2.plot(Z, KDF, color=color, marker="o", linestyle="None")
    ax2.plot(Z, KDF_fit, color=color, linestyle="--", linewidth=2, label=f"w/t = {i}")

# Fit-Ergebnisse in Box anzeigen
textstr = '\n\n'.join(
    [f"w/t = {i}:\n$KDF = {a:.2f} \\cdot Z^{{{b:.3f}}}$\n$R^2 = {r2:.3f}$"
     for i, a, b, r2 in fit_results]
)
props = dict(boxstyle='round', facecolor='white', alpha=0.95)
ax2.text(0.98, 0.98, textstr, transform=ax2.transAxes, fontsize=12,
         verticalalignment='top', horizontalalignment='right', bbox=props)

ax2.set_xlabel("Batdorf Parameter Z", fontsize=16)
ax2.set_title("Power Law Fits to Mechanistic Design Curves (MDC)", fontsize=16)
ax2.set_xlim(0, 4000)
ax2.grid(True, linestyle="--", linewidth=0.3)
ax2.legend(fontsize=10, loc="lower left", frameon=True)

plt.tight_layout()
plt.show()
