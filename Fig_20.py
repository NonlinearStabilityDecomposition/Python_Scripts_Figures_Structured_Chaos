import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataframe with Knockdown Factors and Confidence Intervals
data = {
    "Z": [50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 5000, 10000],
    "w/t = 0": [(0.808, 0.803, 0.812), (0.727, 0.714, 0.741), (0.654, 0.647, 0.661), 
                 (0.573, 0.570, 0.576), (0.507, 0.505, 0.508), (0.467, 0.463, 0.470),
                 (0.429, 0.427, 0.431), (0.406, 0.403, 0.408), (0.374, 0.371, 0.378), 
                 (0.342, 0.338, 0.347), (0.303, 0.301, 0.305)],
    "w/t = 0.5": [(0.698, 0.665, 0.731), (0.570, 0.561, 0.579), (0.547, 0.540, 0.533),
                  (0.524, 0.503, 0.545), (0.485, 0.479, 0.492), (0.460, 0.453, 0.467),
                  (0.425, 0.422, 0.429), (0.403, 0.397, 0.408), (0.372, 0.367, 0.376),
                  (0.340, 0.337, 0.342), (0.301, 0.298, 0.304)],
    "w/t = 1": [(0.622, 0.605, 0.640), (0.478, 0.465, 0.491), (0.437, 0.431, 0.443),
                (0.437, 0.423, 0.450), (0.455, 0.443, 0.466), (0.425, 0.408, 0.443),
                (0.404, 0.387, 0.421), (0.388, 0.380, 0.397), (0.366, 0.360, 0.371),
                (0.331, 0.325, 0.337), (0.298, 0.294, 0.301)],
    
    "w/t = 2": [
        (0.546, 0.517, 0.575),
        (0.420, 0.402, 0.439),
        (0.367, 0.358, 0.377),
        (0.353, 0.348, 0.357),
        (0.351, 0.345, 0.357),
        (0.359, 0.352, 0.367),
        (0.365, 0.357, 0.373),
        (0.357, 0.336, 0.377),
        (0.337, 0.327, 0.348),
        (0.320, 0.305, 0.335),
        (0.286, 0.272, 0.299)
    ],
    "w/t = 3": [
        (0.522, 0.515, 0.528),
        (0.381, 0.374, 0.387),
        (0.325, 0.323, 0.328),
        (0.311, 0.306, 0.317),
        (0.298, 0.291, 0.305),
        (0.306, 0.300, 0.311),
        (0.313, 0.304, 0.322),
        (0.316, 0.303, 0.330),
        (0.318, 0.307, 0.328),
        (0.307, 0.295, 0.319),
        (0.267, 0.257, 0.277)
    ],
    "w/t = 4": [
    (0.494, 0.485, 0.502),
    (0.358, 0.356, 0.361),
    (0.297, 0.281, 0.312),
    (0.283, 0.277, 0.290),
    (0.280, 0.274, 0.287),
    (0.273, 0.267, 0.279),
    (0.273, 0.264, 0.283),
    (0.286, 0.280, 0.293),
    (0.287, 0.283, 0.291),
    (0.283, 0.268, 0.299),
    (0.254, 0.232, 0.276)
],
    "w/t = 6": [
    (0.484, 0.468, 0.500),
    (0.341, 0.330, 0.352),
    (0.276, 0.269, 0.283),
    (0.253, 0.249, 0.258),
    (0.243, 0.239, 0.247),
    (0.240, 0.234, 0.246),
    (0.240, 0.237, 0.244),
    (0.238, 0.231, 0.245),
    (0.239, 0.236, 0.242),
    (0.246, 0.234, 0.259),
    (0.232, 0.215, 0.250)
],
    "w/t = 8": [
    (0.468, 0.457, 0.478),
    (0.322, 0.311, 0.333),
    (0.259, 0.248, 0.269),
    (0.235, 0.231, 0.239),
    (0.216, 0.212, 0.220),
    (0.214, 0.208, 0.219),
    (0.209, 0.206, 0.212),
    (0.210, 0.202, 0.218),
    (0.217, 0.210, 0.223),
    (0.221, 0.209, 0.233),
    (0.218, 0.210, 0.227)
]
}

# Transforming the data for heatmap
df_values = pd.DataFrame({col: [x[0] for x in values] for col, values in data.items() if col != "Z"})
df_values.index = data["Z"]

# Creating heatmap
plt.figure(figsize=(12, 7))
ax = sns.heatmap(df_values, annot=True, cmap="coolwarm", fmt=".3f", linewidths=0.5, cbar_kws={'label': 'Knockdown Factor KDF'})

# Adding confidence intervals as text inside the heatmap
fig, ax = plt.subplots(figsize=(12, 7))
sns.heatmap(df_values, annot=False, cmap="coolwarm", fmt=".3f", linewidths=0.5, cbar_kws={'label': 'Knockdown Factor KDF'}, ax=ax)

# Adjusting text size for better readability
for i, z in enumerate(data["Z"]):
    for j, col in enumerate(df_values.columns):
        kdf, lb, ub = data[col][i]
        if lb is not None and ub is not None:
            ax.text(j + 0.5, i + 0.35, f"{kdf:.3f}", color="black", fontsize=14, ha="center", va="center", fontweight='bold')  # Larger font for 1% quantile
            ax.text(j + 0.5, i + 0.65, f"[{lb:.3f}, {ub:.3f}]", color="black", fontsize=10, ha="center", va="center")  # Larger font for confidence intervals

# Formatting the plot
ax.set_title("Heatmap of Knockdown Factors with Confidence Intervals", fontsize=16)
ax.set_xlabel("w/t", fontsize=14)
ax.set_ylabel("Batdorf Parameter Z", fontsize=14)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)

# Save the updated heatmap with larger text
#heatmap_large_text_path = "/mnt/data/knockdown_factor_heatmap_large_text.png"
#plt.savefig(heatmap_large_text_path, dpi=300, bbox_inches="tight")
plt.show()

# Provide the file path for download
#heatmap_large_text_path