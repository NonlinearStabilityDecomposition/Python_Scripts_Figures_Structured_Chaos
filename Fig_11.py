import pandas as pd
import matplotlib.pyplot as plt

# Manuelle Eingabe der Daten
data = {
    "Z": [50, 100, 200, 400, 700, 1000, 1500,3000, 5000],
    "Deepdrawing": [0.546, 0.42, 0.367, 0.353, 0.351, 0.359, 0.365,0.333,	0.32],
    "Electroforming": [0.616803137, 0.560352688, 0.485306292, 0.460121937, 0.498037238, 0.437018691, 0.420360464,0.37,	0.343],
    "Machining": [0.6066493, 0.565060446, 0.446671933, 0.43923083, 0.447424011, 0.39961351, 0.372262155,0.326,	0.31],
    "Axial Welds": [0.61774549, 0.570258752, 0.459975104, 0.451692999, 0.45415636, 0.425316025, 0.393091492,0.316,	0.31],
    #"Filament Winding & Prepreg Handy Layup": [0.583, 0.5, 0.444, 0.424, 0.407, 0.383, 0.372]
}


0.359, 0.365, 0.357, 0.337, 0.32, 0.286
df = pd.DataFrame(data)

# Plot erstellen
plt.figure(figsize=(10, 6))
for column in df.columns[1:]:
    plt.plot(df["Z"], df[column], marker='o', label=column)

plt.xlabel("Batdorf Parameter Z", fontsize=16)
plt.ylabel("Knockdown Factor (KDF)", fontsize=16)
plt.title("KDF vs. Z for Different Manufacturing Processes & w/t = 2", fontsize=14)
plt.grid(True)
plt.legend(title="Manufacturing Process")
plt.ylim(0.2, 0.7)
plt.tight_layout()
plt.show()
