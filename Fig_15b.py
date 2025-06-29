# Nach dem Reset müssen alle Imports und Variablen neu definiert werden
import matplotlib.pyplot as plt

# Werte für die x-Achse (Batdorf Parameter Z)
x_values = [50, 100, 200, 400, 700, 1000]

# LRSM-Kurve (z. B. Z = 457)
y_values_left = [0.803, 0.727, 0.654, 0.573, 0.507, 0.467]

# Hook Curve für w/t = 0.5 (angenommene Werte aus Heatmap oder Tabelle)
y_hook_wt_05 = [0.698, 0.57, 0.547, 0.524, 0.485, 0.46]  # Beispielwerte

# Experimentelle Daten für Z = 457
exp_x = [457] * 1
exp_y = [0.80]
exp_wt = [0.3]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter Plot für experimentelle Daten
scatter_left = ax.scatter(exp_x, exp_y, c=exp_wt, cmap='jet', edgecolors='k', s=100, marker='o', label='Exp. Data, Shell Z = 457')

# LRSM-Kurve
ax.plot(x_values, y_values_left, marker='o', linestyle='-', color='black', label='MDC (w/t = 0, 1% Quantile)')

# Hook-Kurve für w/t = 0.5
ax.plot(x_values, y_hook_wt_05, marker='s', linestyle='--', color='red', label='MDC (w/t = 0.5, 1% Quantile)')

# Achsenbeschriftung und Grenzen
ax.set_xlabel(r"Batdorf Parameter Z", fontsize=16)
ax.set_ylabel(r"Knockdown Factor", fontsize=16)
ax.set_xlim(50, 1000)
ax.set_ylim(0, 1.0)
ax.grid(True)

ax.plot(457, 0.386, marker='*', markerfacecolor='white', markeredgecolor='black', markersize=14, label='NASA SP-8007')
ax.plot(457, 0.534, marker='D', markerfacecolor='white', markeredgecolor='black', markersize=9, label='MDC (interpolated, 1% quantile)')
# Legende
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)

# Farbskala
cbar = plt.colorbar(scatter_left, ax=ax)
cbar.set_label("w/t value")

# Anzeige
plt.tight_layout()
plt.show()
