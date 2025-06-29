import matplotlib.pyplot as plt
import numpy as np

# Funktion zum Einlesen der Daten
def read_data(filename):
    try:
        data = np.loadtxt(filename)
        Z = data[:, 0]
        KDF = data[:, 1]
        return Z, KDF
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei {filename}: {e}")
        return None, None


# Beispiel-Daten für die Hook Curve
Z_hook = [50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000, 10000]
KDF_hook = [0.622, 0.478, 0.437, 0.437, 0.455, 0.425, 0.404, 0.388, 0.366, 0.331, 0.298]

# Daten laden
Z1, KDF1 = read_data("Daten4.txt")

# Plot mit farbigen Zonen
fig, ax = plt.subplots(figsize=(8, 5))

# Hintergrundzonen (Zahlengrenzen beispielhaft, können angepasst werden)


ax.axvspan(0, 750, facecolor='red', alpha=0.2, label='Regime 1')
ax.axvspan(750, 1500, facecolor='yellow', alpha=0.2, label='Regime 2')
ax.axvspan(1500, 20000, facecolor='green', alpha=0.2, label='Regime 3')

# Streudiagramm
ax.scatter(Z1, KDF1, color='blue', label='Experimental Data (161 Data Points)')

# Hook Curve
#ax.plot(Z_hook, KDF_hook, color='black', linestyle='--', linewidth=2,alpha=0.5, label='Hook Curve - w/t = 1 (1% Quantil)')


# Achsenbeschriftung, Titel etc.
ax.set_title("Experimental Data – Cylindrical Shells under axial Compression (Weingarten et al., 1965)")
ax.set_xlabel("Batdorf Parameter Z", fontsize=16)
#ax.set_xlabel("Generalized Shell Slenderness Z (-)", fontsize=16)
ax.set_ylabel("Knockdown Factor KDF", fontsize=16)
#ax.set_ylabel("Strength Reduction Factor SRF (-)", fontsize=16)
ax.set_ylim(0, 1)
ax.set_xlim(0, 3500)
ax.grid(True)
ax.legend()
ax.set_xscale('linear')
#ax.set_xscale('log')
ax.axvline(750, linestyle=':', color='gray', alpha=0.75)
ax.axvline(1500, linestyle=':', color='gray', alpha=0.75)
plt.tight_layout()
plt.show()
