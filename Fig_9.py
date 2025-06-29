import matplotlib.pyplot as plt
import pandas as pd

# Datei einlesen (Tab-getrennt, ohne Header)
data_path = "data_input_ST.txt"
data = pd.read_csv(data_path, sep="\t", header=None, names=["Z", "KDF", "WT", "LocalBuckling"])

# Symbolgröße auf Basis des LocalBuckling-Werts skalieren (optional anpassen)
sizes = 300 * data["LocalBuckling"] / data["LocalBuckling"].max()

# Plot erstellen
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(
    data["Z"], data["KDF"],
    c=data["WT"],
    cmap='jet',
    s=sizes,
    alpha=0.8,
    edgecolor='k',
    linewidth=0.3
)

# Achsenbeschriftungen und Titel
ax.set_xlabel("Batdorf Parameter Z", fontsize=16)
ax.set_ylabel("Knockdown Factor [-]", fontsize=16)
ax.set_xlim(0, 5000)
ax.set_ylim(0, 1.0)
ax.grid(True)
#plt.xscale('log')
# Farbskala für w/t-Werte
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("w/t value")

plt.title("Knockdown Factors vs. Z (w/t color, local buckling size)", fontsize=16)
plt.tight_layout()
plt.show()
