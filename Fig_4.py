import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
#file_path = "Daten11.txt"
file_path = "Daten8.txt"
data = np.loadtxt(file_path)

# Extrahieren von Z (Batdorf-Parameter) und KDF (Knockdown Factor)
Z = data[:, 0]
KDF = data[:, 1]

# Daten für den XY-Plot (Local Buckling LRSM Kurve)
Z_values = np.array([50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000, 10000])
KDF_values = np.array([0.808, 0.727, 0.654, 0.573, 0.507, 0.467, 0.429, 0.406, 0.374, 0.342, 0.303])

# Einzelner Plot
plt.figure(figsize=(8, 6))
#plt.scatter(Z, KDF, color="blue", alpha=0.6, label="Experimental data from Mylar cylinders tested by Weingarten et al. (1965)")
#plt.scatter(Z, KDF, color="blue", alpha=0.6, label="Experimental data from isotropic cylinders (various studies from 1932 to 1979)")
plt.scatter(Z, KDF, color="blue", alpha=0.6, label="Experimental data from CFRP cylinders (various studies from 1965 to 2024)")
plt.plot(Z_values, KDF_values, linestyle='-', color='r', marker="o", markersize=6, label="Local Buckling (LRSM)")
plt.xlabel("Batdorf Parameter Z", fontsize=16)
plt.ylabel("Knockdown Factor KDF", fontsize=16)
#plt.title("Scatter Plot of Experimental Data", fontsize=14)
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3, color="gray")
plt.xlim(0, 5000)
plt.ylim(0, 1.0)
plt.tight_layout()
plt.show()
