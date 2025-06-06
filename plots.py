import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
# Data
demo_names = [
    "flip.campfire.man", "inner.einstein.marilyn", "jigsaw.houseplants.marilyn",
    "negate.landscape.houseplants", "patch.lemur.kangaroo", "pixel.duck.rabbit",
    "skew.taylor.rose", "skew.tudor.skull"
]

tancik_a = [0.2682, 0.1394, 0.1070, 0.3184, 0.3329, 0.3127, 0.1648, 0.1853]
tancik_c = [0.2742, 0.2500, 0.2500, 0.7248, 0.2756, 0.2500, 0.2500, 0.2500]

va_a = [0.1582, 0.2196, 0.1468, 0.2432, 0.2503, 0.2653, 0.2439, 0.2141]
va_c = [0.4553, 0.5273, 0.5715, 0.5722, 0.5063, 0.4696, 0.4827, 0.5298]

burgert_a = [0.0502, 0.2635, 0.1988, 0.0573, 0.0881, 0.1480, 0.2315, 0.2244]
burgert_c = [0.5008, 0.5210, 0.4046, 0.6020, 0.3992, 0.1290, 0.4844, 0.5023]

bar_width = 0.25
x = np.arange(len(demo_names))
num = 15  # font size

# Colors
colors = {
    'Tancik': '#E0EBEB',
    'VA Original': '#F7BDA9',
    'Burgert': '#FBDED4'
}

# Plot
fig, axs = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# A Score
axs[0].bar(x - bar_width, tancik_a, width=bar_width, label='Tancik (A)', color=colors['Tancik'])
axs[0].bar(x, va_a, width=bar_width, label='VA Original (A)', color=colors['VA Original'])
axs[0].bar(x + bar_width, burgert_a, width=bar_width, label='Burgert (A)', color=colors['Burgert'])
axs[0].set_ylabel("CLIP-A", fontsize=num, fontweight='bold')
# axs[0].set_title("N×M Matrix CLIP - Alignment (A) Score Comparison", fontsize=num, fontweight='bold')
axs[0].legend(fontsize=num)

# C Score
axs[1].bar(x - bar_width, tancik_c, width=bar_width, label='Tancik (C)', color=colors['Tancik'])
axs[1].bar(x, va_c, width=bar_width, label='VA Original (C)', color=colors['VA Original'])
axs[1].bar(x + bar_width, burgert_c, width=bar_width, label='Burgert (C)', color=colors['Burgert'])
axs[1].set_ylabel("CLIP-C", fontsize=num, fontweight='bold')
# axs[1].set_title("N×M Matrix CLIP - Concealment (C) Score Comparison", fontsize=num, fontweight='bold')
axs[1].set_xticks(x)
xtick_labels = axs[1].set_xticklabels(demo_names, rotation=30, ha='right', fontsize=num)
for label in xtick_labels:
    label.set_fontweight('bold')
axs[1].legend(fontsize=num)

# Remove all gridlines
for ax in axs:
    ax.grid(False)

plt.tight_layout()
plt.savefig("imgs/AC_scores_coms.pdf", format='pdf')
plt.savefig("imgs/AC_scores_coms.png", format='png', dpi=300)
plt.show()










import matplotlib.pyplot as plt

# Provided average A and C scores for each view count (no sampling needed)
view_counts = [2, 3, 4, 5, 6]
# avg_A_scores = [0.2383, 0.2376, 0.2465, 0.2308, 0.2466]
# avg_C_scores = [0.4917, 0.2303, 0.3143, 0.2979, 0.2251]
avg_A_scores = [0.2383, 0.2376, 0.2465, 0.2308, 0.2466]
avg_C_scores = [0.4917, 0.2303, 0.3143, 0.2979, 0.2251]
num = 20

# Plot
plt.figure(figsize=(12, 8))
plt.plot(view_counts, avg_A_scores, marker='o', label='NxM CLIP-A (Alignment)', color='#ACD6EC', linewidth=3, markersize=10)
plt.plot(view_counts, avg_C_scores, marker='s', label='NxM CLIP-C (Concealment)', color='#F5A889', linewidth=3, markersize=10)
plt.axvline(x=4, color='gray', linestyle='--', label='Empirical Threshold (4 Views)', linewidth=3)
plt.xticks(view_counts, fontsize=num, fontweight='bold')  # Only integer ticks
plt.yticks(fontsize=num, fontweight='bold')
# plt.title("NxM Matrix Average CLIP-A / CLIP-C Scores by Number of Views", fontsize=num, fontweight='bold')
plt.xlabel("Number of Views", fontsize=num, fontweight='bold')
plt.ylabel("Average CLIP Score", fontsize=num, fontweight='bold')
plt.legend(fontsize=num)
plt.ylim(0.15, 0.55)  # 统一比例
plt.tight_layout()
plt.grid(False)
plt.savefig("imgs/threshold.pdf", format='pdf', bbox_inches='tight')
plt.savefig("imgs/threshold.png", format='png', dpi=300, bbox_inches='tight')
plt.show()









import matplotlib.pyplot as plt

# Provided average A and C scores for each view count (NxN matrix data)
view_counts = [2, 3, 4, 5, 6]
avg_A_scores = [0.2383, 0.2376, 0.2465, 0.2308, 0.2466]
avg_C_scores = [0.4917, 0.2303, 0.3143, 0.2979, 0.2251]

# Single-view scores for 4, 5, 6 views
single_view_counts = [4, 5, 6]
single_A_scores = [0.2724, 0.2630, 0.2612]
single_C_scores = [0.2500, 0.2000, 0.1667]

num = 20
font_num =18
# Set global font weight to bold
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
# Plot
plt.figure(figsize=(12, 8))
plt.plot(view_counts, avg_A_scores, marker='o', label='NxM CLIP-A (Alignment)', color='#ACD6EC', linewidth=3, markersize=10)
plt.plot(view_counts, avg_C_scores, marker='s', label='NxM CLIP-C (Concealment)', color='#F5A889', linewidth=3, markersize=10)
plt.plot(single_view_counts, single_A_scores, marker='D', linestyle='--', label='Single CLIP-A', color='#4A90E2', linewidth=3, markersize=10)
plt.plot(single_view_counts, single_C_scores, marker='*', linestyle='--', label='Single CLIP-C', color='#D36F52', linewidth=3, markersize=20)

for x, y in zip(single_view_counts, single_A_scores):
    plt.text(x, y + 0.009, f"{y:.3f}", ha='center', fontsize=font_num, fontweight='bold')
for x, y in zip(single_view_counts, single_C_scores):
    plt.text(x, y - 0.015, f"{y:.3f}", ha='center', fontsize=font_num, fontweight='bold')

plt.axvline(x=4, color='gray', linestyle='--', label='Empirical Threshold (4 Views)', linewidth=3)
# plt.gca().axes.get_yaxis().set_visible(False)
plt.xticks(view_counts, fontsize=num, fontweight='bold')
plt.yticks(fontsize=num, fontweight='bold')
# plt.title("CLIP-A / CLIP-C Scores by Number of Views (Matrix vs. Single)", fontsize=num, fontweight='bold')
plt.xlabel("Number of Views", fontsize=num, fontweight='bold')
plt.ylabel("Average CLIP Score", fontsize=num, fontweight='bold')
plt.legend(fontsize=font_num)
plt.ylim(0.15, 0.55)  # 统一比例
plt.tight_layout()
plt.grid(False)
plt.savefig("imgs/threshold_com.pdf", format='pdf', bbox_inches='tight')
plt.savefig("imgs/threshold_com.png", format='png', dpi=300, bbox_inches='tight')
plt.show()