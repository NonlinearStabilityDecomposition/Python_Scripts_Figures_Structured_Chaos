# Nach dem Reset müssen alle Imports und Variablen neu definiert werden
import matplotlib.pyplot as plt

# Werte für die x-Achse (Batdorf Parameter Z)
x_values = [50, 100, 200, 400, 700, 1000]

# LRSM-Kurve (z. B. Z = 457)
y_values_left = [0.65, 0.56, 0.537, 0.492, 0.467, 0.434]

# Hook Curve für w/t = 0.5 (angenommene Werte aus Heatmap oder Tabelle)
y_hook_wt_05 = [0.622, 0.478, 0.437, 0.437, 0.455, 0.425]  # Beispielwerte

y_hook_wt_a = [0.932, 0.88, 0.768, 0.684, 0.626, 0.588]  # Beispielwerte
# Experimentelle Daten für Z = 457
exp_x = [317] * 1
exp_y = [0.87]
exp_wt = [1.18]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter Plot für experimentelle Daten
scatter_left = ax.scatter(exp_x, exp_y, c=exp_wt, cmap='jet', edgecolors='k', s=100, marker='o', label='Exp. Data, Shell Z = 317')

# LRSM-Kurve
ax.plot(x_values, y_values_left, marker='o', linestyle='dashed', color='green', label='MDC - CFRP Imperfection (w/t = 1)')

# Hook-Kurve für w/t = 0.5
ax.plot(x_values, y_hook_wt_05, marker='s', linestyle='--', color='red', label='MDC - Metal Imperfection (w/t = 1)')

ax.plot(x_values, y_hook_wt_a, marker='s', linestyle='--', color='blue', label='MDC - CFRP Imperfection & Anisotropy (w/t = 1)')


# Achsenbeschriftung und Grenzen
ax.set_xlabel(r"Batdorf Parameter Z", fontsize=16)
ax.set_ylabel(r"Knockdown Factor", fontsize=16)
ax.set_xlim(50, 1000)
ax.set_ylim(0, 1.0)
ax.grid(True)

ax.axhline(y=0.33, color="black", linestyle="-", linewidth=1.5, label="NASA SP-8019 (KDF = 0.33)")
#ax.plot(317, 0.33, marker='*', markerfacecolor='white', markeredgecolor='black', markersize=14, label='NASA SP-8019')
ax.plot(317, 0.69, marker='D', markerfacecolor='white', markeredgecolor='black', markersize=9, label='MDC (estimated, 1% quantile)')
# Legende
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20), ncol=2, frameon=False)

# Farbskala
cbar = plt.colorbar(scatter_left, ax=ax)
cbar.set_label("w/t value")

# Anzeige
plt.tight_layout()
plt.show()
