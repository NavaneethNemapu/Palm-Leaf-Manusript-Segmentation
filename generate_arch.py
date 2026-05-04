import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

# Draw Input
ax.add_patch(patches.Rectangle((0.5, 0.3), 1, 0.4, fill=True, color='lightblue'))
ax.text(1.0, 0.5, 'Input Image\n(256x256x3)', ha='center', va='center', fontsize=10)

# Arrow
ax.arrow(1.5, 0.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Encoder
ax.add_patch(patches.Rectangle((2.1, 0.2), 1.2, 0.6, fill=True, color='orange'))
ax.text(2.7, 0.5, 'Encoder\n(Conv + Pool)', ha='center', va='center', fontsize=10)

# Arrow
ax.arrow(3.3, 0.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Bottleneck
ax.add_patch(patches.Rectangle((3.9, 0.1), 1.2, 0.8, fill=True, color='salmon'))
ax.text(4.5, 0.5, 'Bottleneck\n(Deep Features)', ha='center', va='center', fontsize=10)

# Arrow
ax.arrow(5.1, 0.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Decoder
ax.add_patch(patches.Rectangle((5.7, 0.2), 1.2, 0.6, fill=True, color='lightgreen'))
ax.text(6.3, 0.5, 'Decoder\n(UpConv + Concat)', ha='center', va='center', fontsize=10)

# Skip connection
ax.annotate("", xy=(6.3, 0.8), xytext=(2.7, 0.8), arrowprops=dict(arrowstyle="->", connectionstyle="bar,fraction=0.2", color='gray', lw=1.5))
ax.text(4.5, 1.05, 'Skip Connection', ha='center', va='center', fontsize=9, color='gray')

# Arrow
ax.arrow(6.9, 0.5, 0.5, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Output
ax.add_patch(patches.Rectangle((7.5, 0.3), 1, 0.4, fill=True, color='plum'))
ax.text(8.0, 0.5, 'Output Mask\n(256x256x1)', ha='center', va='center', fontsize=10)

plt.title('Figure: System Architecture (U-Net based Segmentation)', fontsize=12, pad=20)
plt.tight_layout()
plt.savefig('system_architecture.png', dpi=300, bbox_inches='tight')
plt.close()
