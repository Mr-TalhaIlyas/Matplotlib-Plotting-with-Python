import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define data
data = [
    ("ResNet", 42, 2048, 259.71),
    ("ResNext", 86, 2048, 499.35),
    ("MobileNet", 4, 1280, 70.45),
    ("EfficientNet", 52, 1280, 313.34),
    ("ViT", 305, 1024, 69.62),
    ("Swin", 86, 1024, 189.46),
    ("MaxViT", 30, 512, 389.87),
]

# Extract data for the axes
models = [row[0] for row in data]
params = [row[1] for row in data]
embeddings = [row[2] for row in data]
fwd_bwd = [row[3] for row in data]

# Normalize the number of parameters for bubble sizes
sizes = [value * 10 for value in params]

# Define colors for each bubble
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']

# Create the bubble chart
fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(fwd_bwd, embeddings, s=sizes, c=colors, alpha=0.5)

# Set axis labels and title
ax.set_xlabel("Fwd/Bwd Pass (MB)")
ax.set_ylabel("Feature Embeddings (#)")
#ax.set_title("Bubble Chart: Model vs. Fwd/Bwd Pass vs. Feature Embeddings vs. Parameters")

# Add model names as annotations
for i, model in enumerate(models):
    ax.annotate(model, (fwd_bwd[i], embeddings[i]), fontsize=9, ha='center', va='center')

# Adjust plot limits to avoid cutting bubbles
ax.set_ylim(min(embeddings) - 100, max(embeddings) + 100)
ax.set_xlim(min(fwd_bwd) - 20, max(fwd_bwd) + 20)

# Create a custom legend for the number of parameters
legend_patches = [mpatches.Patch(color=colors[i], alpha=0.5, label=f"{models[i]}: {params[i]}M") for i in range(len(models))]
ax.legend(handles=legend_patches, title="Parameters", loc='lower left',  bbox_to_anchor=(-.0, -0.25), borderaxespad=0, ncol=4)
plt.xlim(-0.001, 518)
# Display the plot
plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl
mpl.rcParams['figure.dpi']=500
# Define data
data = [
    ("ResNet", 42, 2048, 259.71),
    ("ResNext", 86, 2048, 499.35),
    ("MobileNet", 4, 1280, 70.45),
    ("EfficientNet", 52, 1280, 313.34),
    ("ViT", 305, 1024, 69.62),
    ("Swin", 86, 1024, 189.46),
    ("MaxViT", 30, 512, 389.87),
]

# Extract data for the axes
models = [row[0] for row in data]
params = [row[1] for row in data]
embeddings = [row[2] for row in data]
fwd_bwd = [row[3] for row in data]

# Normalize the feature embeddings for bubble sizes
sizes = [value / 2 for value in embeddings]

# Define colors for each bubble
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']

# Create the bubble chart
fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(params, fwd_bwd, s=sizes, c=colors, alpha=0.5)

# Set axis labels and title
ax.set_xlabel("Parameters (M)")
ax.set_ylabel("Fwd/Bwd Pass (MB)")
# ax.set_title("Bubble Chart: Model vs. Parameters vs. Fwd/Bwd Pass vs. Feature Embeddings")

# Add model names as annotations
for i, model in enumerate(models):
    ax.annotate(model, (params[i], fwd_bwd[i]), fontsize=9, ha='center', va='center')

# Adjust plot limits to avoid cutting bubbles
ax.set_ylim(min(fwd_bwd) - 20, max(fwd_bwd) + 20)
ax.set_xlim(min(params) - 10, max(params) + 10)

# Create a custom legend for the feature embeddings
legend_patches = [mpatches.Patch(color=colors[i], alpha=0.5, label=f"{embeddings[i]}") for i in range(len(models))]
ax.legend(handles=legend_patches, title="Feature Embeddings Size", loc='lower left',  bbox_to_anchor=(-.0, -0.2), borderaxespad=0, ncol=7)
# plt.xlim(-0.001, 518)
# Display the plot
plt.grid(alpha=0.3)
plt.show()
