import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Experimentelle Daten aus Datei einlesen
data_file = "Daten4Rt.txt"
df_exp = pd.read_csv(data_file, delim_whitespace=True, names=["R/t", "KDF"])

# Definierte Gleichung für KDF (NASA SP-8019 Approximation)
def rho_eq(R_t):
    return 1 - 0.902 * (1 - np.exp(- (1 / 16) * np.sqrt(R_t)))

# Wertebereich für die Gleichung definieren
R_t_values = np.linspace(1, 2000, 500)
rho_values = rho_eq(R_t_values)

# Erstellen der Abbildung
fig, ax = plt.subplots(figsize=(8, 6))

# Experimentelle Datenpunkte (rot, mit Marker X)
ax.scatter(df_exp["R/t"], df_exp["KDF"], color="red", marker="x", s=60, alpha=0.8, label="Weingarten et al (161), 1965")



# Gleichung aus dem Bild plotten
ax.plot(R_t_values, rho_values, color="blue", linestyle="--", linewidth=2, label="NASA SP-8007 (Design Guideline)")

# Achsenbeschriftungen
#ax.set_xlabel("Radius-to-thickness ratio R/t", fontsize=16)
ax.set_xlabel("Radius-to-thickness ratio, R/t", fontsize=16)
ax.set_ylabel("Knockdown Factor KDF", fontsize=16)
#ax.set_ylabel("Strength Reduction Factor SRF (-)", fontsize=16)
#ax.set_title("Conventional Representation: SRF vs. Radius-to-Thickness Ratio (R/t)", fontsize=16, pad=15)
ax.set_title("Cylindrical Shells Under Axial Compression", fontsize=16, pad=15)

# X-Achse auf 0 bis 2000 begrenzen
ax.set_xlim(0, 1000)

# Y-Achse (falls nötig, kann auch angepasst werden)
ax.set_ylim(0, 1)

# Gitterlinien hinzufügen
ax.grid(True, linestyle="--", linewidth=0.5, color="gray")

# Legende
ax.legend(loc="upper right", fontsize=12, frameon=True, facecolor="white")

# Layout anpassen und anzeigen
plt.tight_layout()
plt.show()
