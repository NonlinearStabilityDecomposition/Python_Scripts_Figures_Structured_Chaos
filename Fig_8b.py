import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bootstrap
from statsmodels.nonparametric.smoothers_lowess import lowess
from sklearn.metrics import mean_squared_error
from scipy.interpolate import interp1d

# Daten einlesen
data = pd.read_csv("Daten.txt", sep='\s+', header=None, names=["Z", "KDF"])

# 1. NASA SP-8007 Referenzfunktion
def nasa_sp8007(z):
    r_t = z / (2 * np.pi * np.sqrt(3 * (1 - 0.3**2)))
    return 1 - 0.902 * (1 - np.exp(-1 / 16 * np.sqrt(r_t)))

# 2. LOESS-Glättung
loess_smoothed = lowess(data["KDF"], data["Z"], frac=0.3, it=3)

# 3. Quantilberechnung
window_size = 200
step = 50
z_min, z_max = data["Z"].min(), data["Z"].max()
bins = np.arange(z_min, z_max + step, step)

valid_bins = []
q01 = []
ci_low = []
ci_high = []
counts = []
mean_q01 = []
std_q01 = []
q01_weighted = []

def quantile_01(x, axis=None):
    return np.quantile(x, 0.01, axis=axis)

def weighted_quantile(values, quantile, sample_weight=None):
    values = np.array(values)
    if sample_weight is None:
        sample_weight = np.ones(len(values))
    sample_weight = np.array(sample_weight)
    sorter = np.argsort(values)
    values = values[sorter]
    sample_weight = sample_weight[sorter]
    cumulative_weight = np.cumsum(sample_weight)
    cumulative_weight /= cumulative_weight[-1]
    return np.interp(quantile, cumulative_weight, values)

# Berechnung der Quantile + Bootstrap
for z_center in bins:
    mask = (data["Z"] >= z_center - window_size / 2) & (data["Z"] < z_center + window_size / 2)
    group = data[mask]
    if len(group) >= 5:
        valid_bins.append(z_center)
        counts.append(len(group))

        res = bootstrap((group["KDF"].values,), quantile_01, confidence_level=0.95, n_resamples=5000, method='BCa')
        q01.append(res.confidence_interval.low)
        ci_low.append(res.confidence_interval.low)
        ci_high.append(res.confidence_interval.high)

        estimates = [quantile_01(np.random.choice(group["KDF"].values, len(group["KDF"]), replace=True)) for _ in range(5000)]
        mean_q01.append(np.mean(estimates))
        std_q01.append(np.std(estimates))

        weights = 1 / (group["Z"].values + 1e-9)
        q01_weighted.append(weighted_quantile(group["KDF"].values, 0.01, sample_weight=weights))

# Umwandlung in Arrays
valid_bins = np.array(valid_bins)
q01 = np.array(q01)
ci_low = np.array(ci_low)
ci_high = np.array(ci_high)
mean_q01 = np.array(mean_q01)
std_q01 = np.array(std_q01)
q01_weighted = np.array(q01_weighted)

# Interpolation für Bewertung
hook_interp = interp1d(valid_bins, q01, bounds_error=False, fill_value=(q01[0], q01[-1]))
mask = (data["Z"] >= valid_bins.min()) & (data["Z"] <= valid_bins.max())
filtered_data = data[mask].copy()
predicted_kdf = hook_interp(filtered_data["Z"])
predicted_kdf = np.clip(predicted_kdf, 0, 1)
mse = mean_squared_error(filtered_data["KDF"], predicted_kdf)
below_curve = filtered_data["KDF"] < predicted_kdf
pct_below = np.mean(below_curve) * 100

# Plot
fig, ax1 = plt.subplots(figsize=(8, 5))

# Histogramm (rechte Achse)
ax2 = ax1.twinx()
ax2.hist(data["Z"], bins=60, color='lightgray', alpha=0.3, edgecolor='black', label='Z Histogram')
ax2.set_ylabel("Data Count", fontsize=12)

# Raw Data Scatter
ax1.scatter(data["Z"], data["KDF"], color='black', alpha=0.3, s=10, label='Raw Data')

# Kurven und Auswertungen
z_range = np.linspace(50, 3500, 100)
#ax1.plot(z_range, [nasa_sp8007(z) for z in z_range], '--', color='gray', linewidth=2, label='NASA SP-8007')
ax1.plot(loess_smoothed[:, 0], loess_smoothed[:, 1], color='red', linewidth=2, label='LOESS Smoothing (span=0.3)')
ax1.plot(valid_bins, q01, 'o-', color='green', label='Hook Curve (1% Unweighted)')
ax1.plot(valid_bins, q01_weighted, 's--', color='orange', label='Hook Curve (1% Weighted by 1/Z)')
ax1.fill_between(valid_bins, ci_low, ci_high, color='green', alpha=0.2, label='95% CI (BCa)')
ax1.errorbar(valid_bins, mean_q01, yerr=std_q01, fmt='s', color='black', capsize=3, label='Bootstrap Mean ± Std')

# Achsen und Beschriftung
ax1.set_xlabel("Batdorf Parameter Z", fontsize=16)
ax1.set_ylabel("Knockdown Factor", fontsize=16)
ax1.set_title("Statistical Analysis of Exp. Data", fontsize=16)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 3500)
ax1.set_ylim(0, 1)
ax1.text(2000, 0.1, f'MSE={mse:.3f}, Below 1% Curve: {pct_below:.1f}%', bbox=dict(facecolor='white', alpha=0.8))

# Legende
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.tight_layout()
plt.savefig("Hook_Curve_Weighted_vs_Unweighted_With_Histogram.png", dpi=300)
plt.show()
