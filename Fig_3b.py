import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Experimentelle Daten aus Datei einlesen
data_file = "DatenRt.txt"
df_exp = pd.read_csv(data_file, delim_whitespace=True, names=["Z", "KDF"])

# Erstellen der Abbildung
fig, ax = plt.subplots(figsize=(8, 6))

# Experimentelle Datenpunkte (rot, mit Marker X)
ax.scatter(df_exp["Z"], df_exp["KDF"], color="red", marker="x", s=60, alpha=0.8, label="Weingarten et al (133), 1965")

# Konstante Referenzlinie für NASA SP-8019 (KDF = 0.33)
ax.axhline(y=0.33, color="blue", linestyle="--", linewidth=1.5, label="NASA SP-8019 (Design Limit: KDF = 0.33)")

# Achsenbeschriftungen
#ax.set_xlabel("Average Radius of Curvature to Thickness ratio, Ra/t (-)", fontsize=14)
ax.set_xlabel("Mean Radius-to-thickness ratio, Rm/t", fontsize=16)
ax.set_ylabel("Knockdown Factor KDF", fontsize=16)
#ax.set_ylabel("Strength Reduction Factor SRF (-)", fontsize=16)
ax.set_title("Conical Shells Under Axial Compression", fontsize=16, pad=15)
#ax.set_title("Conventional Representation: SRF vs. Mean Radius-to-Thickness Ratio (Rm/t)", fontsize=16, pad=15)


# Achsenlimits (anpassen falls nötig)
ax.set_xlim(df_exp["Z"].min() * 0.9, df_exp["Z"].max() * 1.1)
ax.set_ylim(0, 1)

# Gitterlinien hinzufügen
ax.grid(True, linestyle="--", linewidth=0.5, color="gray")

# Legende
ax.legend(loc="upper right", fontsize=12, frameon=True, facecolor="white")
ax.set_xlim(0, 3500)
# Layout anpassen und anzeigen
plt.tight_layout()
plt.show()
