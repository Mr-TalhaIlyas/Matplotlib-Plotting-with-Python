import matplotlib.pyplot as plt
import numpy as np
import squarify
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 500
age_in_weeks = np.array(['w0', 'w1', 'w10', 'w11', 'w12', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9'])
number_of_samples = np.array([17379, 29719, 2006, 1913, 826, 29672, 27386, 29490, 17914, 10068, 4676, 3484, 2279])

# Sort age_in_weeks based on the integer value after 'w'
sorted_indices = np.argsort([int(a[1:]) for a in age_in_weeks])

# Apply sorted_indices to age_in_weeks and number_of_samples
age_in_weeks_sorted = age_in_weeks[sorted_indices]
number_of_samples_sorted = number_of_samples[sorted_indices]

# Calculate proportions
total_samples = np.sum(number_of_samples_sorted)
proportions = number_of_samples_sorted / total_samples * 100
proportion_labels = [f'{age}\n({prop:.2f}%)' for age, prop in zip(age_in_weeks_sorted, proportions)]

# Assign a unique color to each rectangle using a colormap
# colors = plt.cm.viridis(np.linspace(0, 1, len(age_in_weeks_sorted)))
colors = plt.cm.tab20(np.linspace(0, 1, len(age_in_weeks_sorted)))

# Create a treemap
fig, ax = plt.subplots(figsize=(10, 13))
squarify.plot(sizes=number_of_samples_sorted, label=proportion_labels, alpha=0.8, color=colors)
# ax.set_title('Proportion of Samples by Age in Weeks (Treemap)')
ax.axis('off')  # Remove axis for better visualization
plt.show()
